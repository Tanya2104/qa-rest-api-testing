def create(client,user,product,q=2): return client.post("/orders",json={"user_id":user["id"],"product_id":product["id"],"quantity":q})
def test_successful_order(client,user,product): assert create(client,user,product).status_code==201
def test_order_defaults(client,user,product): assert create(client,user,product).json()["status"]=="created"
def test_correct_total(client,user,product): assert create(client,user,product,3).json()["total_price"]==76.5
def test_stock_reduction(client,user,product):
    create(client,user,product,3); assert client.get(f"/products/{product['id']}").json()["stock"]==7
def test_quantity_zero(client,user,product): assert create(client,user,product,0).status_code==422
def test_quantity_negative(client,user,product): assert create(client,user,product,-1).status_code==422
def test_quantity_over_stock(client,user,product): assert create(client,user,product,11).status_code==400
def test_nonexistent_order_user(client,product):
    assert client.post("/orders",json={"user_id":999,"product_id":product["id"],"quantity":1}).status_code==404
def test_nonexistent_order_product(client,user):
    assert client.post("/orders",json={"user_id":user["id"],"product_id":999,"quantity":1}).status_code==404
def test_get_and_delete_order(client,user,product):
    order=create(client,user,product).json(); assert client.get(f"/orders/{order['id']}").status_code==200; assert client.delete(f"/orders/{order['id']}").status_code==204
def test_nonexistent_order(client): assert client.get("/orders/999").status_code==404
