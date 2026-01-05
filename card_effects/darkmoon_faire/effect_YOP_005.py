"""Effect for Barricade (YOP_005).

Card Text: Summon a 2/4 Guard with <b>Taunt</b>. If it's your only minion, summon another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOP_005t")