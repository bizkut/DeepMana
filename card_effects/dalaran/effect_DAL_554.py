"""Effect for Chef Nomi (DAL_554).

Card Text: <b>Battlecry:</b> If your deck is empty, summon six 6/6 Greasefire Elementals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_554t")