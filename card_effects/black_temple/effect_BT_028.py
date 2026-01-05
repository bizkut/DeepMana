"""Effect for Astromancer Solarian (BT_028).

Card Text: [x]<b>Spell Damage +1</b>
<b>Deathrattle:</b> Shuffle
'Solarian Prime'
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1