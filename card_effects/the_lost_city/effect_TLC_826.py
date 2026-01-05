"""Effect for Story of Carnassa (TLC_826).

Card Text: Shuffle ten 1-Cost 3/2 Raptors into your deck with "<b>Battlecry:</b> Draw a card."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)