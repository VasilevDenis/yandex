# задание 2
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/'

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get('href', '')
        response = requests.put(url=href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

    def _get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, disk_file_path):
        upload_url = f'{self.url}v1/disk/resources/upload'
        print(upload_url)
        headers = self._get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        href_response = requests.get(upload_url, headers=headers, params=params)
        return href_response.json()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'questions.txt'
    my_file = 'questions.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload_file_to_disk(path_to_file, my_file)

