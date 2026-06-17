def test_get_activities_returns_all_activities(client):
    """Arrange: none (initial state)
    Act: GET /activities
    Assert: response contains expected activities and fields
    """
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Basic sanity checks
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "description" in data["Chess Club"]
    assert "participants" in data["Chess Club"]


def test_root_redirects_to_static_index(client):
    """Arrange: none
    Act: GET /
    Assert: redirect (307) to /static/index.html
    """
    response = client.get("/", follow_redirects=False)
    assert response.status_code in (301, 302, 307)
    assert response.headers.get("location") == "/static/index.html"
