import requests
from dotenv import load_dotenv
import os
from classes.teams import Team

load_dotenv()
TOKEN = os.getenv("NBA_KEY")
TEAM = "DAL"
# The API endpoint

def getPlayersNBA(team: str):
    url = "https://api.sportsdata.io/v3/nba/scores/json/PlayersBasic/"+ team +"?key=" + TOKEN
    # A GET request to the API
    response = requests.get(url)
    # Print the response
    response_json = response.json()
    players = fomratPlayers(response_json)
    print(players)

def getTeamNBA():
    url = "https://api.sportsdata.io/v3/nba/scores/json/AllTeams?key=" + TOKEN
    # A GET request to the API
    response = requests.get(url)
    # Print the response
    response_json = response.json()
    teams = formatTeams(response_json)
    for team in teams:
        print(team)
    
def fomratPlayers(response):
    players = []

    for player in response:
        first = player["FirstName"]
        last = player["LastName"]
        players.append(first + " " + last)
    
    return players

def formatTeams(response):
    teams = []
    for team in response:
        if (team["Key"] != 'EAST' and team["Key"] != 'WEST'):
            newTeam = Team(team["Key"], team["Name"])
            teams.append(newTeam)
    return teams

