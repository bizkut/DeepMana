"""Effect for Warsong Commander (CORE_EX1_084).

Card Text: Whenever you summon a minion with 3 or less Attack, give it <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_EX1_084t")