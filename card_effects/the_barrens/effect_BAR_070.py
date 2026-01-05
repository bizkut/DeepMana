"""Effect for Gruntled Patron (BAR_070).

Card Text: <b>Frenzy:</b> Summon another Gruntled Patron.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_070t")