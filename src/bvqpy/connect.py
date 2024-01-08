"""
Authenticate in Google and formr
"""

import requests
import csv
import gspread
import gspread
import requests
from dotenv import dotenv_values


def connect(password=dotenv_values(".env")["FORMR_PWD"]):
    """
    This function tries to log in to the formr API with the user-provided password (argument password).
    """

    email = "gonzalo.garciadecastro@upf.edu"

    try:
        r = requests.get('https://formr.org', auth=(email, password))
        if (r.status_code == 200):
            return gspread.oauth()
        else:
            print(f"Failed to connect: Error {r.status_code}")

    except ValueError:
        print("Unable to connect")
