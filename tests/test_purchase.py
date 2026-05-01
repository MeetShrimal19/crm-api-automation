import random
from utils.logger import get_logger

logger = get_logger()


def test_post_purchase(auth_api, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    # Get suppliers
    res = auth_api.get_supplier(page=1, limit=5, headers=headers)
    assert res.status_code == 200

    data = res.json()
    supplier_list = data["results"]["data"]

    supplier = random.choice(supplier_list)
    supplier_id = supplier["supplier_id"]

    logger.info(f"Selected Supplier ID: {supplier_id}")

    # Dynamic data
    quantity = random.randint(1, 500)
    cost_price = random.randint(100, 1000)
    amount_paid = quantity * cost_price

    logger.info(f"Creating purchase → qty={quantity}, price={cost_price}, amount={amount_paid}")

    # Create purchase
    response = auth_api.add_purchase(
        supplier_id=supplier_id,
        product_id=1,
        quantity=quantity,
        cost_price=cost_price,
        payment_date="2026-01-15",
        payment_status="paid",
        amount_paid=amount_paid,
        headers=headers
    )

    logger.info(f"Purchase Response: {response.text}")

    assert response.status_code == 201

    data = response.json()
    assert data["success"] is True
    assert data["code"] == 201
    assert data["message"] == "Purchase added successfully"


def test_get_purchase(auth_api, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    logger.info("Fetching purchase list")

    response = auth_api.get_purchase(page=1, limit=5, headers=headers)
    logger.info(f"GET Purchase Response: {response.text}")

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "Purchase retrieved successfully"

    purchase_list = data["results"]["data"]

    logger.info(f"Total purchases fetched: {len(purchase_list)}")

    assert isinstance(purchase_list, list)
    assert len(purchase_list) <= 5