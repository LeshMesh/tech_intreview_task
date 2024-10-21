import os

import pytest
from dotenv import load_dotenv, find_dotenv

from pages.ya_disk_uploader_page import YaUploader

load_dotenv(find_dotenv())

ya_token = os.getenv("TOKEN")


@pytest.fixture(scope="function")
def delete_folder_ya_disk(request):
    yield
    folder_name = getattr(request.function, "folder_name")
    yandex_client = YaUploader(ya_token)
    yandex_client.delete_folder(folder_name)
