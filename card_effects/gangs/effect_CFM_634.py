"""Effect for Lotus Assassin (CFM_634).

Card Text: <b>Stealth</b>. Whenever this attacks and kills a minion, gain <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass