"""Effect for Surrender to Madness (TRL_500).

Card Text: [x]Destroy 3 of your Mana
Crystals. Give all minions
in your deck +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()