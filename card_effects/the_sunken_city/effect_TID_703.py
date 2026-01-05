"""Effect for Topple the Idol (TID_703).

Card Text: [x]<b>Dredge</b>. Reveal it and
deal damage equal to
 its Cost to all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)