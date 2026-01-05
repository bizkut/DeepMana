"""Effect for Bloodfury Potion (CFM_611).

Card Text: [x]Give a minion +3 Attack.
If it's a Demon, also
give it +3 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)