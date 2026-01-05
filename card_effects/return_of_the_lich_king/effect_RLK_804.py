"""Effect for Conjured Arrow (RLK_804).

Card Text: Deal $2 damage
to a minion.
<b>Manathirst (6):</b> Draw
that many cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)