"""Effect for Barnes (KAR_114).

Card Text: <b>Battlecry:</b> Summon a 1/1 copy of a random minion in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_114t")