# Stubs for google.cloud.storage.client (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from google.cloud.client import ClientWithProject
from typing import Any, Optional

class Client(ClientWithProject):
    SCOPE: Any = ...
    def __init__(self, project: Optional[Any] = ..., credentials: Optional[Any] = ..., _http: Optional[Any] = ...) -> None: ...
    @property
    def current_batch(self): ...
    def bucket(self, bucket_name, user_project: Optional[Any] = ...): ...
    def batch(self): ...
    def get_bucket(self, bucket_name): ...
    def lookup_bucket(self, bucket_name): ...
    def create_bucket(self, bucket_name, requester_pays: Optional[Any] = ...): ...
    def list_buckets(self, max_results: Optional[Any] = ..., page_token: Optional[Any] = ..., prefix: Optional[Any] = ..., projection: str = ..., fields: Optional[Any] = ...): ...
