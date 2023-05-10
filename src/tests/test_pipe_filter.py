import unittest
from patterns.pipe_filter import UppercaseFilter, ReverseFilter, Pipeline


class UppercaseFilterTests(unittest.TestCase):
    def test_process_converts_string_to_uppercase(self):
        filter_instance = UppercaseFilter()
        result = filter_instance.process("Just a TeSt")
        self.assertEqual(result, "JUST A TEST")


class ReverseFilterTests(unittest.TestCase):
    def test_process_reverses_string(self):
        filter_instance = ReverseFilter()
        result = filter_instance.process("Just A TEST!")
        self.assertEqual(result, "!TSET A tsuJ")


class PipelineTests(unittest.TestCase):
    def test_run_applies_filters_in_a_pipeline(self):
        pipeline = Pipeline()
        pipeline.add_filter(UppercaseFilter())
        pipeline.add_filter(ReverseFilter())
        result = pipeline.run("Just a TeSt?")
        self.assertEqual(result, "?TSET A TSUJ")


if __name__ == '__main__':
    unittest.main()
