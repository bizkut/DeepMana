"""Effect for Forgotten Torch (LOE_002).

Card Text: Deal $3 damage. Shuffle a 'Roaring Torch' into your deck that deals 6 damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)