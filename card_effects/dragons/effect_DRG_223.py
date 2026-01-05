"""Effect for Cumulo-Maximus (DRG_223).

Card Text: <b>Battlecry:</b> If you have <b>Overloaded</b> Mana Crystals, deal 5 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)