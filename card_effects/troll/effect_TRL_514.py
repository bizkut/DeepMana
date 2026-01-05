"""Effect for Belligerent Gnome (TRL_514).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If your opponent
has 2 or more minions,
gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2