"""Effect for Seal of Blood (RLK_922).

Card Text: Give a minion +3/+3 and <b>Divine Shield</b>. Deal $3 damage to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)