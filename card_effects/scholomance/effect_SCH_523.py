"""Effect for Ceremonial Maul (SCH_523).

Card Text: <b>Spellburst</b>: Summon a Student with <b>Taunt</b> and stats equal to the spell's Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_523t")