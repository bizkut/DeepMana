import unittest
from simulator.game import Game
from simulator.player import Player
from runtime.parser import LogParser
from simulator.enums import Zone

class TestLogParser(unittest.TestCase):
    def test_parse_coin_to_hand(self):
        # 1. Setup Empty Game (Listen Mode)
        game = Game()
        p1 = Player("Player 1", game)
        p2 = Player("Player 2", game)
        game.players = [p1, p2]
        
        # Ensure players are reset/empty
        for p in game.players:
            p.hand = []
            p.board = []
            
        parser = LogParser(game)
        
        # 2. Simulate Log Line: Creating/Drawing the Coin
        # Real log sample: 
        # D 02:22:20.123456 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=60 cardId=GAME_005 name=Coin] tag=ZONE value=HAND
        log_line = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=60 cardId=GAME_005 name=Coin] tag=ZONE value=HAND"
        
        parser.parse_line(log_line)
        
        # 3. Assertions
        # Player 0 (default controller in current simple parser info) should have the coin
        p1_check = game.players[0]
        
        self.assertEqual(len(p1_check.hand), 1, "Player should have 1 card in hand")
        coin = p1_check.hand[0]
        
        self.assertEqual(coin.card_id, "GAME_005")
        self.assertEqual(coin.entity_id, 60)
        self.assertEqual(coin.zone, Zone.HAND)
        
    def test_parse_play_minion(self):
        # 1. Setup
        game = Game()
        p1 = Player("Player 1", game)
        p2 = Player("Player 2", game)
        game.players = [p1, p2]
        
        parser = LogParser(game)
        p1 = game.players[0]
        
        # 2. Put card in hand first
        log_draw = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=20 cardId=CS2_120 name=RiverCrocolisk] tag=ZONE value=HAND"
        parser.parse_line(log_draw)
        
        self.assertEqual(len(p1.hand), 1)
        self.assertEqual(len(p1.board), 0)
        
        # 3. Play it (Hand -> Play)
        log_play = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=20 cardId=CS2_120 name=RiverCrocolisk] tag=ZONE value=PLAY"
        parser.parse_line(log_play)
        
        self.assertEqual(len(p1.hand), 0, "Hand should be empty")
        self.assertEqual(len(p1.board), 1, "Board should have 1 minion")
        self.assertEqual(p1.board[0].zone, Zone.PLAY)

    def test_parse_damage(self):
        # 1. Setup Game with a Minion
        game = Game()
        p1 = Player("Player 1", game)
        p2 = Player("Player 2", game)
        game.players = [p1, p2]
        
        parser = LogParser(game)
        
        # Create a minion manually to damage it
        from simulator.factory import create_card
        minion = create_card("CS2_120", p1) # River Crocolisk (2/3)
        minion.entity_id = 99
        minion.zone = Zone.PLAY
        p1.board.append(minion)
        parser.entity_map[99] = minion
        
        # 2. Log: Damage Trigger
        # TAG_CHANGE Entity=[id=99 ...] tag=DAMAGE value=2
        log_dmg = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=99 cardId=CS2_120 name=RiverCrocolisk] tag=DAMAGE value=2"
        parser.parse_line(log_dmg)
        
        # 3. Assert damage taken
        self.assertEqual(minion.damage, 2, "Minion should have 2 damage")
        self.assertEqual(minion.health, 1, "Minion (3 HP) - 2 dmg = 1 health remaining")

    def test_parse_turn_change(self):
        game = Game()
        p1 = Player("Player 1", game)
        p2 = Player("Player 2", game)
        game.players = [p1, p2]
        game.current_player_idx = 0
        
        parser = LogParser(game)
        # Assuming P1 is usually ID 2 or similar in logs (GameEntity=1, P1=2, P2=3)
        # We need a way to map "Player 2" string to P2 object in parse.
        # Let's verify parser logic for name resolution.
        
        # Log: TAG_CHANGE Entity=Player 2 tag=CURRENT_PLAYER value=1
        log_turn = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=Player 2 tag=CURRENT_PLAYER value=1"
        parser.parse_line(log_turn)
        
        self.assertEqual(game.current_player, p2, "Current player should switch to Player 2")

    def test_parse_choices(self):
        # 1. Setup
        game = Game()
        p1 = Player("Player 1", game)
        p2 = Player("Player 2", game)
        game.players = [p1, p2]
        parser = LogParser(game)
        
        # 2. Simulate 3 cards appearing in SETASIDE (Discover Options)
        # TAG_CHANGE Entity=[id=101 cardId=OPTION_1 ...] tag=ZONE value=SETASIDE
        log_opt1 = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=101 cardId=OPT_001 name=OptionA] tag=ZONE value=SETASIDE"
        log_opt2 = "D 00:00:00.000000 GameState.DebugPrintPower() - TAG_CHANGE Entity=[id=102 cardId=OPT_002 name=OptionB] tag=ZONE value=SETASIDE"
        
        parser.parse_line(log_opt1)
        parser.parse_line(log_opt2)
        
        # 3. Assertions
        p1_check = game.players[0]
        self.assertEqual(len(p1_check.setaside), 2, "Should have 2 options in Setaside")
        self.assertEqual(p1_check.setaside[0].card_id, "OPT_001")
        self.assertEqual(p1_check.setaside[1].card_id, "OPT_002")
        self.assertEqual(p1_check.setaside[0].zone, Zone.SETASIDE)

if __name__ == "__main__":
    unittest.main()
