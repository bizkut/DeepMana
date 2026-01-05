"""Effect for Garrosh's Gift (CORE_GIFT_07).

Card Text: <b>Discover</b> a <b>Temporary</b> Execute, Shield Block, or Brawl.
"""

from simulator.enums import CardType

def on_play(game, source, target):
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