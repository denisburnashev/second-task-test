from main import upload, yatoken


class TestResponse:

    def test_response_yan_disk(self):
        assert upload(yatoken) == '200'