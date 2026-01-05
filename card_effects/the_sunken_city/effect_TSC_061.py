"""Effect for The Garden's Grace (TSC_061).

Card Text: [x]Give a minion +4/+4 and
<b>Divine Shield</b>. Costs (1) less
for each Mana you've spent
on Holy spells this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4