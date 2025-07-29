from selene import browser, have
import pytest


@pytest.mark.parametrize('browser_desktop_configuration', [(1280,720)], indirect=True)
def test_param_desktop_indirect(browser_desktop_configuration):
    browser.open('https://github.com')
    browser.element('[class*="HeaderMenu-link--sign-in"]').click()
    browser.element('[class*="authFormHeaderTitle"]').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_mobile_configuration', [(320, 658)], indirect=True)
def test_param_mobile_indirect(browser_mobile_configuration):
    browser.open('https://github.com')
    browser.element('a[href*="login"]').click()
    browser.element('[class*="authFormHeaderTitle"]').should(have.text('Sign in to GitHub'))