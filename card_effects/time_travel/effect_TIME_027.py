"""Effect for Tachyon Barrage (TIME_027).

Card Text: Deal $6 damage split among all enemies. Shuffle 2 Shreds of Time into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)