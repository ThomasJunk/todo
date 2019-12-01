"""RequestID Middleware
"""

import uuid


class RequestID:
    """Injects request ids
    """

    def process_request(self, req, resp):
        """Pre routing

        Args:
            req (object): Request
            resp (object): Response
        """
        req.context.request_id = str(uuid.uuid4())
