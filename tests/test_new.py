import pytest
from requests.cookies import RequestsCookieJar, create_cookie, remove_cookie_by_name

def test_remove_cookie_by_name():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie2', value='value2', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value3', domain='another.com', path='/'))

    assert len(cookiejar) == 3

    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com', path='/')

    assert len(cookiejar) == 2
    assert 'cookie2' in [cookie.name for cookie in cookiejar]
    assert 'cookie1' in [cookie.name for cookie in cookiejar]

    remove_cookie_by_name(cookiejar, 'cookie1')

    assert len(cookiejar) == 1
    assert 'cookie2' in [cookie.name for cookie in cookiejar]

def test_remove_cookie_by_name_no_match():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))

    assert len(cookiejar) == 1

    remove_cookie_by_name(cookiejar, 'non_existent_cookie')

    assert len(cookiejar) == 1
    assert 'cookie1' in [cookie.name for cookie in cookiejar]

def test_remove_cookie_by_name_specific_domain():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='another.com', path='/'))

    assert len(cookiejar) == 2

    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com')

    assert len(cookiejar) == 1
    assert 'cookie1' in [cookie.name for cookie in cookiejar]
    assert cookiejar._cookies['another.com']['/']['cookie1'].value == 'value2'

def test_remove_cookie_by_name_specific_path():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/path1'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='example.com', path='/path2'))

    assert len(cookiejar) == 2

    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com', path='/path1')

    assert len(cookiejar) == 1
    assert 'cookie1' in [cookie.name for cookie in cookiejar]
    assert cookiejar._cookies['example.com']['/path2']['cookie1'].value == 'value2'

def test_remove_cookie_by_name_domain_mismatch():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='another.com', path='/'))

    assert len(cookiejar) == 2

    remove_cookie_by_name(cookiejar, 'cookie1', domain='nonexistent.com')

    assert len(cookiejar) == 2

def test_remove_cookie_by_name_path_mismatch():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/path1'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='example.com', path='/path2'))

    assert len(cookiejar) == 2

    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com', path='/nonexistent')

    assert len(cookiejar) == 2

def test_find_cookie_by_name():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))

    assert cookiejar._find('cookie1') == 'value1'

def test_find_cookie_by_name_and_domain():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie2', value='value2', domain='another.com', path='/'))

    assert cookiejar._find('cookie2', domain='another.com') == 'value2'

def test_find_cookie_by_name_domain_and_path():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/path1'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='example.com', path='/path2'))

    assert cookiejar._find('cookie1', domain='example.com', path='/path2') == 'value2'

def test_find_cookie_not_found():
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))

    with pytest.raises(KeyError):
        cookiejar._find('non_existent_cookie')

    with pytest.raises(KeyError):
        cookiejar._find('cookie1', domain='nonexistent.com')

    with pytest.raises(KeyError):
        cookiejar._find('cookie1', domain='example.com', path='/nonexistent')

