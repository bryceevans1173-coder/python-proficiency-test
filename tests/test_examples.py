"""Public example tests for the Python Fluency Check.

These tests demonstrate the interface and a few ordinary cases. The automatic
grader checks additional boundaries and interactions.
"""

import unittest

from answers import (
    ScoreTracker,
    categorize_temperature,
    describe_value,
    mean_by_group,
    running_totals,
    safe_divide,
    select_values,
    word_counts,
)


class FluencyCheckExamples(unittest.TestCase):
    def test_describe_value_examples(self) -> None:
        self.assertEqual(describe_value(True), "boolean")
        self.assertEqual(describe_value(3), "integer")
        self.assertEqual(describe_value([1, 2]), "list")

    def test_categorize_temperature_examples(self) -> None:
        self.assertEqual(categorize_temperature(-2), "freezing")
        self.assertEqual(categorize_temperature(20), "mild")
        self.assertEqual(categorize_temperature(40), "hot")

    def test_running_totals_examples(self) -> None:
        self.assertEqual(running_totals([2, 3, -1]), [2, 5, 4])
        self.assertEqual(running_totals([]), [])

    def test_select_values_examples(self) -> None:
        self.assertEqual(select_values([1, 4, 7], minimum=4), [4, 7])
        self.assertEqual(select_values([1, 4, 7], maximum=4), [1, 4])

    def test_word_counts_example(self) -> None:
        self.assertEqual(
            word_counts("Data, data-driven data!"),
            {"data": 2, "data-driven": 1},
        )

    def test_mean_by_group_example(self) -> None:
        records = [
            {"group": "A", "value": 2},
            {"group": "A", "value": 4},
            {"group": "B", "value": None},
        ]
        self.assertEqual(mean_by_group(records), {"A": 3.0})

    def test_safe_divide_examples(self) -> None:
        self.assertEqual(safe_divide(9, 3), 3)
        self.assertIsNone(safe_divide(9, 0))

    def test_score_tracker_example(self) -> None:
        tracker = ScoreTracker("Ada")
        tracker.add_score(80)
        tracker.add_score(90)

        self.assertEqual(tracker.name, "Ada")
        self.assertEqual(tracker.scores, [80, 90])
        self.assertEqual(tracker.average(), 85)
        self.assertEqual(tracker.count_at_or_above(85), 1)


if __name__ == "__main__":
    unittest.main()
