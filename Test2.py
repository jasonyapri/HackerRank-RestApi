#!/bin/python3

import math
import os
import random
import re
import sys


import requests
import json
#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#

def getWinnerTotalGoals(competition, year):
    res0 = requests.get("https://jsonmock.hackerrank.com/api/football_competitions?name="+competition+"&year="+str(year)).json()
    return getTotalGoals(competition, res0['data'][0]['winner'], year)

def getTotalGoals(competition, team, year):
    total_goals = 0
    
    res1 = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team1="+team).json()
    for i in range(res1['total_pages']):
        res_home = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team1="+team + "&page="+str(i+1)).json()
        count = res_home['per_page']
        if((i+1) == res_home['total_pages']):
            count = res_home['total']%res_home['per_page']
        for j in range(count):
            total_goals += int(res_home['data'][j]['team1goals'])
    
            
    res2 = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team2="+team).json()
    for i in range(res2['total_pages']):
        res_away = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition="+competition+"&year="+str(year)+"&team2="+team + "&page="+str(i+1)).json()
        count = res_away['per_page']
        if((i+1) == res_away['total_pages']):
            count = res_away['total']%res_away['per_page']
        for j in range(count):
            total_goals += int(res_away['data'][j]['team2goals'])

    return total_goals    

if __name__ == '__main__':
    print(getWinnerTotalGoals('UEFA Champions League', 2011))