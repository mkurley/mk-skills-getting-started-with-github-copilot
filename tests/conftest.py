import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy


# Capture the original activities state at import time
ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to the original seed before each test."""
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield
    # ensure clean state after test as well
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
