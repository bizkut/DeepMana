"""Effect for Muster for Battle (GVG_061).

Card Text: Summon three 1/1 Silver Hand Recruits. Equip a 1/4 Weapon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_061t")