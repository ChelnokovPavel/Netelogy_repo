import logging
import requests


class YaUploader:
    def __init__(self, token: str, yadisk_file_path: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net'
        self.yadisk_file_path = yadisk_file_path
        self.headers = {'Authorization': self.token}

    def _create_dir(self):
        self.yadisk_dir_path = self.yadisk_file_path.split('/')[:-1]
        res = requests.get(url=f'{self.url}/v1/disk/resources',
                           headers=self.headers,
                           params={'path': self.yadisk_dir_path})
        if res.status_code != 200:
            requests.put(url=f'{self.url}/v1/disk/resources',
                         headers=self.headers,
                         params={'path': self.yadisk_dir_path})
            logging.info('dir %s is created', self.yadisk_dir_path)
        else:
            logging.info('%s is exists', self.yadisk_dir_path)

    def _get_upload_link(self):
        params = {'path': self.yadisk_file_path, 'overwrite': 'true'}
        res = requests.get(url=f'{self.url}/v1/disk/resources/upload',
                           headers=self.headers,
                           params=params)
        if res.json().get('href'):
            return res.json().get('href')
        else:
            raise KeyError(f'Key href is empty')

    def upload(self, path_to_file):
        self._create_dir()
        href = self._get_upload_link()
        res = requests.put(url=href, data=open(path_to_file, 'rb'))
        res.raise_for_status()
        if res.status_code == 201:
            logging.info('Vnature 4etko')


if __name__ == '__main__':
    path_to_file = 'your path here'
    token = 'your token here'
    yadisk_file_path = '/default/default.txt'
    uploader = YaUploader(token, yadisk_file_path)
    uploader.upload(path_to_file)
