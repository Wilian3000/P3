"""Simple in-memory storage for evaluation results."""

from collections import defaultdict
from uuid import uuid4


class Storage:
    def __init__(self):
        self._data = defaultdict(dict)

    def save(self, payload: dict) -> str:
        eval_id = uuid4().hex
        self._data[eval_id] = payload
        return eval_id

    def get(self, eval_id: str) -> dict | None:
        return self._data.get(eval_id)


storage = Storage()
