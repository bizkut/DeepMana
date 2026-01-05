"""Effect for Ice Lance (CS2_031).

Card Text: <b>Freeze</b> a character. If it was already <b>Frozen</b>, deal $4 damage instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)