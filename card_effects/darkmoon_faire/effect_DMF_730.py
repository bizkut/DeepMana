"""Effect for Moontouched Amulet (DMF_730).

Card Text: Give your hero +4 Attack this turn. <b>Corrupt:</b> And gain 6 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4