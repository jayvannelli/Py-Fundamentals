from abc import ABC, abstractmethod
from ._utils import _init_session


class FmpReader(ABC):
    """Establishes child with basic FMP Reader interface."""

    @abstractmethod
    def __init__(self, api_key: str, session):
        """Interface for standard Fmp reader classes.

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

        self._url_v3 = "https://financialmodelingprep.com/api/v3"
        self._url_v4 = "https://financialmodelingprep.com/api/v4"
        self._conn_timeout = 5
        self._read_timeout = 30

    def close(self):
        """Close requests.Session."""
        self.session.close()

    def _data(self, url_version: str, path: str, params: dict[str, int | str | float]):
        if url_version == "v3":
            url = f"{self._url_v3}/{path}"
        elif url_version == "v4":
            url = f"{self._url_v4}/{path}"
        else:
            raise ValueError(f"Invalid url_version: {url_version}. Valid url_version values are: 'v3' or 'v4'.")
        params.update({"apikey": self.api_key})
        response = self.session.get(
            url=url, params=params, timeout=(self._conn_timeout, self._read_timeout)
        )

        if 'Error Message' in response.json():
            raise ValueError("Invalid fmp api key.")

        if response.status_code == 200 and len(response.json()) != 0:
            return response.json()
        elif response.status_code == 403:
            raise ValueError(
                "The fmp key provided does not have access to this endpoint."
            )
        elif 'Error Message' in response.json():
            raise ValueError("Invalid fmp api key.")

        else:
            raise IOError(
                f"Request from: {self.__class__} with url: {url} returned empty list."
            )
