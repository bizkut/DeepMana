"""Effect for Astalor Bloodsworn (RLK_222).

Card Text: <b>Battlecry:</b> Add Astalor, the Protector to your hand. <b>Manathirst (5):</b> Deal 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)