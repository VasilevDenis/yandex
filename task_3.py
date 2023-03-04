import requests
import json


class Parser:
    def __init__(self, base_url, version, request_type):
        self.base_url = base_url
        self.version = version
        self.request_type = request_type
        self.file_name = request_type + '.txt'

    def get_questions(self, payload):
        self._get_file(payload)
        self._read_json()
        self._print_json()

    def _get_file(self, payload):
        r = requests.get(f'{self.base_url}{self.version}{self.request_type}', params=payload)
        self._save_file(r)

    def _save_file(self, r):
        with open(self.file_name, 'w') as f:
            f.write(r.text)

    def _read_json(self):
        with open(self.file_name) as f:
            self.text = json.load(f)

    def _print_json(self):
        for elem in self.text['items']:
            print(elem['title'])


if __name__ == "__main__":
    payload = {'fromdate': '1677456000',
               'todate': '1677628800',
               'order': 'desc',
               'sort': 'activity',
               'tagged': 'Python',
               'site': 'stackoverflow'}

    parser = Parser('https://api.stackexchange.com/', '2.3/', 'questions')
    parser.get_questions(payload)
