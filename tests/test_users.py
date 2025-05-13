def test_post_user_success(client):
    payload = {
        "email": "teste70@teste.com",
        "password": "1234",
        "name": "Teste",
        "document_number": "12345678925"
    }

    response = client.post("/user/register", json=payload)

    assert response.status_code == 200
    assert "message" in response.json()


def test_create_user_already_registered(client):
    payload = {
        "email": "teste@teste.com",
        "password": "1234",
        "name": "Teste",
        "document_number": "12345678910"
    }

    response = client.post("/user/register", json=payload)

    assert response.status_code == 400
    assert "detail" in response.json()
    assert "User email already registered" in response.json()[
        "detail"
    ]


def test_user_login_success(client):
    payload = {
        "username": "teste@teste.com",
        "password": "1234",
    }

    response = client.post("/user/login", data=payload)

    assert response.status_code == 200
    assert "access_token" in response.json()
