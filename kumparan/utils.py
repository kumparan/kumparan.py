from datetime import datetime
from datetime import timezone


MICROSECONDS = 1000000


def unixtimestamp() -> int:
    """Get the current Unix timestamp in microseconds."""
    timestamp = int(datetime.now(tz=timezone.utc).timestamp() * MICROSECONDS)
    return timestamp
