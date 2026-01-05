"""Effect for Darkmoon Rabbit (DMF_070).

Card Text: <b>Rush</b>, <b>Poisonous</b>
Also damages the minions next to whomever this attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass