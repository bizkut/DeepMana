"""Effect for Whirling Combatant (BAR_840).

Card Text: [x]<b>Battlecry and Frenzy:</b>
Deal 1 damage to all
other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)