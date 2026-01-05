"""Effect for Ancient Raptor (TLC_245).

Card Text: [x]<b>Battlecry:</b> Choose to gain
+3 Attack, <b>Divine Shield</b>,
or "<b>Deathrattle:</b> Summon
two 1/1 Plants."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_245t")


def deathrattle(game, source):
    pass