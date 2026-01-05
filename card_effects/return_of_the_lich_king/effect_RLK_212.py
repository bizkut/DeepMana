"""Effect for Brutal Annihilan (RLK_212).

Card Text: [x]<b>Taunt</b>, <b>Rush</b>
After this minion survives
damage, deal that amount
to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)