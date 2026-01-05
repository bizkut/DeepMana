"""Effect for Multicaster (DED_524).

Card Text: [x]<b>Battlecry:</b> Draw a card for
 each different spell school 
 you've cast this game.@ <i>(@)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)