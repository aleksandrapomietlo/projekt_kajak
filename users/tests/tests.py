import pytest
from django.contrib.auth import authenticate
from django.urls import reverse


@pytest.mark.django_db
def test_profile_login_view(client, user_data, user):
    '''Test checking login validation
    :param client: fixture client
    :param user: user object for authentication
    :type user: django.contrib.auth.models.User'''
    url = reverse('login')
    response = client.post(url, data=user_data)
    assert response.status_code == 302
    assert response.url == reverse('/home/')
    assert client.login(**user_data) is True
    assert authenticate(username=user_data['username'], password=user_data['password']) == user
    assert client.session['_auth_user_id'] == str(user.pk)


@pytest.mark.django_db
def test_profile_logout_view(client):
    """Test checking rendering views for logged out users.
    :param client: fixture client
    :param view_name: parameter containing the name of the view
    :return: client should be redirected to the logout page,
     http status code is 200"""
    client.logout()
    response = client.post('/logout/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_profile_register_view(client, user_one, user_data):
    ''' Test checking whether user is created with given attributes
    :param user_one: fixture creating a user with given attributes
    :type user_one: django.contrib.auth.models.User'''
    assert user_one.username == 'testuser'
    assert user_one.check_password('password')
    assert user_one.name == 'name'
    assert user_one.surnname == 'surname'
    assert user_one.email == 'test@test.com'
    assert user_one.is_superuser
    response = client.get('/register/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_set_check_user(user):
    '''Test checking whether the username is set correctly'''
    assert user.username == 'testname'
