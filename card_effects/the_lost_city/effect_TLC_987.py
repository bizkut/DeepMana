"""Effect for Questing Assistant (TLC_987).

Card Text: [x]<b>Battlecry:</b> If you played
a <b>Quest</b> this game,
deal 3 damage to an
enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)