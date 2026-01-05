"""Effect for Malevolent Strike (DMF_518).

Card Text: [x]Destroy a minion.
 Costs (1) less for each
  card in your deck that
  didn't start there.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()