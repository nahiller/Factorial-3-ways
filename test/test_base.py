class TestBase():
    def test_zero_1_2_5_10_20_50_returns_correct_value(self):
        inputs_and_results = [(0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800), (20, 2432902008176640000), (50, 30414093201713378043612608166064768844377641568960512000000000000)]

        for input, result in inputs_and_results:
            with self.subTest(input = input):
                self.assertEquals(result, self.get_factorial()(input))