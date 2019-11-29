"""Todo handler
"""

import json
import todo


class Todo:
    """Handles routes for ToDos
    """

    def __init__(self, service):
        self.service = service

    def on_get(self, req, resp):
        """GET request

        Args:
            req (object): request
            resp (resp): response
        """
        todos = self.service.list()
        resp.media = list(todos)

    def on_post(self, req, resp):
        """POST request

        Args:
            req (object): request
            resp (resp): response
        """
        content = req.media.get("todo")["content"]
        item = todo.New(content)
        self.service.save(item)
        resp.media = item.to_dict()
