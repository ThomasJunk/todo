# SPDX-License-Identifier: MIT
"""Tests user routes
"""

import unittest.mock as mock

import pytest
import falcon

from routes import User
from user import UserExists

mock_service = mock.Mock()
log = mock.Mock()
user_route = User(mock_service, log)
resp = mock.Mock()

login = "test"
password = "test"
groups = ["user"]


def get_user():
    user = {
        "login": login,
        "password": password,
        "groups": groups
    }
    return user


def build_request(session):
    req = mock.Mock()
    context = mock.Mock()
    context.session = session
    req.context = context
    return req


def build_request_with_user():
    return build_request(session={"user": get_user()})


class TestUserRoutes:
    def test_list_users_unauthorized(self):
        with pytest.raises(falcon.errors.HTTPUnauthorized):
            req = build_request({})
            user_route.on_get(req, resp)

    def test_list_users(self):
        req = build_request_with_user()
        mock_service.list.return_value = [get_user()]
        user_route.on_get(req, resp)
        assert len(resp.media) == 1

    def test_create_user_empty_request(self):
        req = build_request_with_user()
        req.media = {}
        user_route.on_post(req, resp)
        assert resp.status == falcon.HTTP_400

    def test_create_user(self):
        req = build_request_with_user()
        req.media = {"user": get_user()}
        item = mock.Mock()
        item.to_dict.return_value = get_user()
        mock_service.create_new_user.return_value = item
        user_route.on_post(req, resp)
        assert resp.media is not None
        assert resp.media["login"] == login

    def test_create_user_exits(self):
        req = build_request_with_user()
        req.media = {"user": get_user()}
        mock_service.create_new_user.side_effect = UserExists()
        user_route.on_post(req, resp)
        assert resp.status == falcon.HTTP_409
