import os
import shutil
from datetime import datetime




def post_mediafile_path(instance, filename):
  return f'posts/{filename}'

def post_delete_path(mediafile):
    file_path = mediafile.path
    if os.path.isfile(file_path):
        os.remove(file_path)


# def post_delete_path(mediafile):
#     datetime_path = os.path.abspath(os.path.join(mediafile.path, '..'))
#     shutil.rmtree(datetime_path)