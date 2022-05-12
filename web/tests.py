from django.test import TestCase
from django.conf import settings
import shutil
import os
from .utils.genVoices import genvoice
from .utils.uploading import upload_functions

from .models import Word

class VoicesTestCase(TestCase):
    def setUp(self) -> None:
        self.word = Word(ru='мышь',eng='mouse')

    def tests_upload_functions(self):
        target_path,target_filename ,path_for_database = upload_functions(self.word)
        print(path_for_database)
        self.assertIn(target_filename, os.listdir(target_path))


