"""Effect for Baroness Vashj (REV_925).

Card Text: [x]If this would transform
into a minion, summon
that minion instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_925t")