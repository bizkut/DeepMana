"""Effect for Dispose of Evidence (REV_507).

Card Text: Give your hero +3 Attack this turn. Choose a card in your hand to shuffle into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3