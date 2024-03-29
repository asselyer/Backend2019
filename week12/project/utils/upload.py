import os
import shutil
from datetime import datetime




def task_document_path(instance, filename):
    project_id = instance.project.id
    return f'projects/{project_id}/{filename}'

# def task_delete_path(document):
#     file_path = document.path
#     if os.path.isfile(file_path):
#         os.remove(file_path)


def task_delete_path(document):
    datetime_path = os.path.abspath(os.path.join(document.path, '..'))
    shutil.rmtree(datetime_path)