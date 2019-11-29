"""Bootstrapping the server
"""

import os

import falcon
from beaker.middleware import SessionMiddleware
from dotenv import load_dotenv

import db
import routes
import todo

load_dotenv()

app = falcon.API()

db = db.create_database(os.getenv("DBFILE", "db.json"))

login = routes.Login()
logout = routes.Logout()
todos = routes.Todo(todo.create_Service(db))

app.add_route("/login", login)
app.add_route("/logout", logout)
app.add_route("/todos", todos)

session_opts = {
    "session.type": "memory",
    "session.cookie_expires": os.getenv("COOKIE_EXPIRES", 300),
    "session.auto": True,
    "session.key": os.getenv("COOKIE_NAME", "session")
}
app = SessionMiddleware(app, session_opts)
