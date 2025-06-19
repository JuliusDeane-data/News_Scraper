import time
import datetime


class TimeKeeper:
    def __init__(self, duration: dict, intervall: dict):
        self.total_time = datetime.timedelta(**duration).total_seconds()
        self.intervall = datetime.timedelta(**intervall).total_seconds()
        self.seconds_passed = 0

    def timeleft(self):
        return datetime.timedelta(
            seconds=(
                self.total_time - self.seconds_passed
            )
        ).total_seconds()

    def countdown(self):
        while self.seconds_passed < self.total_time:
            time.sleep(1)
            self.seconds_passed += 1
            self.timeleft()


duration = {"days": 0, "hours": 0, "seconds": 3}
intervall = {"days": 0, "hours": 0, "seconds": 1}

print(datetime.timedelta(**duration).total_seconds())

tk = TimeKeeper(duration, intervall)

print(tk.countdown())