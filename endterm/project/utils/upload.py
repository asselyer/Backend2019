import os
import shutil
from datetime import datetime


def article_image_path(instance, filename):
    article_id = instance.article.id
    return f'articles/{article_id}/{filename}'

# def task_delete_path(document):
#     file_path = document.path
#     if os.path.isfile(file_path):
#         os.remove(file_path)

