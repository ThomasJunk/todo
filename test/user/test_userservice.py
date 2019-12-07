"""Tests Userservice
"""

import pytest

import unittest.mock as mock

from passlib.hash import argon2

from user import Service, UserExists, User

mock_repo = mock.Mock()
mock_logger = mock.Mock()
mock_entity = mock.Mock()

user_service = Service(mock_repo, mock_logger, mock_entity)
test_password = "password"
test_password2 = argon2.using(rounds=5).hash("wrong password")


def get_user():
    pw_hash = argon2.using(rounds=5).hash(test_password)
    user = {
        "login": "test",
        "password": pw_hash,
        "groups": ["user"]
    }
    return user


class TestClass:
    def test_list_clears_passwords(self):
        mock_user = mock.Mock()
        mock_user.password = test_password
        result = user_service.clear_password(mock_user)
        assert result.password == ""

    def test_create_existing_user(self):
        with pytest.raises(UserExists):
            mock_repo.exists.return_value = True
            user = get_user()
            user_service.create_new_user(
                user["login"], user["password"])

    def test_create_user(self):
        mock_user = mock.Mock()
        mock_user.to_dict.return_value = get_user()
        mock_repo.exists.return_value = False
        mock_repo.save.return_value = mock_user
        test_user = get_user()
        user_service.create_new_user(
            test_user["login"], test_user["password"])

    def test_grant_login(self):
        user = get_user()
        mock_user = mock.Mock()
        mock_user.password = user["password"]
        mock_repo.get_user_by_login.return_value = mock_user
        result = user_service.grant_login(user["login"], test_password)
        assert result

    def test_grant_login_no_user(self):
        mock_repo.get_user_by_login.return_value = None
        user = get_user()
        result = user_service.grant_login(user["login"], test_password)
        assert not result

    def test_grant_login_wrong_passphrase(self):
        mock_user = mock.Mock()
        mock_user.password = test_password2
        mock_repo.get_user_by_login.return_value = mock_user
        user = get_user()
        result = user_service.grant_login(user["login"], test_password)
        assert not result
