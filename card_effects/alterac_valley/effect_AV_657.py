"""Effect for Desecrated Graveyard (AV_657).

Card Text: [x]At the end of your turn,
destroy your lowest Attack
minion to summon a
4/4 Shade. Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_657t")