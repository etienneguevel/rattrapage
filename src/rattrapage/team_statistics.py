# This script aims to illustrate how to show statistics for the teams
# The value showed will be premade, it is up to you to get the same results
import os
import pandas as pd
from rattrapage import PROJECT_DIR

def get_franchises():
    dfTeams = pd.read_csv(
        PROJECT_DIR / "data" / "TeamStatistics.csv"
    )
    return list(dfTeams.teamName.unique())
    

def main():
    teams = get_franchises()
    while True:
        team = input("Select a franchise (example: Nuggets): ")
        if team in teams:
            break
        print("Please select a valid franchise")
    
    while True:
        season = input("Select a season (example: 2022): ")
        try:
            season = int(season)
            break
        
        except ValueError:
            print("Please input a number")
            continue
    
    with open(os.path.join(
        os.path.dirname(__file__), "denver_example.txt"
    ), "r") as f:
        txt = f.read()
    
    print(txt)

if __name__ == "__main__":
    main()