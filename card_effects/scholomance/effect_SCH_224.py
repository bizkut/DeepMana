"""Effect for Headmaster Kel'Thuzad (SCH_224).

Card Text: <b><b>Spellburst</b>:</b> If the spell destroys any minions, summon them.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_224t")