import requests
import json
from configuration import *

class TestDropbox:
    def __init__(self):
        self.access_token=ACCESS_TOKEN
        self.test_file=test_file
        self.file_path=file_path

    def file_upload(self):
        url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Dropbox-API-Arg': json.dumps({
                "mode": "add",
                "autorename": True,
                "mute": False,
                "strict_conflict": False,
                "path": self.file_path, }),
            'Content-Type': 'application/octet-stream'
        }
        with open(test_file, 'rb') as file:
            data_file = file.read()
            return requests.post(
                url=url,
                headers=headers,
                data=data_file
            )

    def get_filemetadata(self):
        url = 'https://api.dropboxapi.com/2/sharing/get_file_metadata'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'file': self.file_path
        }
        return requests.post(
            url=url,
            headers=headers,
            json=data
        )

    def file_delete(self):
        url = 'https://api.dropboxapi.com/2/files/delete'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = json.dumps({
            'path': self.file_path
        })
        return requests.post(
            url,
            headers=headers,
            data=data
        )


