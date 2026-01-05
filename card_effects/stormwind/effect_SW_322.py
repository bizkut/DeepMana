"""Effect for Defend the Dwarven District (SW_322).

Card Text: <b>Questline:</b> Deal damage with 3 spells. <b>Reward:</b> Your Hero Power can target minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)