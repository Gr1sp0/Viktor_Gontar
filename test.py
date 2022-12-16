from common import TestDropbox
import pytest

global test
test = TestDropbox()


def test_file_upload():
    response = test.file_upload()
    assert response.status_code == 200


def test_get_file_metadata():
    response = test.get_filemetadata()
    assert response.status_code == 200


def test_file_delete():
    response = test.file_delete()
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()