import unittest
from common.helper import GradestTest

global tester


def test_init_driver():
    global tester
    tester = GradestTest()


def test_login_page():
    tester.login_page()


def test_main_page():
    tester.main_page()

def test_pay_grades_page():
    tester.pay_grades_page()


def test_add_currency():
    tester.add_currency()


def test_check_new_Currency():
    tester.check_new_Currency()


def test_remove_Currency():
    tester.remove_Currency()


def test_delete_grades():
    tester.delete_grades()


if __name__ == '__main__':
    unittest.main()