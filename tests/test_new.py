import pytest
from requests.cookies import RequestsCookieJar, create_cookie, remove_cookie_by_name

def test_remove_cookie_by_name():
    # Create a cookie jar and add some cookies
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie2', value='value2', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value3', domain='another.com', path='/'))

    # Verify initial state
    assert len(cookiejar) == 3

    # Remove a specific cookie by name
    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com', path='/')

    # Verify the cookie is removed
    assert len(cookiejar) == 2
    assert 'cookie2' in [cookie.name for cookie in cookiejar]
    assert 'cookie1' in [cookie.name for cookie in cookiejar]

    # Remove another cookie by name across all domains
    remove_cookie_by_name(cookiejar, 'cookie1')

    # Verify all cookies with that name are removed
    assert len(cookiejar) == 1
    assert 'cookie2' in [cookie.name for cookie in cookiejar]

def test_remove_cookie_by_name_no_match():
    # Create a cookie jar and add some cookies
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))

    # Verify initial state
    assert len(cookiejar) == 1

    # Attempt to remove a non-existing cookie by name
    remove_cookie_by_name(cookiejar, 'non_existent_cookie')

    # Verify no cookie is removed
    assert len(cookiejar) == 1
    assert 'cookie1' in [cookie.name for cookie in cookiejar]

def test_remove_cookie_by_name_specific_domain():
    # Create a cookie jar and add some cookies
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='another.com', path='/'))

    # Verify initial state
    assert len(cookiejar) == 2

    # Remove a specific cookie by name and domain
    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com')

    # Verify the cookie is removed only for the specified domain
    assert len(cookiejar) == 1
    assert 'cookie1' in [cookie.name for cookie in cookiejar]
    assert cookiejar._cookies['another.com']['/']['cookie1'].value == 'value2'

def test_remove_cookie_by_name_specific_path():
    # Create a cookie jar and add some cookies with different paths
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/path1'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='example.com', path='/path2'))

    # Verify initial state
    assert len(cookiejar) == 2

    # Remove a specific cookie by name and path
    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com', path='/path1')

    # Verify the cookie is removed only for the specified path
    assert len(cookiejar) == 1
    assert 'cookie1' in [cookie.name for cookie in cookiejar]
    assert cookiejar._cookies['example.com']['/path2']['cookie1'].value == 'value2'

def test_remove_cookie_by_name_domain_mismatch():
    # Create a cookie jar and add some cookies
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='another.com', path='/'))

    # Verify initial state
    assert len(cookiejar) == 2

    # Attempt to remove a cookie with a non-matching domain
    remove_cookie_by_name(cookiejar, 'cookie1', domain='nonexistent.com')

    # Verify no cookie is removed
    assert len(cookiejar) == 2

def test_remove_cookie_by_name_path_mismatch():
    # Create a cookie jar and add some cookies with different paths
    cookiejar = RequestsCookieJar()
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value1', domain='example.com', path='/path1'))
    cookiejar.set_cookie(create_cookie(name='cookie1', value='value2', domain='example.com', path='/path2'))

    # Verify initial state
    assert len(cookiejar) == 2

    # Attempt to remove a cookie with a non-matching path
    remove_cookie_by_name(cookiejar, 'cookie1', domain='example.com', path='/nonexistent')

    # Verify no cookie is removed
    assert len(cookiejar) == 2
