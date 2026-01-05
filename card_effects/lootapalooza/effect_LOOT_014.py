"""Effect for Kobold Librarian (LOOT_014).

Card Text: <b>Battlecry:</b> Draw a card. Deal 2 damage to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)