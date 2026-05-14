from api.base_api import BaseAPI
class PurchaseAPI(BaseAPI):
    
    def add_purchase(self, supplier_id, product_id, quantity, cost_price, payment_date, payment_status, amount_paid, headers=None):
        endpoint ="/api/v1/business/purchase/add"
        payload ={
            "supplier_id": supplier_id,
            "product_id": product_id,
            "quantity": quantity,
            "cost_price": cost_price,
            "payment_date": payment_date,
            "payment_status": payment_status,
            "amount_paid": amount_paid
            }
        return self.post(endpoint, json=payload, headers=headers)

    def get_purchase(self, page, limit, search=None, headers=None):
        endpoint="/api/v1/business/purchase/get-all"
        params={
            "page":page,
            "limit": limit,
            "search":search
        }

        return self.get(endpoint, headers=headers, params=params)

    def get_purchase_by_id(self, purchaseId):
        endpoint = "/api/v1/business/purchase/getByID"
        params={
            "purchaseId": purchaseId
        }
        return self.get(endpoint, params=params)

    def put_purchase(self, purchaseId, payload):
        endpoint="/api/v1/business/purchase/update"
        return self.put(endpoint, json=payload)

    def delete_purchase(self, purchaseId):
        endpoint = "/api/v1/business/purchase/delete"
        params={
            "purchaseId": purchaseId
        }
        return self.delete(endpoint, params=params)
