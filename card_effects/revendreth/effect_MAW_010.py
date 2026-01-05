"""Effect for Motion Denied (MAW_010).

Card Text: [x]<b>Secret:</b> After your
opponent plays three cards
in a turn, deal $6 damage
to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)