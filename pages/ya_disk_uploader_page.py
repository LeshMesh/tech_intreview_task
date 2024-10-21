import requests
from requests import Response

from routes.ya_disk_enum import RoutesYaDisk


class YaUploader:
    def __init__(self, token):
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}

    def create_folder(self, path: str) -> None:
        url = RoutesYaDisk.BASE_URL + RoutesYaDisk.RESOURCES
        requests.put(f'{url}?path={path}', headers=self.headers)

    def _wait_operation_success(self, response: Response):
        url_operation = response.json()['href']
        status = "in-progress"
        while status == "in-progress":
            resp = requests.get(url_operation, headers=self.headers)
            status = resp.json()['status']
        assert status == "success"

    def upload_photos_to_yd(self, folder_name: str, file_name: str, url_file: str) -> None:
        url = RoutesYaDisk.BASE_URL + RoutesYaDisk.RESOURCES_UPLOAD
        params = {"path": f'/{folder_name}/{file_name}', 'url': url_file, "overwrite": "true"}
        response = requests.post(url, headers=self.headers, params=params)
        self._wait_operation_success(response)

    def get_info_folder(self, folder_name) -> Response:
        url = f'{RoutesYaDisk.BASE_URL + RoutesYaDisk.RESOURCES}?path=/{folder_name}'
        return requests.get(url, headers=self.headers)

    def delete_folder(self, folder_name) -> None:
        url = f'{RoutesYaDisk.BASE_URL + RoutesYaDisk.RESOURCES}?path=/{folder_name}'
        params = {"path": f'/{folder_name}', "permanently": True}
        requests.delete(url, headers=self.headers, params=params)
