from . import rps


def main() -> None:
    game = rps.RpsGame()
    game.play_forever()
