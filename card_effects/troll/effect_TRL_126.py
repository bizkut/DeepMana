"""Effect for Captain Hooktusk (TRL_126).

Card Text: <b>Battlecry:</b> Summon 3 Pirates from your deck. Give them <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_126t")