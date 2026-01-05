"""Effect for Taintheart Tormenter (WC_040).

Card Text: <b>Taunt</b>
Your opponent's spells cost (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass