import random

import requests


def test_get_inventory(base_url):
    response = requests.get(f"{base_url}/store/inventory")

    assert response.status_code == 200
    inventory = response.json()
    assert isinstance(inventory, dict)
    for value in inventory.values():
        assert isinstance(value, int)


def test_create_order(base_url, headers, sample_pet):
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
    body = response.json()
    assert "id" in body
    assert body["petId"] == sample_pet["id"]

    requests.delete(f"{base_url}/store/order/{body['id']}", headers=headers)


def test_get_order_by_id(base_url, sample_order):
    response = requests.get(f"{base_url}/store/order/{sample_order['id']}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == sample_order["id"]
    assert body["petId"] == sample_order["petId"]


def test_delete_order(base_url, headers, sample_pet):
    order_id = random.randint(1, 10)
    payload = {
        "id": order_id,
        "petId": sample_pet["id"],
        "quantity": 1,
        "status": "placed",
        "complete": True,
    }
    created = requests.post(f"{base_url}/store/order", json=payload, headers=headers).json()

    response = requests.delete(f"{base_url}/store/order/{created['id']}", headers=headers)

    assert response.status_code == 200
