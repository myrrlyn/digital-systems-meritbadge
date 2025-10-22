"Implements the game Rock/Paper/Scissors"

from typing import Self
from enum import StrEnum, Enum
import random


class GameResult(Enum):
    WIN = 1
    TIE = 0
    LOSS = -1


class RpsMove(StrEnum):
    "Describes a single move of Rock/Paper/Scissors"

    ROCK = "🪨"
    PAPER = "📄"
    SCISSORS = "✂️"

    # LIZARD = "🦎"
    # SPOCK = "🖖"

    def execute(self, other: Self) -> GameResult:
        "decides if self beats the other move"
        if self == other:
            return GameResult.TIE
        elif (
            (self == RpsMove.ROCK and other == RpsMove.SCISSORS)
            or (self == RpsMove.PAPER and other == RpsMove.ROCK)
            or (self == RpsMove.SCISSORS and other == RpsMove.PAPER)
        ):
            return GameResult.WIN
        else:
            return GameResult.LOSS

    def __str__(self):
        return self.value

    @staticmethod
    def parse(text: str):
        """Parses some text as a move. Raises `ValueError` if the input is not a recognized move name"""
        text = text.strip().lower()
        if text == "rock":
            return RpsMove.ROCK
        elif text == "paper":
            return RpsMove.PAPER
        elif text == "scissors":
            return RpsMove.SCISSORS
        else:
            raise ValueError("moves are only rock, paper, or scissors")

    @staticmethod
    def get_random():
        return random.choice([RpsMove.ROCK, RpsMove.PAPER, RpsMove.SCISSORS])


class RpsGame:
    def __init__(self):
        pass

    def play_once(self) -> GameResult:
        inp = input("Enter your move here: ")
        inp = inp.strip().lower()
        if inp in ["quit", "q"]:
            raise StopIteration
        try:
            play = RpsMove.parse(inp)
        except ValueError as exc:
            print(f"couldn't understand `{inp}` as an RPS move. Try again?")
            raise exc

        roboplay = RpsMove.get_random()
        outcome = play.execute(roboplay)
        if outcome == GameResult.WIN:
            print(f"Your {play}  beat my {roboplay}  !")
        elif outcome == GameResult.LOSS:
            print(f"Your {play}  was no match for my {roboplay}  ")
        else:
            print(f"We both played {play}")

        return outcome

    def play_forever(self):
        print("The game continues until you [q]uit")
        your_score = 0
        robo_score = 0

        while True:
            try:
                outcome = self.play_once()
            except StopIteration:
                break
            except ValueError:
                continue
            if outcome == GameResult.WIN:
                your_score += 1
            elif outcome == GameResult.LOSS:
                robo_score += 1
            person = ["😡", "😀"][your_score > robo_score]
            print(f"{person} : {your_score}; 💻 : {robo_score}")
