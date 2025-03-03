import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("without allure")
@allure.severity(Severity.MINOR)
@allure.label("owner", " ABalsis")
@allure.feature("Поиск issue в репозитории")
@allure.suite("Поиск issue в репозитории")
@allure.story("Поиск issue в репозитории без шагов")
@allure.link("https://github.com", name="Testing")
@allure.title("Поиск issue в репозитории github - шаги allure не размечены")
def test_github_without_report_step():
    browser.open('/')
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.text('Тестируем тест')).should(be.clickable)


@allure.tag("with allure")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", " ABalsis")
@allure.feature("Поиск issue в репозитории")
@allure.suite("Поиск issue в репозитории")
@allure.story("Поиск issue в репозитории с лямбда шагами")
@allure.link("https://github.com", name="Testing")
@allure.title("Поиск issue в репозитории GitHub с лямбда шагами @allure.step")
def test_search_issue_with_lambda_steps():
    with allure.step(f"Открываем главую страницу GitHub"):
        browser.open('/')
    with allure.step("Ищем необходимый репозиторий"):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    with allure.step("Переходим по ссылке в репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с названием 'Тестируем тест' и его кликабельность"):
        browser.element(by.text('Тестируем тест')).should(be.clickable)


@allure.tag("with allure")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", " ABalsis")
@allure.feature("Поиск issue в репозитории")
@allure.suite("Поиск issue в репозитории")
@allure.story("Поиск issue в репозитории c декораторами")
@allure.link("https://github.com", name="Testing")
@allure.title("Поиск issue в репозитории GitHub с использованием @allure.step")
def test_search_issue_with_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_have_text("Тестируем тест")


@allure.step('')
def open_main_page():
    browser.open('/')


@allure.step("Ищем необходимый репозиторий")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Переходим по ссылке в репозиторий")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие issue с названием '{name}' и его кликабельность")
def should_have_text(name):
    browser.element(by.text(name)).should(be.clickable)
