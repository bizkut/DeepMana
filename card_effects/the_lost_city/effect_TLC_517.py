"""Effect for Knockback (TLC_517).

Card Text: [x]Deal $1 damage to
a minion <i>(improved for
each time you've shuffled
cards into your deck)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)