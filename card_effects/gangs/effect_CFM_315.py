"""Effect for Alleycat (CFM_315).

Card Text: <b>Battlecry:</b> Summon a 1/1 Cat.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_315t")