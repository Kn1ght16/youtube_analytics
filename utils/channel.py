import json
import os
from googleapiclient.discovery import build


class Channel():
    api_key = os.environ['YouTube-API']
    # YouTube-API  переменная окружения

    def __init__(self, id):
        self.id = id
        self.json = ""
        self.get_json_by_id()

    def get_json_by_id(self):
        with build('youtube', 'v3', developerKey=Channel.api_key) as youtube:
            channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
            self.json = json.dumps(channel, indent=2, ensure_ascii=False)

    def print_info(self):
        print(self.json)
