import requests
from bs4 import BeautifulSoup
import csv


date = input("please enter a date in the following format MM/DD/YYYY: ")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

