def test_login(client,user):
    r=client.post("/login",json={"email":"qa@example.com","password":"password123"}); assert r.status_code==200 and r.json()["access_token"]=="test-token"
def test_wrong_password(client,user): assert client.post("/login",json={"email":"qa@example.com","password":"wrongpass"}).status_code==401
def test_unknown_email(client): assert client.post("/login",json={"email":"none@example.com","password":"password123"}).status_code==401
def test_missing_email(client): assert client.post("/login",json={"password":"password123"}).status_code==422
def test_missing_password(client): assert client.post("/login",json={"email":"qa@example.com"}).status_code==422
