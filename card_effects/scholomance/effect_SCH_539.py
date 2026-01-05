"""Effect for Professor Slate (SCH_539).

Card Text: Your spells are <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass