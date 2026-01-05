"""Effect for Fel Lord Betrug (DAL_607).

Card Text: [x]Whenever you draw a
minion, summon a copy
 with <b>Rush</b> that dies at
end of turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)