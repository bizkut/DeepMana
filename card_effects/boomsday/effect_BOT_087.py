"""Effect for Academic Espionage (BOT_087).

Card Text: Shuffle 10 cards from your opponent's class into your deck. They cost (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass