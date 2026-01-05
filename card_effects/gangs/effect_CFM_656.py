"""Effect for Streetwise Investigator (CFM_656).

Card Text: <b>Battlecry:</b> Enemy minions lose <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass