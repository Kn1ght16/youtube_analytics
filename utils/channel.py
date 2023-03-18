import json
import os
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import isodate


class MixinYT():
    @classmethod
    def get_service(cls):
        # YouTube-API  переменная окружения
        api_key = os.environ['YouTubeAPI']
        with build('youtube', 'v3', developerKey=api_key) as youtube:
            return youtube


class Channel(MixinYT):
    def __init__(self, id):
        self.__id = id
        self.json = ""
        self.title = Channel.get_json(self)['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/channel/' + self.__id
        self.subscriber_count = Channel.get_json(self)['items'][0]['statistics']['subscriberCount']
        self.video_count = Channel.get_json(self)['items'][0]['statistics']['videoCount']
        self.view_count = Channel.get_json(self)['items'][0]['statistics']['viewCount']

    @property
    def id(self):
        return self.__id

    def get_json(self):
        channel = Channel.get_service().channels().list(id=self.__id, part='snippet,statistics').execute()
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

    def __str__(self):
        return f'Youtube-канал: {self.title}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __lt__(self, other):
        return self.subscriber_count > other.subscriber_count


class Video(MixinYT):
    def __init__(self, id):
        self.__id = id
        try:
            self.title = Video.get_channel(self)['items'][0]['snippet']['title']
            self.likes = Video.get_channel(self)['items'][0]['statistics']['likeCount']
            self.view_count = Video.get_channel(self)['items'][0]['statistics']['viewCount']
        except:
            self.title = None
            self.likes = None
            self.views = None

    def get_channel(self):
        channel = Video.get_service().videos().list(id=self.__id, part='snippet,statistics').execute()
        return channel

    def __str__(self):
        return f'Youtube-канал: {self.title}'


class PLVideo(Video):
    def __init__(self, id, pl_id):
        super().__init__(id)
        self.pl_id = pl_id

    @property
    def pl_title(self):
        playlist = PLVideo.get_service().playlists().list(id=self.pl_id, part='snippet').execute()
        return playlist['items'][0]['snippet']['title']

    def __str__(self):
        return f'Youtube-канал: {self.title} ({self.pl_title})'


class Playlist(MixinYT):
    def __init__(self, id):
        self.id = id
        self.title = Playlist.get_channel(self)["items"][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.id

    def get_channel(self) -> object:
        channel = Playlist.get_service().playlists().list(id=self.id, part='snippet').execute()
        return channel

    def video_list(self):
        playlist = self.get_service().playlistItems().list(playlistId=self.id, part="contentDetails",
                                                           maxResults=50).execute()
        video_list = []
        for item in playlist['items']:
            video_list.append(item['contentDetails']['videoId'])
        return video_list

    def total_duration(self) -> timedelta:
        video_list = self.video_list()
        total_duration = timedelta(seconds=0)
        for item in video_list:
            video = self.get_service().videos().list(id=item, part="contentDetails").execute()
            duration = video['items'][0]['contentDetails']['duration']
            duration_time = isodate.parse_duration(duration)
            total_duration += duration_time
        return total_duration

    def total_seconds(self):
        time_str = self.total_duration
        time_obj = datetime.strptime(time_str, '%H:%M:%S')
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds

    def show_best_video(self):
        video_list = self.video_list()
        best_video = ''
        likes = 0
        for item in video_list:
            video = Video(item)
            if int(video.likes) > likes:
                likes = int(video.likes)
                best_video = item
        return f'"https://www.youtube.com/watch?v={best_video}'
