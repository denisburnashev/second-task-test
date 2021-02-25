import requests


with open('Yatoken.txt', 'r') as file_object:
    yatoken = file_object.read().strip()


def upload(yatoken):
    respon = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                          params={'path': '/'},
                          headers={"Authorization": f"OAuth {yatoken}"}
                          )
    return respon


def new_folder_yandisk(yatoken, folder_name):
    respon = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                          params={'path': folder_name},
                          headers={"Authorization": f"OAuth {yatoken}"})
    return respon
