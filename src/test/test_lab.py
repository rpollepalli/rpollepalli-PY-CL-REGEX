import unittest
import re
from src.main.lab import regExExerciseOne, regExExerciseTwo, regExExerciseThree
class TestRegexExercises(unittest.TestCase):
    def test_exercise_one(self):
        test1 = "Alice has 3 apples, Bob has 5 oranges, and Charlie has 2 bananas. David has 8 grapes, and Emily has 4 peaches."
        result1 = regExExerciseOne(test1)

        
        self.assertEqual(len(re.findall(r'has', test1)), len(re.findall('owns', result1)))

    def test_exercise_two_one(self):
        test = "Alice has 3 apples, Bob has 5 oranges, and Charlie has 2 bananas. David has 8 grapes, and Emily has 4 peaches."
        result = regExExerciseTwo(test)

        self.assertEqual(len(re.findall(r'\d', test)), len(re.findall(r'X', result)))

    def test_exercise_two_two(self):
        test = "my phone number is 323-348-2384"
        result = regExExerciseTwo(test)

        self.assertEqual(len(re.findall(r'\d', test)), len(re.findall(r'X', result)))

    def test_exercise_three_one(self):
        test = "example@example.com"
        result = regExExerciseThree(test)

        self.assertTrue(result)

    def test_exercise_three_two(self):
        test = "example@.com"
        result = regExExerciseThree(test)

        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()