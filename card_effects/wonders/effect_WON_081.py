"""Effect for Tuskarr Totemic (WON_081).

Card Text: <b>Battlecry:</b> Summon a random basic Totem.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_081t")