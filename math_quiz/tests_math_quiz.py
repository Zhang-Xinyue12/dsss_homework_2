import unittest
from math_quiz import calculate_result_A, calculate_result_B, calculate_result_C


class TestMathGame(unittest.TestCase):
    #test calculate_result_A：Checks if the returned integer is within the given range.检查返回的整数是否在给定范围内。
    #test calculate_result_B：Verify that the return value is a legal operator (+, -, or *).验证返回值是否是合法的运算符（+、- 或 *）。
    #test calculate_result_C：Test the +, -, and * operators to ensure that they return the correct answer.对 +、- 和 * 运算符进行测试，确保返回的答案正确。

    def test_calculate_result_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = calculate_result_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_calculate_result_B(self):
        """Test calculate_result_B to return a valid operator"""
        result = calculate_result_B()
        self.assertIn(result, ['+', '-', '*'], "Result is not a valid operator.")
        # TODO
        #pass

    def test_calculate_result_C(self):
        """Test calculate_result_C to check correct computation of expressions"""
        # Test addition
        problem, answer = calculate_result_C(3, 2, '+')
        self.assertEqual(answer, 3 + 2, f"Expected 5, got {answer}")

        # Test subtraction
        problem, answer = calculate_result_C(5, 3, '-')
        self.assertEqual(answer, 5 - 3, f"Expected 2, got {answer}")

        # Test multiplication
        problem, answer = calculate_result_C(4, 2, '*')
        self.assertEqual(answer, 4 * 2, f"Expected 8, got {answer}")
            #test_cases = [
            #   (5, 2, '+', '5 + 2', 7),
            #    ''' TODO add more test cases here '''
            #]

            #for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
             #   pass

if __name__ == "__main__":
    unittest.main()



