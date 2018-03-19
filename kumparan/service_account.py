from os import environ as env
import logging
from typing import Optional
from typing import Dict

import ujson
from google.oauth2 import service_account

logger = logging.getLogger(__name__)


def get_credentials():
    """Get service credentials from environment variables."""
    env_name = "SERVICE_ACCOUNT_CREDENTIALS"
    cred_str: Optional[str] = env.get(env_name, None)
    if cred_str is None:
        error = "{} is not set".format(env_name)
        raise EnvironmentError(error)

    # Build the credentials
    try:
        cred_info: Dict[str, str] = ujson.loads(cred_str)
        logger.debug("Service Account Credentials is initialized")
    except Exception as err:
        logger.exception("SERVICE_ACCOUNT_CREDENTIALS={}".format(cred_str))
        raise err

    cred = service_account.Credentials.from_service_account_info(cred_info)
    return cred
