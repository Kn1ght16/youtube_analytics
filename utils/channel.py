import json
import os
from googleapiclient.discovery import build


class Channel():
    api_key = os.environ['YouTubeAPI']

    # YouTube-API  переменная окружения

    def __init__(self, id):
        self.__id = id
        self.json = ""
        self.title = Channel.get_json(self)['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/channel/' + self.__id
        self.subscriber_count = Channel.get_json(self)['items'][0]['statistics']['subscriberCount']
        self.video_count = Channel.get_json(self)['items'][0]['statistics']['videoCount']
        self.view_count = Channel.get_json(self)['items'][0]['statistics']['viewCount']

    def get_json(self):
        with build('youtube', 'v3', developerKey=Channel.api_key) as youtube:
            channel = youtube.channels().list(id=self.__id, part='snippet,statistics').execute()
            self.json = json.dumps(channel, indent=2, ensure_ascii=False)
            return channel

    def print_info(self):
        """Выводит информацию о канале"""
        print(self.json)

    def to_json(self, name):
        """Записывает информацию о канале в файл name"""
        channel_dict = self.__dict__
        print(type(channel_dict))
        with open(f'{name}', 'w', encoding='utf-8') as file:
            file.write(self.json)

    @classmethod
    def get_service(cls):
        with build('youtube', 'v3', developerKey=Channel.api_key) as youtube:
            return youtube
