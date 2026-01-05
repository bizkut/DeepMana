"""Effect for Sorcerous Substitute (SCH_530).

Card Text: <b>Battlecry:</b> If you have <b>Spell Damage</b>, summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_530t")