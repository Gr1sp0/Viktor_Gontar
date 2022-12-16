from behave import *
from common import TestDropbox

global test


@given('successful authenticated')
def init(context):
    global test
    test = TestDropbox()


@when('uploading the file to Dropbox')
def file_upload(context):
    context.response=test.file_upload()


@then('the file is uploaded')
def file_upload_check(context):
    assert context.response.status_code == 200


@when('retrieving the metadata of the file')
def get_filemetadata(context):
    context.response=test.get_filemetadata()


@then('the metadata is got')
def get_filemetadata_check(context):
    assert context.response.status_code == 200


@when('delete the file from Dropbox')
def file_delete(context):
    context.response=test.file_delete()


@then('the file is deleted')
def file_delete_check(context):
    assert context.response.status_code == 200