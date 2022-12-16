Feature: Test Dropbox's storage

  Scenario: Access for Dropbox storage
    Given successful authenticated
    When uploading the file to Dropbox
    Then the file is uploaded
    When retrieving the metadata of the file
    Then the metadata is got
    When delete the file from Dropbox
    Then the file is deleted