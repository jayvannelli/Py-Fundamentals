import requests


def _init_session(session: requests.Session | None) -> requests.Session:
    """Initialize requests session. """
    if isinstance(session, requests.Session):
        return session

    if session is None:
        return requests.Session()
