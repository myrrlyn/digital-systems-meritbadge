"Implements the game Rock/Paper/Scissors"

from typing import Self
from enum import StrEnum
import random

from .utils import GameResult


class Move(StrEnum):
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
            (self == Move.ROCK and other == Move.SCISSORS)
            or (self == Move.PAPER and other == Move.ROCK)
            or (self == Move.SCISSORS and other == Move.PAPER)
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
            return Move.ROCK
        elif text == "paper":
            return Move.PAPER
        elif text == "scissors":
            return Move.SCISSORS
        else:
            raise ValueError("moves are only rock, paper, or scissors")

    @staticmethod
    def get_random():
        return random.choice([Move.ROCK, Move.PAPER, Move.SCISSORS])


class Game:
    def __init__(self):
        pass

    def play_once(self) -> GameResult:
        inp = input("Enter your move here: ")
        inp = inp.strip().lower()
        if inp in ["quit", "q"]:
            raise StopIteration
        try:
            play = Move.parse(inp)
        except ValueError as exc:
            print(f"couldn't understand `{inp}` as an RPS move. Try again?")
            raise exc

        roboplay = Move.get_random()
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
