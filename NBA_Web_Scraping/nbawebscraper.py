"""
from basketball_reference_web_scraper import client

print(client.team_box_scores(day=4, month=4, year=2024))
print()
#print(client.player_box_scores(day=5, month=4, year=2024))
"""
from enum import Enum
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

class Months(Enum):
    october = 1
    november = 2
    december = 3
    january = 4
    february = 5
    march = 6
    april = 7
    may = 8
    june = 9


box_score_urls = []
for year in range(2000, 2024):
    for month in Months:
        season_url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month.name}.html"

        month_data = requests.get(season_url)
        soup = BeautifulSoup(month_data.text, 'html.parser')

        if "429 error" in soup.title.string:
            print("Rate Limited Request: Cannot access page now")
            exit()

        schedule_table = soup.find("table", id="schedule")
        if schedule_table == None:
            continue

        links = schedule_table.find_all('a')
        links = [l.get("href") for l in links]
        links = [l for l in links if '/boxscores/' in l]

        for l in links:
            box_score_urls.append(f"https://www.basketball-reference.com{l}")

print(box_score_urls)


with open('box_score_URLs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([box_score_urls])

#print(box_score_urls)

# 2001-2024
# October-June
# Iteration through table
