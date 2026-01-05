"""Effect for King Phaoris (ULD_304).

Card Text: [x]<b>Battlecry:</b> For each spell
in your hand, summon a
random minion of the
same Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_304t")