"""Effect for Animated Avalanche (YOD_007).

Card Text: [x]<b>Battlecry:</b> If you played
an Elemental last turn,
summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_007t")