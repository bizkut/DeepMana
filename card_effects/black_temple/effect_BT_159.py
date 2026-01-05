"""Effect for Terrorguard Escapee (BT_159).

Card Text: <b>Battlecry:</b> Summon three 1/1 Huntresses for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_159t")