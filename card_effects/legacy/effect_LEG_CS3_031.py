"""Effect for Alexstrasza the Life-Binder (LEG_CS3_031).

Card Text: [x]<b>Battlecry</b>: Choose a
character. If it's friendly,
restore 8 Health. If it's an
   enemy, deal 8 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)