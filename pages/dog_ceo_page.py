import requests

import conftest
from pages.ya_disk_uploader_page import YaUploader
from routes.dog_ceo_enum import RoutesDocCeo


class DogSeoPage:
    @staticmethod
    def get_sub_breeds(breed: str) -> list:
        res = requests.get(f'{RoutesDocCeo.BASE_URL}{RoutesDocCeo.LIST_BREED.format(breed)}')
        return res.json().get('message', [])

    @staticmethod
    def get_urls_images(breed: str, sub_breeds: list) -> list:
        url_images = []
        if sub_breeds:
            for sub_breed in sub_breeds:
                response = requests.get(
                    f"{RoutesDocCeo.BASE_URL}{RoutesDocCeo.RANDOM_SUB_BREED.format(breed, sub_breed)}")
                url_images.append(response.json().get('message'))
        else:
            response = requests.get(f"{RoutesDocCeo.BASE_URL}{RoutesDocCeo.RANDOM_BREED.format(breed)}")
            url_images.append(response.json().get('message'))
        return url_images

    def upload_images(self, breed: str, folder_name: str) -> list:
        sub_breeds = self.get_sub_breeds(breed)
        urls = self.get_urls_images(breed, sub_breeds)
        yandex_client = YaUploader(conftest.ya_token)
        yandex_client.create_folder(folder_name)
        for url in urls:
            part_name = url.split('/')
            file_name = '_'.join([part_name[-2], part_name[-1]])
            yandex_client.upload_photos_to_yd(folder_name, file_name, url)
        return sub_breeds
