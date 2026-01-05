"""Effect for Former Champ (TRL_151).

Card Text: <b>Battlecry:</b> Summon a 5/5 Hotshot.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_151t")