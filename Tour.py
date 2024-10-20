class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
        return False


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        # Сортируем бегунов по скорости
        sorted_runners = sorted(self.runners, key=lambda runner: runner.speed, reverse=True)
        for i, runner in enumerate(sorted_runners, start=1):
            results[i] = runner.name
        return results


import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_and_nik(self):
        tournament = Tournament(90, [self.usain, self.nik])
        result = tournament.start()
        self.all_results['usain_and_nik'] = result
        # Проверяем правильность распределения мест
        self.assertEqual(result[1], "Усэйн")
        self.assertEqual(result[2], "Ник")

    def test_andrey_and_nik(self):
        tournament = Tournament(90, [self.andrey, self.nik])
        result = tournament.start()
        self.all_results['andrey_and_nik'] = result
        # Проверяем правильность распределения мест
        self.assertEqual(result[1], "Андрей")
        self.assertEqual(result[2], "Ник")

    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nik])
        result = tournament.start()
        self.all_results['usain_andrey_and_nik'] = result
        # Проверяем правильность распределения мест
        self.assertEqual(result[1], "Усэйн")
        self.assertEqual(result[2], "Андрей")
        self.assertEqual(result[3], "Ник")


if __name__ == '__main__':
    unittest.main()
