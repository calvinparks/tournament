# Simulate a sports tournament

import csv
import sys
import random
from operator import itemgetter


# Number of simluations to run
N = 1

test_name = "Colombia"


def main():
   
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")
    
    # number of teams in tournament
    
    teams = [] 
    #####teams_counter = 0
    
    # TODO: Read teams into memory from file
    # store inside teams = [] list
    # with open(filename) as file:
    #  reader = csv.DictReader(file)
    #  In Python, to append to the end of a list, use the .append()
    # after reading in you will have to convert the rating to an integer
    
    if len(sys.argv) != 2:
        print("missing command-line argument")
        sys.exit(1)
   
    with open(sys.argv[1], "r") as file:
        for line in file:
            team = {}  # dictionary for a team
            data = line.split(",")

            key = data[0].replace('\r', '').replace('\n', '')
            value = data[1].replace('\r', '').replace('\n', '')
            if value.isnumeric():
                team["name"] = data[0]
                team["rating"] = int(value)
                teams.append(team)
                #teams_counter += 1
               
    counts = {} 
    # initialize the counts dictionary with for all teams
    for index in range(len(teams)):
        for key in teams[index]:
            counts[teams[index]["name"]] = 0
            
    for x in range(N):
        winning_team = simulate_tournament(teams)
        counts[winning_team] += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while len(teams) > 1:       
        teams = simulate_round(teams)
 
    winning_values_dict = teams[0].values()
    winning_values_list = list(winning_values_dict)
    return winning_values_list[0]

    
if __name__ == "__main__":
    main()
