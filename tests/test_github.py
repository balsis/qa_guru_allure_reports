import allure
from selene import browser, by, be


def test_github_without_report_step():
    browser.open('/')
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.text('Тестируем тест')).should(be.clickable)


@allure.feature("my_feature")
@allure.story("my_story")
@allure.tag("github")
@allure.link("https://github.com", name = "Testing")
def test_github_with_allure_steps_inside_func():
    with allure.step(f"Открываем главую страницу GitHub"):
        browser.open('/')
    with allure.step("Ищем необходимый репозиторий"):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    with allure.step("Переходим по ссылке в репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с названием 'Тестируем тест'"):
        browser.element(by.text('Тестируем тест')).should(be.clickable)


@allure.feature("my_feature")
@allure.story("my_story")
@allure.tag("github")
@allure.link("https://github.com", name = "Testing")
def test_github_with_allure_steps_using_decorators():
    ...
