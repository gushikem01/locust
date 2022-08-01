from locust import HttpUser, task, between
import random
class User(HttpUser):
    wait_time = between(1, 1)
    @task(1)
    def index(self):
        x = random.randint(50001, 50135)
        self.client.cookies.clear()
        # TEST CASE 1
        # self.client.get("/aiakos10/app-psgi/reserve/50001")
        # TEST CASE 2
        self.client.get("/aiakos4/app-psgi/sessionlimit/CGISESSID=4a88df9bca60e95fa02cab7fcc2262ae")
        # TEST CASE 3
        # self.client.get("/aiakos4/yoyaku/login.cgi?recno=%d" % x)
