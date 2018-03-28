import logging
import sys
from datetime import datetime

from typing import Dict
from typing import Any

import ujson

logger = logging.getLogger(__name__)


class StackdriverLoggingFormatter(logging.Formatter):
    """
    StackdriverLoggingFormatter instances are used to convert a LogRecord
    to JSON-formatted string for Google Stackdriver Logging.

    https://cloud.google.com/logging/

    Example usage:
        handler = logging.StreamHandler(stream=sys.stdout)
        formatter = StackdriverLoggingFormatter()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    """
    def __init__(self, service_name=None, service_version=None):
        # Google StackDriver Timestamp Format
        # 2014-10-02T15:01:23.045123456Z
        # https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
        logging.Formatter.__init__(self)

        self.service_context = None
        if service_name or service_version:
            self.service_context = {
                "service": service_name,
                "version": service_version
            }

    def formatTime(self,
                   record: logging.LogRecord,
                   datefmt: str = None) -> str:
        """
        formatTime formats LogRecord.created seconds in readable UTC format.
        """
        seconds = record.created
        # nanoseconds = seconds * 1e9
        current_time = datetime.utcfromtimestamp(seconds)
        s = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return s

    def format(self, record: logging.LogRecord) -> str:
        # Collect a LogRecord as python dictionary
        log_record: Dict[str, Any] = {}
        log_record["timestamp"] = self.formatTime(record)
        log_record["severity"] = record.levelname
        log_record["message"] = record.getMessage()
        log_record["sourceLocation"] = {
            "file": record.filename,
            "line": record.lineno,
            "function": record.funcName,
        }
        # Handle exception information
        if record.exc_info:
            traceback = self.formatException(record.exc_info)
            # Append the traceback as a newline
            log_record["message"] += "\n{}".format(traceback)

        # Add service context to log record
        if self.service_context:
            log_record["serviceContext"] = self.service_context

        json_str = ujson.dumps(log_record, ensure_ascii=False)
        return json_str


# Example Usage
def main():
    logger.debug("test DEBUG logger")
    logger.info("test INFO logger")
    logger.warning("test WARNING logger")
    logger.error("test ERROR logger")
    logger.critical("test CRITICAL logger")

    try:
        raise ValueError("Input is not valid")
    except Exception as e:
        logger.exception(e)

    try:
        raise OSError("not found")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    # Setup the logging handler and the formatter
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = StackdriverLoggingFormatter(service_name="stackdriver-logging",
                                            service_version="latest")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    main()
