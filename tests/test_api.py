import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_create_post():
    body = {
        "title": "Proyecto Final",
        "body": "Prueba API",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=body
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == body["title"]
    assert data["body"] == body["body"]


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200