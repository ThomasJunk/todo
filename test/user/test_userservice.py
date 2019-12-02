"""Tests Userservice
"""

import pytest

from unittest.mock import Mock

from passlib.hash import argon2

from user import Service, UserExists, User

mock_repo = Mock()
mock_logger = Mock()

user_service = Service(mock_repo, mock_logger)
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
        item = Mock()
        item.to_dict.return_value = get_user()
        mock_repo.list.return_value = [item]
        result = user_service.list()
        assert len(result) == 1
        assert result[0]["password"] == ""

    def test_create_existing_user(self):
        with pytest.raises(UserExists):
            mock_repo.exists.return_value = True
            _ = user_service.create_new_user("test", test_password)

    def test_create_user(self):
        login = "test"
        user = Mock()
        user.login = login
        user.password = test_password
        user.to_dict.return_value = get_user()
        mock_repo.exists.return_value = False
        mock_repo.save.return_value = user
        result = user_service.create_new_user(login, test_password)
        assert result["password"] == ""
        assert result["login"] == "test"

    def test_grant_login(self):
        mock_repo.get_user_by_login.return_value = get_user()
        result = user_service.grant_login("test", test_password)
        assert result

    def test_grant_login_no_user(self):
        mock_repo.get_user_by_login.return_value = None
        result = user_service.grant_login("test", test_password)
        assert not result

    def test_grant_login_wrong_passphrase(self):
        mock_repo.get_user_by_login.return_value = get_user()
        result = user_service.grant_login("test", test_password2)
        assert not result
