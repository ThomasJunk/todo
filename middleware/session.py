"""Session Middleware
"""


class Session:
    """Injects session
    """

    def process_request(self, req, resp):
        """Pre routing

        Args:
            req (object): Request
            resp (object): Response
        """
        session = session = req.env["beaker.session"]
        req.context.session = session
