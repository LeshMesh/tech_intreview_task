import conftest
from pages.dog_ceo_page import DogSeoPage
from pages.ya_disk_uploader_page import YaUploader


def test_upload_dog_no_sub_breed(delete_folder_ya_disk):
    breed = 'doberman'
    folder_name = 'test_folder'
    test_upload_dog_no_sub_breed.folder_name = folder_name
    dog = DogSeoPage()
    dog.upload_images(breed, folder_name)

    yandex_client = YaUploader(conftest.ya_token)
    response = yandex_client.get_info_folder(folder_name)

    assert response.status_code == 200
    assert response.json()['type'] == "dir"
    assert response.json()['name'] == folder_name

    item = response.json()['_embedded']['items']
    assert len(item) == 1
    assert item[0]['type'] == 'file'
    assert item[0]['name'].startswith(breed)


def test_upload_dog_sub_breed(delete_folder_ya_disk):
    breed = 'bulldog'
    folder_name = 'test_folder'
    test_upload_dog_sub_breed.folder_name = folder_name
    dog = DogSeoPage()
    sub_breeds = dog.upload_images(breed, folder_name)

    yandex_client = YaUploader(conftest.ya_token)
    response = yandex_client.get_info_folder(folder_name)

    assert response.status_code == 200
    assert response.json()['type'] == "dir"
    assert response.json()['name'] == folder_name

    items = response.json()['_embedded']['items']
    assert len(items) == len(sub_breeds)
    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)
