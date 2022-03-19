import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get("https://amir-flaskpipelines.azurewebsites.net")
            time.sleep(1)

    def on_start(self):
        self.client.post("https://amir-flaskpipelines.azurewebsites.net")
