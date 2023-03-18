import pytest
import json
import os
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import isodate
from channel import Channel, Video, PLVideo, Playlist


@pytest.fixture
def channel():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')


@pytest.fixture
def video():
    return Video('9lO06Zxhu88')


@pytest.fixture
def pl_video():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')


@pytest.fixture
def playlist():
    return Playlist('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


def test_channel_init(channel):
    assert channel.id == 'UC1eFXmJNkjITxPFWTy6RsWg'
    assert channel.title == 'Редакция'
    assert channel.url == 'https://www.youtube.com/channel/UC1eFXmJNkjITxPFWTy6RsWg'
    assert channel.subscriber_count == '3710000'
    assert channel.video_count == '600'
    assert channel.view_count == '1054558477'


def test_video_init(video):
    assert video.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video.likes == '976608'
    assert video.view_count == '49410419'


def test_pl_video_init(pl_video):
    assert pl_video.pl_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
    assert pl_video.title == 'Пушкин: наше все?'
    assert pl_video.likes == '18766'
    assert pl_video.view_count == '514810'


def test_playlist_init(playlist):
    assert playlist.id == 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
    assert playlist.title == 'Редакция. АнтиТревел'
    assert playlist.url == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'


def test_playlist_total_seconds(playlist):
    playlist.total_duration = '00:16:15'
    assert playlist.total_seconds() == 975

