import pytest
from selene import browser


@pytest.fixture(params=[
    ('2560','1440'),
    ('1920','1080'),
    ('1600','900'),
    ('1280','720'),
    ('425','768'),
    ('414', '896'),
    ('390','844'),
    ('320','658')
])
def browser_configuration(request):
    width, height = map(int, request.param)
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1023:
        yield 'desktop'
    else:
        yield 'mobile'
    browser.quit()
