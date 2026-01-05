"""Effect for Bearon Gla'shear (AV_257).

Card Text: [x]<b>Battlecry:</b> For each Frost
spell you've cast this game,
summon a 3/4 Elemental
that <b>Freezes</b>.@ <i>(@)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_257t")