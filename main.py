import time
import csv
from datetime import datetime, timedelta
from scrape_the_news import NewsScraper

INTERVALL = 30  # time between two requests in seconds
REPETITIONS = 10  # total number of requests
DURATION = (INTERVALL * REPETITIONS) - INTERVALL
SECONDS_PASSED = 0

PAGE = "BILD"  # either "Spiegel" or "BILD" atm


def countdown():
    total_time = DURATION - SECONDS_PASSED
    time_left = timedelta(seconds=total_time)
    return time_left


bs = NewsScraper(page=PAGE)

print(f"Program started at {datetime.now()}")

while SECONDS_PASSED < DURATION:
    if SECONDS_PASSED % INTERVALL == 0:
        headline, link = bs.start()
        data = [PAGE, datetime.now(), headline, link]
        with open('headlines.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    print(f"\rLoop {SECONDS_PASSED//INTERVALL + 1} of {REPETITIONS} finished. Time until program finish: ", end="") # noqa
    print(f"{countdown()}", end="")
    SECONDS_PASSED += 1
    time.sleep(1)

print(f"Program finished at {datetime.now()}")
