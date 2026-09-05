import pytest
USER={"name":"QA","email":"qa@example.com","age":30,"password":"password123"}
@pytest.mark.parametrize("age,expected",[(17,422),(18,201),(100,201),(101,422)])
def test_age_boundaries(client,age,expected): assert client.post("/users",json={**USER,"age":age}).status_code==expected
def test_blank_user_name(client): assert client.post("/users",json={**USER,"name":"   "}).status_code==422
def test_blank_product_name(client): assert client.post("/products",json={"name":"  ","price":1,"stock":0}).status_code==422
def test_json_content_type(client): assert client.get("/users").headers["content-type"].startswith("application/json")
def test_malformed_json(client): assert client.post("/users",content="{",headers={"content-type":"application/json"}).status_code==422
