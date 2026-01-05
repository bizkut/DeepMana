"""Effect for High Abbess Alura (SCH_141).

Card Text: <b><b>Spellburst</b>:</b> Cast a spell from your deck <i>(targets this if possible)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass