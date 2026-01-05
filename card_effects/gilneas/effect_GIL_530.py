"""Effect for Murkspark Eel (GIL_530).

Card Text: <b>Battlecry:</b> If your deck has only even-Cost cards, deal 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)