"""Effect for Fortify (TLC_620).

Card Text: [x]Gain 3 Armor.
Deal damage equal
to your Armor to an
enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)