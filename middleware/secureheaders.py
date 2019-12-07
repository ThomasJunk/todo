from secure import SecureHeaders


class SecureHeadersMiddleware:
    def process_response(self, req, resp, resource, req_succeeded):
        """Post-processing of the response (after routing).

        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
            req_succeeded: True if no exceptions were raised while
                the framework processed and routed the request;
                otherwise False.
        """
        secure_headers = SecureHeaders(csp=True, xfo="DENY")
        secure_headers.falcon(resp)
