from utils.channel import Channel


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


if __name__ == "__main__":
    main()