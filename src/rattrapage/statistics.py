# This script aims to illustrate how to show statistics for the scorers
# It is up to you to do the same for others statistical categories

from argparse import ArgumentParser
from warnings import filterwarnings
import pandas as pd
from rattrapage import PROJECT_DIR


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--num_players",
        type=int,
        default=15,
    )

    parser.add_argument(
        "--type",
        type=str,
        default="mean",
        choices=["mean", "std", "sum"],        
    )

    parser.add_argument(
        "--games",
        type=str,
        required=False,
        choices=["Playoffs", "Regular Season"]
    )

    return parser.parse_args()

def findScorers(playersStatistics: pd.DataFrame, games=None) -> pd.DataFrame:
    Names = playersStatistics[["personId", "fullName"]].drop_duplicates("personId")
    if games is not None:
        playersStatistics = playersStatistics[
            playersStatistics["gameType"] == games
        ]
    
    return (
        playersStatistics
         .groupby("personId")
         ["points"]
         .agg(["sum", "mean", "std"])
         .merge(Names, on="personId")
    )

def main():
    # Ignore warnings
    filterwarnings("ignore")

    # Get the arguments
    args = parse_args()

    # Read the data file
    playersStatistics = pd.read_csv(
        PROJECT_DIR / "data" / "PlayerStatistics.csv"
    )

    # Find the best scorers
    scorers = findScorers(playersStatistics, args.games)
    print(f"Ranking of the {args.num_players} best scorers by {args.type}:\n")
    print("-" * 65)
    print(
        scorers.sort_values(args.type, ascending=False).iloc[0:args.num_players]
    )

if __name__ == "__main__":
    main()