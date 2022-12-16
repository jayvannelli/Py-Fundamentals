import abc
from ._utils import _init_session


class FmpBase(abc.ABC):
    """Abstract base class for Financial Modeling Prep endpoints."""
    _URL_V3: str = "https://financialmodelingprep.com/api/v3"
    _URL_V4: str = "https://financialmodelingprep.com/api/v4"
    _CONNECTION_TIMEOUT: int = 5
    _READ_TIMEOUT: int = 30

    def __init__(self, api_key: str, session=None):
        """
        Interface to instantiate Fmp reader.

        Parameters
        ----------
        api_key: str
            Financial Modeling Prep (FMP) Api Token.
        session: requests.Session
            Requests session object.
        """
        if api_key is None:
            raise IOError("Fmp api key must be provided.")

        if not isinstance(api_key, str):
            raise TypeError("api_key must be of type str.")

        self.api_key = api_key
        self.session = _init_session(session)

    def close(self):
        """Close requests Session."""
        self.session.close()

    def data(self, url, params):
        """
        Send and return request to FMP endpoint.

        Parameters
        ----------
        url: str
            Full url used in request.
        params: dict
            All parameters (excluding api_key) used in request.
        """
        with self.session as s:
            params.update({"apikey": self.api_key})
            r = s.get(
                url=url, params=params, timeout=(self._CONNECTION_TIMEOUT, self._READ_TIMEOUT)
            )

            if 'Error Message' in r.json():
                raise ValueError("Invalid fmp api key.")

            if r.status_code == 200 and len(r.json()) != 0:
                return r.json()
            elif r.status_code == 403:
                raise ValueError(
                    "The fmp key provided does not have access to this endpoint."
                )

            else:
                raise IOError(
                    f"Request from: {self.__class__} with url: {url} returned empty list."
                )
