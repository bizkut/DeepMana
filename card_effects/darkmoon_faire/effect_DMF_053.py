"""Effect for Blood of G'huun (DMF_053).

Card Text: [x]<b>Taunt</b>
At the end of your turn,
summon a 5/5 copy of a
minion in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_053t")