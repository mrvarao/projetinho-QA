import random

import requests


def test_create_pet(base_url, headers):
    pet_id = random.randint(10**8, 10**9 - 1)
    payload = {
        "id": pet_id,
        "name": f"rex-{pet_id}",
        "photoUrls": ["https://example.com/rex.jpg"],
        "status": "available",
    }
    response = requests.post(f"{base_url}/pet", json=payload, headers=headers)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == pet_id
    assert body["name"] == f"rex-{pet_id}"

    requests.delete(f"{base_url}/pet/{pet_id}", headers=headers)


def test_get_pet_by_id(base_url, sample_pet):
    response = requests.get(f"{base_url}/pet/{sample_pet['id']}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == sample_pet["id"]
    assert body["name"] == sample_pet["name"]


def test_update_pet(base_url, headers, sample_pet):
    new_name = f"{sample_pet['name']}-updated"
    payload = {**sample_pet, "name": new_name}

    response = requests.put(f"{base_url}/pet", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["name"] == new_name


def test_delete_pet(base_url, headers):
    pet_id = random.randint(10**8, 10**9 - 1)
    payload = {
        "id": pet_id,
        "name": "to-delete",
        "photoUrls": [],
        "status": "available",
    }
    requests.post(f"{base_url}/pet", json=payload, headers=headers)

    response = requests.delete(f"{base_url}/pet/{pet_id}", headers=headers)

    assert response.status_code == 200


def test_find_pets_by_status_available(base_url):
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": "available"})

    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    assert len(pets) > 0
    for pet in pets[:25]:
        assert pet.get("status") == "available"


def test_find_pets_by_tags(base_url):
    response = requests.get(f"{base_url}/pet/findByTags", params={"tags": "tag1"})

    assert response.status_code == 200


def test_upload_pet_image(base_url, sample_pet):
    files = {"file": ("mock.png", b"\x89PNG\r\n\x1a\nmock-bytes", "image/png")}

    response = requests.post(f"{base_url}/pet/{sample_pet['id']}/uploadImage", files=files)

    assert response.status_code == 200
