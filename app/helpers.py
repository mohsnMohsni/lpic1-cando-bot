# Standard imports
import os
from random import randint
from urllib.parse import urlparse
from urllib.request import urlretrieve


def download_files_from_url(link: str) -> str:
    file_name = 'f%s%s' % (randint(0, 100), os.path.basename(urlparse(link).path))
    urlretrieve(link, file_name)
    return file_name
