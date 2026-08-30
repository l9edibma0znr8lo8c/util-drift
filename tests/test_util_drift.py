from src.util_drift.core import watch


def test_watch_keeps_first():
    rows = [{"id": "a"}, {"id": "a"}, {"id": "b"}]
    assert watch(rows) == [{"id": "a"}, {"id": "b"}]
