"""Effect for Conviction (Rank 1) (BAR_880).

Card Text: [x]Give a random friendly
minion +3 Attack.
<i>(Upgrades when you
have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3