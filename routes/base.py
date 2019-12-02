# SPDX-License-Identifier: MIT
"""Initializes route handling class
"""


class RouteBase:
    """Handles routes for ToDos
    """

    def __init__(self, service, log):
        self.service = service
        self.log = log
