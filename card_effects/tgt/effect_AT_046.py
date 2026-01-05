"""Effect for Tuskarr Totemic (AT_046).

Card Text: <b>Battlecry:</b> Summon a random basic Totem.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AT_046t")