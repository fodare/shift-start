import os
import time

app_list = {}


def Open_Apps(apps_list):
    for app in apps_list:
        print(f"Opening app {app}")
        os.startfile(app)
        print("Sleeping for 4 seconds")
        time.sleep(4)


Open_Apps(apps_list=app_list)
