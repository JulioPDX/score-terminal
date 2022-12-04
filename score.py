"""Simple example to display game scores"""
import os
import argparse

from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer

import requests
from dotenv import load_dotenv
from emoji import teams

load_dotenv()

TOKEN = os.getenv("TOKEN")

parser = argparse.ArgumentParser()
parser.add_argument(
    "--week", action="store", type=int, choices=range(1, 18)
)
parser.add_argument(
    "--season",
    action="store",
    type=str,
    required=False,
    default="2022REG",
    help="Example: 2022PRE, 2022REG, 2022POST",
)
parser.add_argument("--emoji", action="store_true")
parser.add_argument("--no-emoji", dest="feature", action="store_false")
parser.set_defaults(feature=False)

args = parser.parse_args()

WEEK = args.week
SEASON = args.season
EMOJI = args.emoji

if not args.week:
    seas_response = requests.get(f"https://api.sportsdata.io/v3/nfl/scores/json/CurrentWeek?key={TOKEN}")
    WEEK = seas_response.text
else:
    WEEK = args.week


def game_info(game):
    """Simple function to return game information"""
    if EMOJI:
        game_text = f"""
        {teams[game['AwayTeam']]} vs {teams[game['HomeTeam']]}
        {game['AwayScore']} - {game['HomeScore']}
        Quarter: {game['Quarter']}
        Time: {game['TimeRemaining']}

        Channel: {game['Channel']}
        [green]Is over: {game['IsOver']}[/green]
        """
    else:
        game_text = f"""
        {game['AwayTeam']} vs {game['HomeTeam']}
        {game['AwayScore']} - {game['HomeScore']}
        Quarter: {game['Quarter']}
        Time: {game['TimeRemaining']}

        Channel: {game['Channel']}
        [green]Is over: {game['IsOver']}[/green]
        """
    return game_text


class GameApp(App):
    """Do all the things"""

    CSS_PATH = "score.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "toggle_quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        response = requests.get(
            f"https://api.sportsdata.io/v3/nfl/scores/json/ScoresByWeek/{SEASON}/{WEEK}?key={TOKEN}",
            timeout=10,
        )
        games = response.json()
        for game in games:
            yield Static(game_info(game), classes="box")

    def action_toggle_quit(self) -> None:
        """Closes app"""
        self.exit()


if __name__ == "__main__":
    app = GameApp()
    app.run()
