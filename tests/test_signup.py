def test_signup_for_activity_success(client):
    """Arrange: activity and email
    Act: POST signup
    Assert: 200 and participant added
    """
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]

    # Verify participant present in activities
    activities_response = client.get("/activities")
    assert email in activities_response.json()[activity_name]["participants"]


def test_signup_for_nonexistent_activity(client):
    # Arrange
    activity_name = "No Such Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_for_activity_already_signed_up(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # already in seed

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]
