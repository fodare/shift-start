import os
import time

app_list = {r"c:\path to app 1",
            r"c:\path to app 2",
            r"c:\path to app 3",
            r"c:\path to app 4",
            r"c:\path to app 5",
            r"c:\path to app 6",
            r"c:\path to app 7"}


def Open_Apps(apps_list):
    for app in apps_list:
        print(f"Opening app {app}")
        os.startfile(app)
        print("Sleeping for 4 seconds")
        time.sleep(4)


Open_Apps(apps_list=app_list)
