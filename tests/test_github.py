from selene import browser


def test_github_without_report_step():
    browser.open('/')


def test_github_with_allure_steps_inside_func():
    ...

def test_github_with_allure_steps_using_decorators():
    ...