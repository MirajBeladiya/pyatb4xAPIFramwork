import pytest
import allure

@allure.title("Hello")
def test_sample():
    assert True == True