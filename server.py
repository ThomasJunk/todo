# SPDX-License-Identifier: MIT
"""Bootstrapping the server
"""

import logging
import os
from wsgiref import simple_server

import falcon
from beaker.middleware import SessionMiddleware
from dotenv import load_dotenv

import database
import middleware
import routes
import todo
import user

load_dotenv()

app = falcon.API(
    middleware=[
        middleware.RequestID(),
        middleware.Session(),
        middleware.SecureHeadersMiddleware()
    ]
)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

database.db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
database.db.generate_mapping(create_tables=True)

login = routes.Login()
logout = routes.Logout()
todos = routes.Todo(todo.create_Service(logging), logging)
users = routes.User(user.create_Service(logging), logging)

app.add_route("/login", login)
app.add_route("/logout", logout)
app.add_route("/todos", todos)
app.add_route("/users", users)

session_opts = {
    "session.type": "memory",
    "session.cookie_expires": os.getenv("COOKIE_EXPIRES", 300),
    "session.auto": True,
    "session.key": os.getenv("COOKIE_NAME", "session")
}
app = SessionMiddleware(app, session_opts)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
