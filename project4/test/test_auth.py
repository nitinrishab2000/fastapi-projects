from .utils import *;
from ..routers.auth import authenticate_user,get_db, create_access_token, SECRET_KEY, ALOGRITHM, get_current_user
from jose import jwt
from datetime import timedelta
import pytest
from fastapi import HTTPException

app.dependency_overrides[get_db] = override_get_db

def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    
    authenticated_user = authenticate_user(test_user.username,"testpassword",db)
    assert authenticated_user is not None
    assert authenticated_user.username == test_user.username
    
    non_existent_user = authenticate_user('WrongUserName','testpassword',db)
    assert non_existent_user is False
    
    wrong_password_user = authenticate_user(test_user.username,"wrongpass",db)
    assert wrong_password_user is False
    


def test_create_access_token():
    username = 'testuser'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)
    
    token = create_access_token(username,user_id,role,expires_delta)
    
    decoded_token = jwt.decode(token,SECRET_KEY,algorithms=[ALOGRITHM],options={'verify_signature':False})
    
    assert decoded_token['sub'] == username
    assert decoded_token['id'] == user_id
    assert decoded_token['role'] == role


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {'sub':'testuser','id':1,'role':'admin'}
    token = jwt.encode(encode,SECRET_KEY,algorithm=ALOGRITHM)
    
    user = await get_current_user(token=token)
    assert user == {'username':'testuser','user_id':1,'user_role':'admin'}
    
@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role':'user'}
    token = jwt.encode(encode,SECRET_KEY,algorithm=ALOGRITHM)
    
    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)
    
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail== 'Could not validate user.'



