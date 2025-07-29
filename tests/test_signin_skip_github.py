import pytest
from selene import browser, have


def test_signin_skip_mobile(browser_configuration):
    if browser_configuration == 'mobile':
        pytest.skip('Это мобильная версия сайта')
    browser.open('https://github.com')
    browser.element('[class*="HeaderMenu-link--sign-in"]').click()
    browser.element('[class*="authFormHeaderTitle"]').should(have.text('Sign in to GitHub'))

def test_signin_skip_desktop(browser_configuration):
    if browser_configuration == 'desktop':
        pytest.skip('Это десктопная версия версия сайта')
    browser.open('https://github.com')
    browser.element('a[href*="login"]').click()
    browser.element('[class*="authFormHeaderTitle"]').should(have.text('Sign in to GitHub'))