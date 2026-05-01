import random

import pytest
import requests


BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def headers():
    return {"Content-Type": "application/json"}


@pytest.fixture
def sample_pet(base_url, headers):
    pet_id = random.randint(10**8, 10**9 - 1)
    payload = {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": f"fixture-pet-{pet_id}",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available",
    }
    response = requests.post(f"{base_url}/pet", json=payload, headers=headers)
    assert response.status_code == 200
    pet = response.json()

    yield pet

    requests.delete(f"{base_url}/pet/{pet['id']}", headers=headers)


@pytest.fixture
def sample_order(base_url, headers, sample_pet):
    order_id = random.randint(1, 10)
    payload = {
        "id": order_id,
        "petId": sample_pet["id"],
        "quantity": 1,
        "status": "placed",
        "complete": True,
    }
    response = requests.post(f"{base_url}/store/order", json=payload, headers=headers)
    assert response.status_code == 200
    order = response.json()

    yield order

    requests.delete(f"{base_url}/store/order/{order['id']}", headers=headers)
