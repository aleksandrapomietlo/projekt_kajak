import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_data():
    return {
        'username': 'testlogin',
        'password': 'testpass',
    }


@pytest.fixture
def user(db, user_data):
    return User.objects.create_user(**user_data)


@pytest.fixture
def new_user_one(db):
    def create_app_user(
            username: str,
            password: str = None,
            name: str = 'name',
            surname: str = 'surname',
            email: str = 'test@test.com',
            is_superuser: str = False,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            name=name,
            surname=surname,
            email=email,
            is_superuser=is_superuser,
        )
        return user
    return create_app_user


@pytest.fixture
def user_one(db, new_user_one):
    return new_user_one(
        'testuser', 'password', 'name', 'surname', 'test@test.com', is_superuser='False',
    )
