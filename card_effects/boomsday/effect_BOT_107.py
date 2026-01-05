"""Effect for Missile Launcher (BOT_107).

Card Text: [x]<b>Magnetic</b>
At the end of your turn,
deal 1 damage to all
other characters.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)