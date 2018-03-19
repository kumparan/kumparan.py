# Stubs for google.cloud.storage.bucket (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from google.cloud.storage._helpers import _PropertyMixin
from typing import Any, Optional

class Bucket(_PropertyMixin):
    def __init__(self, client, name: Optional[Any] = ..., user_project: Optional[Any] = ...) -> None: ...
    @property
    def client(self): ...
    @property
    def user_project(self): ...
    def blob(self, blob_name, chunk_size: Optional[Any] = ..., encryption_key: Optional[Any] = ...): ...
    def notification(self, topic_name, topic_project: Optional[Any] = ..., custom_attributes: Optional[Any] = ..., event_types: Optional[Any] = ..., blob_name_prefix: Optional[Any] = ..., payload_format: Any = ...): ...
    def exists(self, client: Optional[Any] = ...): ...
    def create(self, client: Optional[Any] = ...): ...
    def patch(self, client: Optional[Any] = ...): ...
    @property
    def acl(self): ...
    @property
    def default_object_acl(self): ...
    @staticmethod
    def path_helper(bucket_name): ...
    @property
    def path(self): ...
    def get_blob(self, blob_name, client: Optional[Any] = ..., encryption_key: Optional[Any] = ..., **kwargs): ...
    def list_blobs(self, max_results: Optional[Any] = ..., page_token: Optional[Any] = ..., prefix: Optional[Any] = ..., delimiter: Optional[Any] = ..., versions: Optional[Any] = ..., projection: str = ..., fields: Optional[Any] = ..., client: Optional[Any] = ...): ...
    def list_notifications(self, client: Optional[Any] = ...): ...
    def delete(self, force: bool = ..., client: Optional[Any] = ...): ...
    def delete_blob(self, blob_name, client: Optional[Any] = ...): ...
    def delete_blobs(self, blobs, on_error: Optional[Any] = ..., client: Optional[Any] = ...): ...
    def copy_blob(self, blob, destination_bucket, new_name: Optional[Any] = ..., client: Optional[Any] = ..., preserve_acl: bool = ...): ...
    def rename_blob(self, blob, new_name, client: Optional[Any] = ...): ...
    @property
    def cors(self): ...
    @cors.setter
    def cors(self, entries): ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, mapping): ...
    @property
    def etag(self): ...
    @property
    def id(self): ...
    @property
    def lifecycle_rules(self): ...
    @lifecycle_rules.setter
    def lifecycle_rules(self, rules): ...
    location: Any = ...
    def get_logging(self): ...
    def enable_logging(self, bucket_name, object_prefix: str = ...): ...
    def disable_logging(self): ...
    @property
    def metageneration(self): ...
    @property
    def owner(self): ...
    @property
    def project_number(self): ...
    @property
    def self_link(self): ...
    @property
    def storage_class(self): ...
    @storage_class.setter
    def storage_class(self, value): ...
    @property
    def time_created(self): ...
    @property
    def versioning_enabled(self): ...
    @versioning_enabled.setter
    def versioning_enabled(self, value): ...
    @property
    def requester_pays(self): ...
    @requester_pays.setter
    def requester_pays(self, value): ...
    def configure_website(self, main_page_suffix: Optional[Any] = ..., not_found_page: Optional[Any] = ...): ...
    def disable_website(self): ...
    def get_iam_policy(self, client: Optional[Any] = ...): ...
    def set_iam_policy(self, policy, client: Optional[Any] = ...): ...
    def test_iam_permissions(self, permissions, client: Optional[Any] = ...): ...
    def make_public(self, recursive: bool = ..., future: bool = ..., client: Optional[Any] = ...): ...
    def generate_upload_policy(self, conditions, expiration: Optional[Any] = ..., client: Optional[Any] = ...): ...
