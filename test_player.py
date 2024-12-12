import unittest
from source.player import player_pon
from unittest.mock import patch

# player_pon関数をテストするためのテストケース
class TestPlayer(unittest.TestCase):

    # inputが値が1なら"グー"であることを確認するテスト
    @patch('builtins.input', side_effect=['1'])
    def test_input_1_returns_goo(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")

    # inputが値が2なら"チョキ"であることを確認するテスト
    @patch('builtins.input', side_effect=['2'])
    def test_input_2_returns_choki(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

    # inputが値が3なら"パー"であることを確認するテスト
    @patch('builtins.input', side_effect=['3'])
    def test_input_3_returns_paa(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "パー")

    # inputが不正な値(例: 4)の場合、再入力が求められ、最終的に正しい値を返すことを確認するテスト
    @patch('builtins.input', side_effect=['4', '1'])
    def test_invalid_input_then_valid_input(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")

    # inputが不正な値(例: 0)の場合、再入力が求められ、最終的に正しい値を返すことを確認するテスト
    @patch('builtins.input', side_effect=['0', '2'])
    def test_invalid_input_zero_then_valid_input(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

if __name__ == "__main__":
    unittest.main()
