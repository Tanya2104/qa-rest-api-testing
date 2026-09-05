BASE={"name":"Keyboard","price":25.5,"stock":10}
def test_create_product(client):
    r=client.post("/products",json=BASE); assert r.status_code==201 and r.json()["price"]==25.5
def test_get_product(client,product): assert client.get(f"/products/{product['id']}").status_code==200
def test_list_products(client,product): assert len(client.get("/products").json())==1
def test_update_product(client,product):
    r=client.put(f"/products/{product['id']}",json={**BASE,"stock":20}); assert r.status_code==200 and r.json()["stock"]==20
def test_delete_product(client,product): assert client.delete(f"/products/{product['id']}").status_code==204
def test_zero_price(client): assert client.post("/products",json={**BASE,"price":0}).status_code==422
def test_negative_price(client): assert client.post("/products",json={**BASE,"price":-1}).status_code==422
def test_zero_stock(client): assert client.post("/products",json={**BASE,"stock":0}).status_code==201
def test_negative_stock(client): assert client.post("/products",json={**BASE,"stock":-1}).status_code==422
def test_nonexistent_product(client): assert client.get("/products/999").status_code==404
