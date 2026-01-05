"""Effect for Vengeful Walloper (RLK_213).

Card Text: <b>Rush</b>. Costs (1) less for each <b>Outcast</b> card you've played this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass