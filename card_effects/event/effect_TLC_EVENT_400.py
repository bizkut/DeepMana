"""Effect for Storm the Gates (TLC_EVENT_400).

Card Text: [x]<b>Sidequest:</b> Play
3 Beasts or Undead.
<b>Reward:</b> Craft a custom
Zombeast. It costs (3) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass