from utils.channel import Channel, Video, PLVideo, Playlist


def main():

    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция
    channel = Channel(channel_id)
    channel.print_info()

    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # Вдудь
    vdud.print_info()

    # получаем значения атрибутов
    print(vdud.title)
    print(vdud.video_count)
    print(vdud.url)

    # менять не можем
    vdud.__id= 'Новое название'

    # можем получить объект для работы с API вне класса
    print(vdud.get_service())

    # создать файл 'vdud.json' в данными по каналу
    vdud.to_json('vdud.json')

    print(channel)
    print(vdud)

    print(channel < vdud)
    print(channel > vdud)
    print(channel + vdud)

    # шаблон: 'название_видео (название_плейлиста)'
    video1 = Video('9lO06Zxhu88')
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    print(video1)
    print(video2)

    pl = Playlist('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    print(pl.title)
    print(pl.url)

    duration = pl.total_duration()
    print(duration)
    print(type(duration))
    print(duration.total_seconds())

    pl.show_best_video()


if __name__ == "__main__":
    main()