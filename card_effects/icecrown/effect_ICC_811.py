"""Effect for Lilian Voss (ICC_811).

Card Text: <b>Battlecry:</b> Replace spells in your hand with random spells <i>(from your opponent's class).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass