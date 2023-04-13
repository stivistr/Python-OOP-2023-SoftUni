from exam2.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('player', 20, 100.5)
        self.new_player = TennisPlayer('player2', 30, 200.5)

    def test_correct_init(self):
        self.assertEqual('player', self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(100.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_error_occur_with_wrong_name(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = 'ab'

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_error_occur_with_wrong_age(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 15

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_tournament_already_won(self):
        self.player.add_new_win('test')
        result = self.player.add_new_win('test')

        self.assertEqual("test has been already added to the list of wins!", result)

    def test_tournament_not_played_yet(self):
        self.player.add_new_win('test')

        self.assertEqual(['test'], self.player.wins)

    def test_who_is_better_player(self):
        result = self.player.__lt__(self.new_player)

        self.assertEqual('player2 is a top seeded player and he/she is '
                         'better than player', result)

    def test_first_player_is_better(self):
        self.player.points, self.new_player.points = self.new_player.points, self.player.points
        result = self.player.__lt__(self.new_player)

        self.assertEqual('player is a better player than player2', result)

    def test_correct_string_representation(self):
        self.assertEqual("Tennis Player: player\n"
                         f"Age: 20\n"
                         f"Points: 100.5\n"
                         f"Tournaments won: ", self.player.__str__())

    def test_correct_string_representation_with_wins(self):
        self.player.wins.append('test')
        self.assertEqual("Tennis Player: player\n"
                         f"Age: 20\n"
                         f"Points: 100.5\n"
                         f"Tournaments won: test", self.player.__str__())

    def test_correct_string_representation_with_int_points(self):
        self.player.points = 100
        self.assertEqual("Tennis Player: player\n"
                         f"Age: 20\n"
                         f"Points: 100.0\n"
                         f"Tournaments won: ", self.player.__str__())

    def test_correct_string_representation_with_more_wins(self):
        self.player.wins.append('test')
        self.player.wins.append('test1')
        self.assertEqual("Tennis Player: player\n"
                         f"Age: 20\n"
                         f"Points: 100.5\n"
                         f"Tournaments won: test, test1", self.player.__str__())

if __name__ == '__main__':
    main()
