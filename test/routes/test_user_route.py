"""Tests user routes
"""

import unittest.mock as mock

import pytest
import falcon

from routes import User

mock_service = mock.Mock()
log = mock.Mock()
user_route = User(mock_service, log)
resp = mock.Mock()


def get_user():
    user = {
        "login": "test",
        "password": "test",
        "groups": ["user"]
    }
    return user


def build_request(session):
    req = mock.Mock()
    context = mock.Mock()
    context.session = session
    req.context = context
    return req


class TestUserRoutes:
    def test_list_users_unauthorized(self):
        with pytest.raises(falcon.errors.HTTPUnauthorized):
            req = build_request({})
            user_route.on_get(req, resp)

    def test_list_users(self):
        req = build_request(session={"user": get_user()})
        mock_service.list.return_value = [get_user()]
        user_route.on_get(req, resp)
        assert len(resp.media) == 1
