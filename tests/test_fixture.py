from selene import browser, have
import pytest


def test_mobile_fixture(browser_mobile_configuration):
    browser.open('https://github.com')
    browser.element('a[href*="login"]').click()
    browser.element('[class*="authFormHeaderTitle"]').should(have.text('Sign in to GitHub'))


def test_desktop_fixture(browser_desktop_configuration):
    browser.open('https://github.com')
    browser.element('[class*="HeaderMenu-link--sign-in"]').click()
    browser.element('[class*="authFormHeaderTitle"]').should(have.text('Sign in to GitHub'))