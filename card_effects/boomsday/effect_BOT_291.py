"""Effect for Storm Chaser (BOT_291).

Card Text: <b>Battlecry:</b> Draw a spell from your deck that costs (5) or more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)