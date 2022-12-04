# Score terminal

Proof of concept to show scores in the terminal window using Textual.

## Getting started

If you want to mess with the code or build on this:

> Head to https://sportsdata.io/ and create a free developer account (for token)

```shell
git clone
cd score-terminal
python3 -m venv venv
source venv/bin/activate
```

Create a `.env` file with your new token.

View current weeks games with no emojis as team names:

```shell
python3 score.py
```

View current weeks games with emojis as team names:

```shell
python3 score.py --emoji
```

View specific week of games with emojis as team names:

```shell
python3 score.py --week 8 --emoji
```

View specific preseason week with emojis as team names:

```shell
python3 score.py --season 2022PRE --week 1 --emoji
```

## To do

I need to figure out how to refresh all the `Static` content that is displayed on an interval. At the moment the information stays at the current score without rerunning the program.
