"""Effect for Mythical Runebear (EDR_481).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> If this has 4 or more Attack, summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_481t")