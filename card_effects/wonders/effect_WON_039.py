"""Effect for Black Morass Imposter (WON_039).

Card Text: [x]Each turn this is in your
hand, transform it into a
  random 2-Cost minion that  
  gains <b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2