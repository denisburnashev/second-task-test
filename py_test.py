import unittest
from main import new_folder_yandisk, upload, yatoken

class TestResponse(unittest.TestCase):

    def test1_response_yan_disk_200(self):
        assert upload(yatoken).status_code == 200, ' Response 200 everything ok'

    def test2_response_yan_disk_400(self):
        assert upload(yatoken).status_code != 400, ' Response 400 Bad request'

    def test3_response_yan_disk_401(self):
        assert upload(yatoken).status_code != 401, ' Response 400 Unauthorized'

    def test1_creating_new_folder_201(self):
        assert new_folder_yandisk(yatoken, 'newfolder').status_code == 201, ' The folder successfully created'

    def test1_creating_new_folder_409(self):
        assert new_folder_yandisk(yatoken, 'newfolder').status_code == 409, ' The folder already exists'
