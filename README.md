# Selenium task Gontar KA-04

## Step 1
Clone project to you local computer

## Step 2
Install all requirements
```pip install -r requirements.txt```

## Step 3
You can use commands in console ```behave``` or ```pytest``` to start test

Also you can go to file ```test_grades.py``` and start one test case or all test suite

## Some peculiarities

- Tests use Google Chrome, if you want to change browser :

1) Go to common\helper.py
2) Change parameter  ```self.driver = webdriver.Chrome()``` to ```self.driver = webdriver.Firefox()``` or another

- Don`t click anything in browser window where test is in process - it will make mistakes in tests
