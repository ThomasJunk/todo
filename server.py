"""Bootstrapping the server
"""

import logging
import os
from wsgiref import simple_server

import falcon
from beaker.middleware import SessionMiddleware
from dotenv import load_dotenv

import db
import routes
import todo
import user

load_dotenv()

app = falcon.API()

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

db = db.create_database(os.getenv("DBFILE", "db.json"))

login = routes.Login()
logout = routes.Logout()
todos = routes.Todo(todo.create_Service(db, logging), logging)
users = routes.User(user.create_Service(db, logging), logging)

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
