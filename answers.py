"""Student answers for the STAT 386 Python Fluency Check.

Complete each function and the ScoreTracker class. Keep the public names and
function signatures unchanged. You may add private helper functions if useful.
"""

from __future__ import annotations


def describe_value(value: object) -> str:
    """Return a label describing the built-in type of ``value``.

    Return exactly one of these labels:

    - ``"none"`` for ``None``
    - ``"boolean"`` for a Boolean
    - ``"integer"`` for an integer
    - ``"float"`` for a floating-point number
    - ``"string"`` for a string
    - ``"list"`` for a list
    - ``"tuple"`` for a tuple
    - ``"dictionary"`` for a dictionary
    - ``"set"`` for a set
    - ``"other"`` for anything else

    Remember that Boolean values require careful handling when checking types.
    """
    raise NotImplementedError


def categorize_temperature(celsius: float) -> str:
    """Categorize a Celsius temperature using these inclusive lower ranges.

    - Below 0: ``"freezing"``
    - From 0 up to, but not including, 10: ``"cold"``
    - From 10 up to, but not including, 25: ``"mild"``
    - From 25 up to, but not including, 35: ``"warm"``
    - 35 or above: ``"hot"``
    """
    raise NotImplementedError


def running_totals(values: list[int | float]) -> list[int | float]:
    """Return the cumulative total after each value.

    Examples:
        ``running_totals([2, 3, -1])`` returns ``[2, 5, 4]``.
        ``running_totals([])`` returns ``[]``.

    Do not modify the input list.
    """
    raise NotImplementedError


def select_values(
    values: list[int | float],
    minimum: int | float | None = None,
    maximum: int | float | None = None,
) -> list[int | float]:
    """Return values within the optional inclusive bounds.

    Preserve the original order and duplicates. ``None`` means that a bound is
    absent. Do not modify the input list.

    Examples:
        ``select_values([1, 4, 7], minimum=4)`` returns ``[4, 7]``.
        ``select_values([1, 4, 7], maximum=4)`` returns ``[1, 4]``.
    """
    raise NotImplementedError


def word_counts(text: str) -> dict[str, int]:
    """Return case-insensitive word counts for ``text``.

    Split the text on whitespace. For each resulting piece:

    1. Remove any of ``.,!?;:`` from both ends.
    2. Convert it to lowercase.
    3. Ignore it if nothing remains.

    Apostrophes and hyphens inside words are preserved. For example,
    ``"Data, data-driven data!"`` becomes
    ``{"data": 2, "data-driven": 1}``.
    """
    raise NotImplementedError


def mean_by_group(records: list[dict[str, object]]) -> dict[str, float]:
    """Calculate the mean numeric value for each group.

    Every record has a string ``"group"`` and a ``"value"`` that is an integer,
    float, or ``None``. Skip records whose value is ``None``. Omit groups that
    have no numeric values. Do not modify the input records.

    Example:
        The records ``[{"group": "A", "value": 2},
        {"group": "A", "value": 4}, {"group": "B", "value": None}]``
        produce ``{"A": 3.0}``.
    """
    raise NotImplementedError


def safe_divide(numerator: object, denominator: object) -> float | None:
    """Return ``numerator / denominator`` or ``None`` when division is invalid.

    Return ``None`` when Python raises either ``TypeError`` or
    ``ZeroDivisionError``. Other exceptions should not be suppressed.
    """
    raise NotImplementedError


class ScoreTracker:
    """Track scores for one named student.

    Each instance must have its own independent score list.
    """

    def __init__(self, name: str) -> None:
        """Store ``name`` and initialize an empty public ``scores`` list."""
        raise NotImplementedError

    def add_score(self, score: int | float) -> None:
        """Add a score from 0 through 100, inclusive.

        Raise ``TypeError`` when ``score`` is not an integer or float. Boolean
        values are not valid scores. Raise ``ValueError`` when a numeric score
        is outside the allowed range.
        """
        raise NotImplementedError

    def average(self) -> float | None:
        """Return the arithmetic mean, or ``None`` when there are no scores."""
        raise NotImplementedError

    def count_at_or_above(self, threshold: int | float = 60) -> int:
        """Return the number of scores greater than or equal to ``threshold``."""
        raise NotImplementedError

