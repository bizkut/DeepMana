"""Effect for Sayge, Seer of Darkmoon (DMF_109).

Card Text: <b>Battlecry:</b> Draw 1 card.
<i>(Upgraded for each
friendly <b>Secret</b> that has
triggered this game!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)