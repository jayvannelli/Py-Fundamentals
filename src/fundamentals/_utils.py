import requests


def _init_session(session: requests.Session | None) -> requests.Session:
    """Initialize requests session. """
    if isinstance(session, requests.Session):
        return session

    if session is None:
        return requests.Session()


def _validate_period(period: str) -> str:
    """Validate period value; Only returns if valid."""
    from ._constants import VALID_PERIODS

    if not isinstance(period, str):
        raise TypeError(f"Invalid period: {period}. period must be of type: str.")

    if period not in VALID_PERIODS:
        raise ValueError(f"Invalid period: {period}. Valid period values include: {VALID_PERIODS}. ")

    return period


def _validate_limit(limit: int) -> int:
    """Validate limit value; Only returns if valid."""
    from ._constants import HIGH_LIMIT

    if not isinstance(limit, int):
        raise TypeError("Limit must be of type: int.")

    if limit <= 0 or limit > HIGH_LIMIT:
        raise ValueError(f"Limit must a value between 0 and {HIGH_LIMIT}.")

    return limit
