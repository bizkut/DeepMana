"""Effect for Serrated Bone Spike (REV_939).

Card Text: [x]Deal $3 damage to a 
minion. If it dies, your 
next card this turn 
costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)