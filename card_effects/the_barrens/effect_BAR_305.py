"""Effect for Flurry (Rank 1) (BAR_305).

Card Text: <b>Freeze</b> a random enemy minion. <i>(Upgrades when you have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True