from datetime import datetime
from email.mime import audio
from web.models import Word,CastomUser,Message
import random
from django.core.management.base import BaseCommand
from django.conf import settings
import logging
from typing import List
from telegram.utils.request import Request
from telegram import Bot
from telegram import ReplyKeyboardRemove, Update, KeyboardButton,ReplyKeyboardMarkup, chat
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext,
    InvalidCallbackData,
    PicklePersistence,
    MessageHandler,Filters
)


button_start = '/get_word'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Запускает бота и создает кнопку"""
    logger.info('Запустилась start')
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Начать'),
                KeyboardButton(text='Стоп')
            ]
        ],
        resize_keyboard=True
    )
    count_wrds = Word.objects.filter(reply_date__lte=datetime.now().timestamp()).count()
    update.message.reply_text(
        text=f'У вас {count_wrds} свежих слов',
        reply_markup=reply_markup,
    )

def start_train(update: Update, context:CallbackContext):
    if update.message and update.message.text =='Начать':
        logger.info('Запустилась start_train')
        first_word = Word.objects.filter(reply_date__lte=datetime.now().timestamp(), number_responses__lt=6).all()[:1][0]
        # context.chat_data['current_word'] = Word.objects.filter(reply_date__lte=datetime.now().timestamp()).all()[:2][1]
        get_word(update=update, context=context, first_word=first_word)

def get_word(update: Update, context:CallbackContext, first_word=None):
    logger.info('Запустилась get_word')
    if first_word:
        current_word = first_word
    else:
        current_word = context.chat_data['next_word']
    word_list = Word.objects.filter(pk__gte=current_word.pk)[:4]
    context.chat_data['next_word'] = word_list[1]
    current_word: Word
    # перемешиваем наш массив со словами. 
    word_list = sorted(word_list, key=lambda A: random.random())

    if current_word.bot_path:
        with open(current_word.bot_path, 'rb') as file:
            context.bot.send_audio(
                caption=f'{current_word.eng}\n{current_word.context if current_word.context !="context" else ""}',
                audio=file,
                reply_markup=build_keyboard(word_list, current_word),
                chat_id=update.message.chat_id
            )
    else:
        context.bot.send_message(
            text=f'{current_word.eng}\n{current_word.context if current_word.context !="context" else ""}',
            reply_markup=build_keyboard(word_list, current_word),
            chat_id=515854171
        )


def clear(update: Update, context: CallbackContext) -> None:
    if update.message.text == 'Стоп':
        context.bot.callback_data_cache.clear_callback_data()  # type: ignore[attr-defined]
        context.bot.callback_data_cache.clear_callback_queries()  # type: ignore[attr-defined]
        update.effective_message.reply_text('ok')


def build_keyboard(word_list: List[str],current_word: str) -> InlineKeyboardMarkup:
    """Создает и возвращает кнопки с вариантами ответа."""
    logger.info('Запустилась build_keyboard')
    return InlineKeyboardMarkup.from_column(
        [InlineKeyboardButton(i.ru, callback_data=(i, current_word )) for i in word_list])


def list_button(update: Update, context: CallbackContext) -> None:
    """Проверяет ответа пользователя и говорит правильно ли тот ответил или нет"""
    logger.info('Запустилась list_button')
    query = update.callback_query
    selected_word, current_word= query.data
    current_word: Word
    flug = True

    if selected_word.ru == current_word.ru:
        # Счетчик ответов пользователя на данное слово
        current_word.number_responses += 1
        # Проверка на то , что человек ответил правильно 8 раз на данное слово
        if current_word.number_responses >= 8:
            current_word.is_remember = True
 
        # Проверка на то, что челове ответил на слово не с первого раза.
        if not flug:
            current_word.reply_date = random.randint(7200,18000) + int(datetime.now().timestamp())
        else:
            current_word.reply_date = random.randint(86400,129600) + int(datetime.now().timestamp())

        current_word.save()

        update.effective_message.reply_text(f'Ага! {current_word.eng} - {current_word.ru}')
        context.drop_callback_data(query)
        return get_word(update=update, context=context)
        
    else:
        flug = False
        query.answer('Неа')
        update.effective_message.reply_text('Неа')
        

        

    # we can delete the data stored for the query, because we've replaced the buttons



def handle_invalid_button(update: Update, context: CallbackContext) -> None:
    print('Сработала handle_invalid_button _--------------------')
    """Informs the user that the button is no longer available."""
    update.callback_query.answer()
    update.effective_message.edit_text(
        'Нажмите кнопку начать.'
    )

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        updater = Updater(settings.TOKEN, arbitrary_callback_data=True)

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CommandHandler('get_word', get_word))

        # updater.dispatcher.add_handler(CommandHandler('stop', clear))
        updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('Начать'), callback=start_train))
        updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('Стоп'), callback=clear))


        updater.dispatcher.add_handler(
            CallbackQueryHandler(handle_invalid_button, pattern=InvalidCallbackData)
        )   
        updater.dispatcher.add_handler(CallbackQueryHandler(list_button))

        # Start the Bot
        updater.start_polling()

        # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT
        updater.idle()

