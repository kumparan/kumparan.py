# Stubs for google.cloud._http (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

API_BASE_URL: str
DEFAULT_USER_AGENT: Any
CLIENT_INFO_HEADER: str
CLIENT_INFO_TEMPLATE: Any

class Connection:
    USER_AGENT: Any = ...
    def __init__(self, client) -> None: ...
    @property
    def credentials(self): ...
    @property
    def http(self): ...

class JSONConnection(Connection):
    API_BASE_URL: Any = ...
    API_VERSION: Any = ...
    API_URL_TEMPLATE: Any = ...
    @classmethod
    def build_api_url(cls, path, query_params: Optional[Any] = ..., api_base_url: Optional[Any] = ..., api_version: Optional[Any] = ...): ...
    def api_request(self, method, path, query_params: Optional[Any] = ..., data: Optional[Any] = ..., content_type: Optional[Any] = ..., headers: Optional[Any] = ..., api_base_url: Optional[Any] = ..., api_version: Optional[Any] = ..., expect_json: bool = ..., _target_object: Optional[Any] = ...): ...
