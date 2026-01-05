"""Effect for Greater Healing Potion (CFM_604).

Card Text: Restore #12 Health to a friendly character. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(12)