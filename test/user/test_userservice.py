"""Tests Userservice
"""

import pytest

import unittest.mock as mock

from user import Service, UserExists, User

mock_repo = mock.Mock()
mock_logger = mock.Mock()
mock_entity = mock.Mock()
mock_crypto_service = mock.Mock()

user_service = Service(mock_repo,
                       mock_logger,
                       mock_entity,
                       mock_crypto_service
                       )


def get_user():
    user = {
        "login": "test",
        "password": "password",
        "groups": ["user"]
    }
    return user


class TestClass:
    def test_list_clears_passwords(self):
        mock_user = mock.Mock()
        mock_user.password = "test"
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
        mock_repo.get_user_by_login.return_value = mock_user
        mock_crypto_service.verify_password.return_value = True
        result = user_service.grant_login(user["login"], "test")
        assert result

    def test_grant_login_no_user(self):
        mock_repo.get_user_by_login.return_value = None
        mock_crypto_service.verify_password.return_value = False
        user = get_user()
        result = user_service.grant_login(user["login"], "test")
        assert not result

    def test_grant_login_wrong_passphrase(self):
        mock_user = mock.Mock()
        mock_repo.get_user_by_login.return_value = mock_user
        mock_crypto_service.verify_password.return_value = False
        user = get_user()
        result = user_service.grant_login(user["login"], "test")
        assert not result
