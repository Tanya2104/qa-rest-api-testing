BASE={"name":"QA User","email":"qa@example.com","age":30,"password":"password123"}

def test_create_user(client):
    r=client.post("/users",json=BASE); assert r.status_code==201 and r.json()["id"]==1 and "password" not in r.json()
def test_get_user(client,user): assert client.get(f"/users/{user['id']}").json()["email"]==user["email"]
def test_list_users(client,user): assert len(client.get("/users").json())==1
def test_update_user(client,user):
    data={**BASE,"name":"Updated","email":"new@example.com"}; r=client.put(f"/users/{user['id']}",json=data); assert r.status_code==200 and r.json()["name"]=="Updated"
def test_delete_user(client,user):
    assert client.delete(f"/users/{user['id']}").status_code==204; assert client.get(f"/users/{user['id']}").status_code==404
def test_duplicate_email(client,user): assert client.post("/users",json=BASE).status_code==409
def test_invalid_email(client): assert client.post("/users",json={**BASE,"email":"bad"}).status_code==422
def test_short_password(client): assert client.post("/users",json={**BASE,"password":"short"}).status_code==422
def test_nonexistent_user(client): assert client.get("/users/999").status_code==404
def test_duplicate_email_update(client,user):
    b=client.post("/users",json={**BASE,"email":"two@example.com"}).json(); assert client.put(f"/users/{b['id']}",json=BASE).status_code==409
