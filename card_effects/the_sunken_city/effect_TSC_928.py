"""Effect for Security Automaton (TSC_928).

Card Text: After you summon a Mech, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_928t")