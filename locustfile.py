from locust import HttpUser, task, between
import random

class ShopScaleUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def get_products(self):
        self.client.get("/api/products")

    @task(3)
    def home_page(self):
        self.client.get("/")

    @task(2)
    def search_products(self):
        queries = [
            "keyboard",
            "coffee",
            "fitness",
            "clothing",
            "electronics"
        ]

        query = random.choice(queries)

        self.client.get(
            "/api/search",
            params={"q": query}
        )

    @task(1)
    def add_to_cart(self):
        product_id = random.randint(1, 24)

        self.client.post(
            "/api/cart",
            json={
                "product_id": product_id,
                "quantity": 1
            }
        )
