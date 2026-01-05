"""Effect for Defense Attorney Nathanos (CORE_MAW_011).

Card Text: [x]<b>Battlecry:</b> <b>Discover</b> a friendly
<b>Deathrattle</b> minion that died
this game. Gain its <b>Deathrattle</b>
and then trigger it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    from simulator import CardDatabase
    db = CardDatabase.get_instance()
    cards = [c.card_id for c in db._cards.values() if c.collectible][:100]
    def on_discover(game, chosen_id):
        from simulator.factory import create_card
        c = create_card(chosen_id, game)
        if c: player.add_to_hand(c)
    game.initiate_discover(player, random.sample(cards, 3), on_discover)


def deathrattle(game, source):
    pass