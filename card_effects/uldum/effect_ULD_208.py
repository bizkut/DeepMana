"""Effect for Khartut Defender (ULD_208).

Card Text: [x]<b>Taunt</b>, <b>Reborn</b>
<b>Deathrattle:</b> Restore #3
Health to your hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)