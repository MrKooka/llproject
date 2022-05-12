     
from django.conf import settings
import shutil
from .genVoices import genvoice
def upload_functions(instance)->tuple:
    '''Возвращает путь к файлу и имя файла'''
        
    if hasattr(instance, 'content_object'):
        instance = instance.content_object

    target_path = settings.BASE_DIR / f'llproject/media/{instance.__class__.__name__.lower()}'
    target_filename = f"{instance.eng}.mp3"
    path_for_database = f'{instance.__class__.__name__.lower()}/{target_filename}'

    currnet_path, current_filename = genvoice(instance)

    shutil.move(currnet_path/current_filename, target_path/target_filename)
    return target_filename, target_path, path_for_database



