"""Effect for Soulciologist Malicia (SCH_703).

Card Text: <b>Battlecry:</b> For each Soul Fragment in your deck, summon a 3/3 Soul with <b>Rush</b>.@ <i>(@)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_703t")