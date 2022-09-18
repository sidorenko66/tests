import unittest
import configparser
import requests
from task2 import create_folder


def delete_folder(token, folder_name):
    print('delete')
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.delete(url, headers=headers, params=params)
    return response.status_code


class MyTestCase(unittest.TestCase):
    def test_get_doc_owner_name(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        yandex_token = config["Yandex"]["yandex_token"]
        folder_name = "my_test_folder"
        self.assertEqual(201, create_folder(yandex_token, folder_name))
        self.assertEqual(409, create_folder(yandex_token, folder_name))
        self.assertEqual(401, create_folder('wrong_api', folder_name))
        self.assertEqual(400, create_folder(yandex_token, ''))
        delete_folder(yandex_token, folder_name)


if __name__ == '__main__':
    unittest.main()
