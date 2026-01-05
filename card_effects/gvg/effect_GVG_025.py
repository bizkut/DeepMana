"""Effect for One-eyed Cheat (GVG_025).

Card Text: Whenever you summon a Pirate, gain <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_025t")