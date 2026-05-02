import uuid

import pytest
import requests


def _build_user(username):
    return {
        "id": 0,
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": f"{username}@example.com",
        "password": "p@ssw0rd",
        "phone": "5551234567",
        "userStatus": 1,
    }


@pytest.fixture
def sample_user(base_url, headers):
    username = f"user-{uuid.uuid4().hex[:10]}"
    payload = _build_user(username)
    response = requests.post(f"{base_url}/user", json=payload, headers=headers)
    assert response.status_code == 200

    yield payload

    requests.delete(f"{base_url}/user/{username}", headers=headers)


def test_create_user(base_url, headers):
    username = f"user-{uuid.uuid4().hex[:10]}"
    response = requests.post(f"{base_url}/user", json=_build_user(username), headers=headers)

    assert response.status_code == 200

    requests.delete(f"{base_url}/user/{username}", headers=headers)


def test_create_users_with_list(base_url, headers):
    usernames = [f"user-{uuid.uuid4().hex[:8]}" for _ in range(3)]
    payload = [_build_user(u) for u in usernames]

    response = requests.post(f"{base_url}/user/createWithList", json=payload, headers=headers)

    assert response.status_code == 200

    for username in usernames:
        requests.delete(f"{base_url}/user/{username}", headers=headers)


def test_get_user_by_username(base_url, sample_user):
    response = requests.get(f"{base_url}/user/{sample_user['username']}")

    assert response.status_code == 200
    assert response.json()["username"] == sample_user["username"]


def test_update_user_email(base_url, headers, sample_user):
    new_email = "updated@example.com"
    payload = {**sample_user, "email": new_email}

    response = requests.put(
        f"{base_url}/user/{sample_user['username']}", json=payload, headers=headers
    )

    assert response.status_code == 200


def test_user_login(base_url, sample_user):
    response = requests.get(
        f"{base_url}/user/login",
        params={"username": sample_user["username"], "password": sample_user["password"]},
    )

    assert response.status_code == 200
    assert "logged in" in response.json().get("message", "").lower()


def test_user_logout(base_url):
    response = requests.get(f"{base_url}/user/logout")

    assert response.status_code == 200


def test_delete_user(base_url, headers):
    username = f"user-{uuid.uuid4().hex[:10]}"
    requests.post(f"{base_url}/user", json=_build_user(username), headers=headers)

    response = requests.delete(f"{base_url}/user/{username}", headers=headers)

    assert response.status_code == 200
