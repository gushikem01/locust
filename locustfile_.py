from locust import HttpUser, task, between
import random

class User(HttpUser):
    wait_time = between(1, 1)
    @task
    def limit(self):
        self.client.get("/aiakos1/reserve/limit")
