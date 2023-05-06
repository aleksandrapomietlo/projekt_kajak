import pytest
from django.contrib.auth import authenticate
from django.urls import reverse


@pytest.mark.django_db
def test_profile_login_view(client, user_data, user):
    url = reverse('login')
    response = client.post(url, data=user_data)
    assert response.status_code == 302
    assert response.url == reverse('/home/')
    assert client.login(**user_data) is True
    assert authenticate(username=user_data['username'], password=user_data['password']) == user
    assert client.session['_auth_user_id'] == str(user.pk)


@pytest.mark.django_db
def test_profile_logout_view(client):
    response = client.post('/logout/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_profile_register_view(client, user_one, user_data):
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
    assert user.username == 'testname'
