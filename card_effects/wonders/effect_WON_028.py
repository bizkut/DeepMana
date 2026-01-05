"""Effect for Trial of the Jormungars (WON_028).

Card Text: Summon copies of two Beasts in your deck that cost (3) or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_028t")