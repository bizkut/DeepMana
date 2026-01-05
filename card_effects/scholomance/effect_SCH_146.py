"""Effect for Robes of Protection (SCH_146).

Card Text: Your minions have <b>Elusive</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass