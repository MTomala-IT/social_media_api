"""
to configure fixtures to share data within multiple tests
"""

from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient  # interacting with API without starting the server
from httpx import AsyncClient  # making requests to our API

from socialmedia_api.main import app
from socialmedia_api.routers.post import comment_table, post_table


# Runs once for entire test session
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


# test client to interact with, instead of starting FAST API server
# yielding instead of returning allow to do something before or after that, 'setUp', 'tearDown' etc.
@pytest.fixture()
def client() -> Generator:
    print("Getting test client")
    yield TestClient(app)


# @pytest.fixture() to be shared between multiple tests
# clear the tables before we run every time
@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
