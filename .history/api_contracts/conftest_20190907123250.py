"""conftest for contract tests."""
from os import getenv
from os import path

from auth.auth import GrassAuth, UserType
import pytest


@pytest.fixture(scope='session')
def workstation_accounting_session_token():
    """Initialize workstation grass auth token at start of test session."""
    return GrassAuth(
        UserType.WORKSTATION, 70788
    ).grass_token
