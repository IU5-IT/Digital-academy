# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import requests


def main():
    URL_SITE = 'https://vk.com/im?peers=c141_245145612_345691818&sel=202056822'
    response = requests.get(URL_SITE)
    print(response.text)


if __name__ == '__main__':
    main()
