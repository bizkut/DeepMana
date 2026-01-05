"""Effect for Germination (BT_129).

Card Text: Summon a copy of a friendly minion.
Give the copy <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_129t")