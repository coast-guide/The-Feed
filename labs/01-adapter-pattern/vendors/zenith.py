"""Zenith AI SDK (fictional). Treat this as a library you installed and can't change.

Shape: a module-level function, one text per call, results as nested dicts.
"""
from vendors._toy_model import embed_text

OUTAGE = False  # Lab hook: set True to make every call fail the way Zenith fails.


class ZenithError(Exception):
    def __init__(self, code, message):
        super().__init__(f"{code}: {message}")
        self.code = code


def embed_content(content, *, model="zenith-text-1"):
    if OUTAGE:
        raise ZenithError(429, "quota exhausted")
    order = ["money", "food", "vehicles", "animals"]
    return {"model": model, "embedding": {"values": embed_text(content, order)}}
