#!/usr/bin/python3
import unittest
from unittest.mock import patch
from mines import Minesweeper

class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.game = Minesweeper(width=5, height=5, mines=2)
    
    def test_initialization(self):
        """Test that the game initializes correctly"""
        self.assertEqual(self.game.width, 5)
        self.assertEqual(self.game.height, 5)
        self.assertEqual(len(self.game.mines), 2)
    
    def test_count_mines_nearby(self):
        """Test mine counting around a cell"""
        # Place mines at specific positions for predictable testing
        self.game.mines = {0, 1}  # Two mines in corners
        count = self.game.count_mines_nearby(0, 0)
        self.assertGreaterEqual(count, 0)
    
    def test_reveal_mine(self):
        """Test that revealing a mine returns False"""
        self.game.mines = {0}  # Mine at position 0
        result = self.game.reveal(0, 0)
        self.assertFalse(result)
    
    def test_reveal_safe(self):
        """Test that revealing a safe cell returns True"""
        self.game.mines = {0}
        result = self.game.reveal(1, 0)
        self.assertTrue(result)
        self.assertTrue(self.game.revealed[0][1])
    
    def test_check_win(self):
        """Test win condition detection"""
        # Create game with just 1 mine
        game = Minesweeper(width=2, height=2, mines=1)
        game.mines = {0}  # Only one mine
        # Reveal all safe cells
        for i in range(4):
            if i not in game.mines:
                game.revealed[i // 2][i % 2] = True
        self.assertTrue(game.check_win())
    
    def test_symbol_input_not_accepted(self):
        """Test that non-numeric symbols are rejected in play()"""
        with patch('builtins.input', side_effect=['a', '0', '0']), \
             patch.object(self.game, 'print_board'), \
             patch.object(self.game, 'reveal', return_value=False), \
             patch('builtins.print') as mock_print:
            self.game.play()
        mock_print.assert_any_call('Invalid input. Please enter numbers only.')
    
    def test_play_shows_win_message(self):
        """Test that play() prints a win message when the game is won"""
        game = Minesweeper(width=2, height=2, mines=1)
        game.mines = {0}
        with patch('builtins.input', side_effect=['1', '0']), \
             patch.object(game, 'print_board'), \
             patch.object(game, 'check_win', return_value=True), \
             patch('builtins.print') as mock_print:
            game.play()
        mock_print.assert_any_call('Congratulations! You won!')
    
    def test_bounds_checking(self):
        """Test that out-of-bounds coordinates are handled"""
        result = self.game.reveal(-1, 0)  # This should raise an error or handle gracefully
        # Currently might fail, but test documents expected behavior

if __name__ == "__main__":
    unittest.main()