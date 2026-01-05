"""Effect for Clockwork Goblin (DAL_060).

Card Text: [x]<b>Battlecry:</b> Shuffle a Bomb
into your opponent's deck.
When drawn, it explodes
for 5 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)