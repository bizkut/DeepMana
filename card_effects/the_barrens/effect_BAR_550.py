"""Effect for Galloping Savior (BAR_550).

Card Text: [x]<b>Secret:</b> After your
opponent plays three
cards in a turn, summon a
3/4 Steed with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_550t")