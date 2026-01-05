"""Effect for Blood Troll Sapper (TRL_257).

Card Text: After a friendly minion dies, deal 2 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)