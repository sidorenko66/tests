import requests
import configparser


def create_folder(token, folder_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.put(url, headers=headers, params=params)
    print(response.status_code)
    print(response.json())
    return response.status_code


def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    yandex_token = config["Yandex"]["yandex_token"]
    folder_name = "new_folder2"
    create_folder(yandex_token, folder_name)


if __name__ == "__main__":
    main()
