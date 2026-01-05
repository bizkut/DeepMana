"""Effect for Hold the Bridge (AV_338).

Card Text: [x]Give a minion +2/+1
and <b>Divine Shield</b>.
It gains <b>Lifesteal</b> until
end of turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2