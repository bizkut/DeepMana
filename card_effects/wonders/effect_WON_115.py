"""Effect for Blast from the Past (WON_115).

Card Text: Get 2 <b>Spare Parts</b>. Summon two 1/1 Boom Bots. Shuffle a Bomb into your opponent's deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_115t")