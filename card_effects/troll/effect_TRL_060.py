"""Effect for Spirit of the Frog (TRL_060).

Card Text: [x]<b>Stealth</b> for 1 turn.
Whenever you cast a spell,
draw a spell from your deck
that costs (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)