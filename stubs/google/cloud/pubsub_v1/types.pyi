# Stubs for google.cloud.pubsub_v1.types (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from typing import Any, List

BatchSettings = namedtuple('BatchSettings', ['max_bytes', 'max_latency', 'max_messages'])

FlowControl = namedtuple('FlowControl', ['max_bytes', 'max_messages', 'resume_threshold'])

class TestIamPermissionsResponse:
    def __init__(self) -> None: ...
    @property
    def permissions(self) -> List[str]: ...

# Names in __all__ with no definition:
#   AcknowledgeRequest
#   AcknowledgeRequest
#   AuditData
#   BatchSettings
#   Binding
#   BindingDelta
#   CreateSnapshotRequest
#   CreateSnapshotRequest
#   CustomHttpPattern
#   DeleteSnapshotRequest
#   DeleteSnapshotRequest
#   DeleteSubscriptionRequest
#   DeleteSubscriptionRequest
#   DeleteTopicRequest
#   DeleteTopicRequest
#   DescriptorProto
#   Duration
#   Empty
#   EnumDescriptorProto
#   EnumOptions
#   EnumValueDescriptorProto
#   EnumValueOptions
#   ExtensionRangeOptions
#   FieldDescriptorProto
#   FieldMask
#   FieldOptions
#   FileDescriptorProto
#   FileDescriptorSet
#   FileOptions
#   FlowControl
#   GeneratedCodeInfo
#   GetIamPolicyRequest
#   GetSubscriptionRequest
#   GetSubscriptionRequest
#   GetTopicRequest
#   GetTopicRequest
#   Http
#   HttpRule
#   ListSnapshotsRequest
#   ListSnapshotsRequest
#   ListSnapshotsResponse
#   ListSnapshotsResponse
#   ListSubscriptionsRequest
#   ListSubscriptionsRequest
#   ListSubscriptionsResponse
#   ListSubscriptionsResponse
#   ListTopicSubscriptionsRequest
#   ListTopicSubscriptionsRequest
#   ListTopicSubscriptionsResponse
#   ListTopicSubscriptionsResponse
#   ListTopicsRequest
#   ListTopicsRequest
#   ListTopicsResponse
#   ListTopicsResponse
#   MessageOptions
#   MethodDescriptorProto
#   MethodOptions
#   ModifyAckDeadlineRequest
#   ModifyAckDeadlineRequest
#   ModifyPushConfigRequest
#   ModifyPushConfigRequest
#   OneofDescriptorProto
#   OneofOptions
#   Policy
#   PolicyDelta
#   PublishRequest
#   PublishRequest
#   PublishResponse
#   PublishResponse
#   PubsubMessage
#   PubsubMessage
#   PullRequest
#   PullRequest
#   PullResponse
#   PullResponse
#   PushConfig
#   PushConfig
#   ReceivedMessage
#   ReceivedMessage
#   SeekRequest
#   SeekRequest
#   SeekResponse
#   SeekResponse
#   ServiceDescriptorProto
#   ServiceOptions
#   SetIamPolicyRequest
#   Snapshot
#   Snapshot
#   SourceCodeInfo
#   StreamingPullRequest
#   StreamingPullRequest
#   StreamingPullResponse
#   StreamingPullResponse
#   Subscription
#   Subscription
#   TestIamPermissionsRequest
#   TestIamPermissionsResponse
#   Timestamp
#   Topic
#   Topic
#   UninterpretedOption
#   UpdateSnapshotRequest
#   UpdateSnapshotRequest
#   UpdateSubscriptionRequest
#   UpdateSubscriptionRequest
#   UpdateTopicRequest
#   UpdateTopicRequest
