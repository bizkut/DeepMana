"""Effect for Mistress of Mixtures (CORE_CFM_120).

Card Text: <b>Deathrattle:</b> Restore #4 Health to each hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)