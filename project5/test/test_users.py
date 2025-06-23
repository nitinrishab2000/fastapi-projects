from .utils import *
from ..routers.users import get_current_user , get_db
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users/get_user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'codingwithnitin'
    assert response.json()['email'] == 'codingwithnitin@email.com'
    assert response.json()['first_name'] == 'Nitin'
    assert response.json()['last_name'] == 'Kumar'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '111111'
    
def test_change_password_success(test_user):
    response = client.put("/users/password",json={"password":"testpassword","new_password":"newpassword"})
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
def test_change_password_invalid_current_password(test_user):
    response = client.put("/users/password",json={"password":"testpassword1","new_password":"newpassword"})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password change'}
    
def test_change_phone_number_success(test_user):
    response = client.put("/users/phone_number/222222")
    
    assert response.status_code == status.HTTP_204_NO_CONTENT