from locust import HttpUser, task, between
import random

users = [
  [50001, 11, 11],
  [50002, 11, 11],
  [50003, 11, 11],
  [50004, 11, 11],
  [50005, 11, 11],
  [50006, 11, 11],
  [50007, 11, 11],
  [50008, 11, 11],
  [50009, 11, 11],
  [50010, 11, 11],
  [50011, 11, 11],
  [50012, 11, 11],
  [50013, 11, 11],
  [50014, 11, 11],
  [50015, 11, 11],
  [50016, 11, 11],
  [50017, 11, 11],
  [50018, 11, 11],
  [50019, 11, 11],
  [50020, 11, 11],
]

class User(HttpUser):
    wait_time = between(1, 1)

    def on_start(self):
        user = self.get_user()
        self.client.post("/aiakos1/yoyaku/menu.cgi", json={"recno":user[0], "birthmonth":user[1], "birthday": user[2]})

    def get_user(self):
        user = random.choice(users)
        return user

    @task
    def menu(self):
        self.client.get("/aiakos1/yoyaku/usermenu.cgi")

    # @task
    # def limit(self):
    #     self.client.get("/aiakos1/yoyaku/limit.cgi")

# from locust import HttpUser, TaskSet, task, between, constant

# class UserBehavior(TaskSet):

#     @task(1)
#     def search(self):
#         self.client.get("https://test4.inet489.jp/aiakos1/reserve/limit", verify=False)

# class WebsiteUser(HttpUser):

#     tasks = {UserBehavior:1}
#     wait_time = constant(0)
