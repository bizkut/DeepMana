"""Effect for Alexandros Mograine (RLK_706).

Card Text: <b>Battlecry:</b> For the rest of the game, deal 3 damage to your opponent at the end of your turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)