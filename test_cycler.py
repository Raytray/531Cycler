import cycler
import unittest


class TestCycler(unittest.TestCase):
    def test_calculate_training_max(self):
        assert cycler.calculate_training_max(155, 7) == 172

    def test_round_weight_down(self):
        assert cycler.round_weight(72) == 70

    def test_round_weight_up(self):
        assert cycler.round_weight(73) == 75

    def test_round_weight_base_down(self):
        assert cycler.round_weight(73, 10) == 70

    def test_round_weight_base_up(self):
        assert cycler.round_weight(68, 10) == 70

    def test_round_weight_base_up(self):
        assert cycler.round_weight(68, 10) == 70

    def test_get_cycle_weights(self):
        assert cycler.get_cycle_weights(110, .5, .6, .9) == [55, 65, 100]


if __name__ == '__main__':
    unittest.main()
