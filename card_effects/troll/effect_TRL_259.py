"""Effect for Princess Talanji (TRL_259).

Card Text: <b>Battlecry:</b> Summon all minions from your hand that didn't start in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_259t")