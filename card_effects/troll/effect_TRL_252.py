"""Effect for High Priestess Jeklik (TRL_252).

Card Text: [x]<b>Taunt</b>, <b>Lifesteal</b>
When you discard this,
add 2 copies of it to
your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass