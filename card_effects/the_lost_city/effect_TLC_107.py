"""Effect for Stormbrewer (TLC_107).

Card Text: Whenever this attacks,
deal 3 damage to
the target first.
<b>Kindred:</b> Gain <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)