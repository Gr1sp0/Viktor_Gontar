Feature: Pay Grades test om OrangeHRM

  Scenario: Pay Grades adding and editing
    Given driver initialized
    When login successfully
     And go to Pay Grades
     And add new Pay Grades
    Then have new Pay Grades appeared
     And add new Currency
    Then have new Currency
     And remove Currency
     And remove our Pay Grades