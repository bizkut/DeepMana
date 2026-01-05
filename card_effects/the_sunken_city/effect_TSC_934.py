"""Effect for Pirate Admiral Hooktusk (TSC_934).

Card Text: <b>Battlecry:</b> If you've summoned 7 other Pirates this game, plunder the enemy!0 <i>({0} left!)</i>0 <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_934t")