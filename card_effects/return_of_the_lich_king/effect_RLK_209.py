"""Effect for Unleash Fel (RLK_209).

Card Text: Deal $1 damage
to all enemies. <b>Manathirst (6):</b> With
<b>Lifesteal</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)