from django.test import TestCase

# Create your tests here.

import pytest
from core.user.models import User

# data to be passed in the user model
data_user = {
	"username": "test_name",
	"email": "test@gmail.com",
	"first_name": "Test",
	"last_name": "User",
	"password": "test_password"
}

# function to test user creation
@pytest.mark.django.db
def test_create_user():
	user = User.objects.create_user(**data_user)
	assert user.username == data_user["username"]
	assert user.email == data_user["email"]
	assert user.first_name == data_user["first_name"]
	assert user.last_name == data_user["last_name"]