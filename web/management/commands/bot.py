from web.models import Word,CastomUser,Message
from django.core.management.base import BaseCommand
from django.conf import settings
from random import randint
from telegram import Bot,Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CallbackContext,
    CommandHandler,
    StringCommandHandler)
from telegram.utils.request import Request







def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка {e}'
            print(error_message)
            raise e



def get_some_word(updater: Update, context: CallbackContext):
    chat_id = updater.message.chat_id
    text = updater.message.text
    count = Word.objects.all().count()
    word = Word.objects.get(pk=randint(1, count))

    # pprint(dir(updater.message))

    reply_text = f'Eng: {word.eng} \nRu: {word.ru}\nContext: {word.context}'
    updater.message.reply_text(text=reply_text)
    
def send_word_for_train(updater:Update, context:CallbackContext, bot:Bot):
    chat_id = updater.message.chat_id
    count = Word.objects.all().count()
    word = Word.objects.get(pk=randint(1, count))
    reply_text = f'Eng: {word.eng} \nRu: {word.ru}\nContext: {word.context}'
    bot.send_message(chat_id=515854171, text=reply_text)

def add_word(updater:Update, context:CallbackContext):
    chat_id = updater.message.chat_id
    text = updater.message.text
    print(context.args)
    p,_ =  CastomUser.objects.get_or_create(
        external_id=chat_id,
        defaults={'name':updater.message.from_user.username}
    )
    m = Message(
        profile=p,
        text=text,
    )

def do_echo(update:Update, context:CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    reply_text = f'Ваш ID: {chat_id}\n\ntext: {text}'
    update.message.reply_text(text=reply_text)


        
class Command(BaseCommand):


    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True
        )
        
        updater.dispatcher.add_handler(
            StringCommandHandler('add', add_word)
        )
        updater.dispatcher.add_handler(
                MessageHandler(callback=do_echo , filters=Filters.text)
        )
        
        updater.start_polling()
        updater.idle()

        
