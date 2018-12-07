import requests
import os

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
url_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'


def translate_it(text, to_lang):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """

    params = {
        'key': key,
        'lang': '{}-ru'.format(to_lang),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def to_lang(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/detect ?
    [key=<API-ключ>]
    & text=<переводимый текст>
    & [hint=<список вероятных языков текста>]
    & [callback=<имя callback-функции>]
    """

    params = {
        'key': key,
        'text': text,
    }

    response = requests.get(url_detect, params=params)
    json_ = response.json()
    return ''.join(json_['lang'])


def get_list_file():
    file_format = '.txt'
    list_file = []
    for file in os.listdir():
        if file_format in file:
            list_file.append(file)
    return list_file


def translate_text():
    for file in get_list_file():
        with open(file, encoding='utf-8') as f:
            init_text = f.read()
            with open((file.split('.')[0] + '_RU.txt'), 'w', encoding='utf-8') as wf:
                wf.write(translate_it(init_text, to_lang(init_text)))


if __name__ == "__main__":
    translate_text()