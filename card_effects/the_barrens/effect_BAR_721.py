"""Effect for Mankrik (BAR_721).

Card Text: [x]<b>Battlecry:</b> Help Mankrik find
his wife! She was last seen
somewhere in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass