"""Effect for Magehunter (SCH_276).

Card Text: <b>Rush</b>
Whenever this attacks a minion, <b>Silence</b> it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)