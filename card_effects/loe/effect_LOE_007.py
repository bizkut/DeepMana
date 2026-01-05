"""Effect for Curse of Rafaam (LOE_007).

Card Text: Give your opponent a 'Cursed!' card.
While they hold it, they take 2 damage on their turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2