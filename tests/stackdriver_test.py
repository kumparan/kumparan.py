import unittest
import logging

import ujson

from kumparan.stackdriver import StackdriverLoggingFormatter


def init_logger(output_path: str,
                service_name: str,
                service_version: str) -> logging.Logger:
    """init_logger Initialize new logging.Logger

    Arguments:
        output_path {str} -- Path to the .log file
        service_name {str} -- Service name for the stackdriver
        service_version {str} -- Service version of the stackdriver

    Returns:
        logging.Logger -- Class of the logging.Logger
    """

    logger = logging.getLogger(__name__)
    # Setup the logging handler and the formatter
    service_name = "test"
    service_version = "test"
    handler = logging.FileHandler(filename=output_path)
    formatter = StackdriverLoggingFormatter(
                    service_name=service_name,
                    service_version=service_version)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


class TestStackdriverLogging(unittest.TestCase):

    def test_severity_debug(self):
        # Setup the logging handler and the formatter
        log_file_path = "stackdriver_test_debug.log"
        service_name = "test"
        service_version = "test"
        service_context = {
            "service": service_name,
            "version": service_version
        }
        logger = init_logger(output_path=log_file_path,
                             service_name=service_name,
                             service_version=service_version)

        logger.debug("message")
        with open(log_file_path) as f:
            line = f.read().strip()
        log_record = ujson.loads(line)

        # Make sure the logging is correct
        self.assertTrue("timestamp" in log_record)
        self.assertEqual(log_record["severity"], "DEBUG")
        self.assertEqual(log_record["message"], "message")
        self.assertEqual(log_record["serviceContext"], service_context)
        self.assertTrue("sourceLocation" in log_record)

    def test_severity_info(self):
        # Setup the logging handler and the formatter
        log_file_path = "stackdriver_test_info.log"
        service_name = "test"
        service_version = "test"
        service_context = {
            "service": service_name,
            "version": service_version
        }
        logger = init_logger(output_path=log_file_path,
                             service_name=service_name,
                             service_version=service_version)

        logger.info("message")
        with open(log_file_path) as f:
            line = f.read().strip()
        log_record = ujson.loads(line)

        # Make sure the logging is correct
        self.assertTrue("timestamp" in log_record)
        self.assertEqual(log_record["severity"], "INFO")
        self.assertEqual(log_record["message"], "message")
        self.assertEqual(log_record["serviceContext"], service_context)
        self.assertTrue("sourceLocation" in log_record)

    def test_severity_warning(self):
        # Setup the logging handler and the formatter
        log_file_path = "stackdriver_test_warning.log"
        service_name = "test"
        service_version = "test"
        service_context = {
            "service": service_name,
            "version": service_version
        }
        logger = init_logger(output_path=log_file_path,
                             service_name=service_name,
                             service_version=service_version)

        logger.warning("message")
        with open(log_file_path) as f:
            line = f.read().strip()
        log_record = ujson.loads(line)

        # Make sure the logging is correct
        self.assertTrue("timestamp" in log_record)
        self.assertEqual(log_record["severity"], "WARNING")
        self.assertEqual(log_record["message"], "message")
        self.assertEqual(log_record["serviceContext"], service_context)
        self.assertTrue("sourceLocation" in log_record)

    def test_severity_error(self):
        # Setup the logging handler and the formatter
        log_file_path = "stackdriver_test_error.log"
        service_name = "test"
        service_version = "test"
        service_context = {
            "service": service_name,
            "version": service_version
        }
        logger = init_logger(output_path=log_file_path,
                             service_name=service_name,
                             service_version=service_version)

        logger.error("message")
        with open(log_file_path) as f:
            line = f.read().strip()
        log_record = ujson.loads(line)

        # Make sure the logging is correct
        self.assertTrue("timestamp" in log_record)
        self.assertEqual(log_record["severity"], "ERROR")
        self.assertEqual(log_record["message"], "message")
        self.assertEqual(log_record["serviceContext"], service_context)
        self.assertTrue("sourceLocation" in log_record)

    def test_severity_critical(self):
        # Setup the logging handler and the formatter
        log_file_path = "stackdriver_test_critical.log"
        service_name = "test"
        service_version = "test"
        service_context = {
            "service": service_name,
            "version": service_version
        }
        logger = init_logger(output_path=log_file_path,
                             service_name=service_name,
                             service_version=service_version)

        logger.critical("message")
        with open(log_file_path) as f:
            line = f.read().strip()
        log_record = ujson.loads(line)

        # Make sure the logging is correct
        self.assertTrue("timestamp" in log_record)
        self.assertEqual(log_record["severity"], "CRITICAL")
        self.assertEqual(log_record["message"], "message")
        self.assertEqual(log_record["serviceContext"], service_context)
        self.assertTrue("sourceLocation" in log_record)

    def test_severity_exception(self):
        # Setup the logging handler and the formatter
        log_file_path = "stackdriver_test_exception.log"
        service_name = "test"
        service_version = "test"
        service_context = {
            "service": service_name,
            "version": service_version
        }
        logger = init_logger(output_path=log_file_path,
                             service_name=service_name,
                             service_version=service_version)

        try:
            raise ValueError("Input is not valid")
        except Exception as e:
            logger.exception(e)

        with open(log_file_path) as f:
            line = f.read().strip()
        log_record = ujson.loads(line)

        # Make sure the logging is correct
        self.assertTrue("timestamp" in log_record)
        self.assertEqual(log_record["severity"], "ERROR")
        self.assertTrue("ValueError" in log_record["message"])
        self.assertEqual(log_record["serviceContext"], service_context)
        self.assertTrue("sourceLocation" in log_record)


if __name__ == '__main__':
    unittest.main()
