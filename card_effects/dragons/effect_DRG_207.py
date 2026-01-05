"""Effect for Abyssal Summoner (DRG_207).

Card Text: [x]<b>Battlecry:</b> Summon a
Demon with <b>Taunt</b> and stats
equal to your hand size.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_207t")