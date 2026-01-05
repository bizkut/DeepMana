"""Effect for Witch of the Arch-Thief (WON_104).

Card Text: [x]<b>Battlecry:</b> Summon a
1/3 Voidwalker with <b>Taunt</b>.
If your opponent has more
minions, repeat.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_104t")