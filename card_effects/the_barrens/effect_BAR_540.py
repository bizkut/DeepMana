"""Effect for Plaguemaw the Rotting (BAR_540).

Card Text: [x]After a friendly minion with
 <b>Taunt</b> dies, summon a new
 copy of it without <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_540t")