"""Effect for Shadowlight Scholar (SCH_517).

Card Text: <b>Battlecry:</b> Destroy a Soul Fragment in your deck to deal 3 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)