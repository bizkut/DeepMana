"""Effect for Void Drinker (SCH_343).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> Destroy
a Soul Fragment in your
deck to gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()