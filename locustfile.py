import random
from datetime import datetime
from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task(1)
    def normal_post(self):
        temp = random.randint(12, 20)
        collected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post("/", {
            "temp": temp,
            "collected_at": collected_at
        })

    @task(1)
    def celery_post(self):
        temp = random.randint(12, 20)
        collected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post("/celery_post/", {
            "temp": temp,
            "collected_at": collected_at
        })


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://localhost:8000/api/v1/sensors/temperature"
