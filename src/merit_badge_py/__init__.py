from . import rps


def main() -> None:
    game = rps.Game()
    game.play_forever()
