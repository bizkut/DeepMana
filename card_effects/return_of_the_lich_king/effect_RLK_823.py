"""Effect for Undying Allies (RLK_823).

Card Text: After you play an Undead this turn,
give it <b>Reborn</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1