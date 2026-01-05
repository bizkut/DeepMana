"""Effect for Fleshshaper (NX2_027).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> If you have 5 or more Armor, summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_027t")