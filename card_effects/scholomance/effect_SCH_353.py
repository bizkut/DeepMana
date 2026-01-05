"""Effect for Cram Session (SCH_353).

Card Text: Draw $1 cards <i>(improved by <b>Spell Damage</b>)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)