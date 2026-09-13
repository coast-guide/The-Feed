"""Acme Embeddings SDK (fictional). Treat this as a library you installed and can't change.

Shape: a client object, batch calls of at most MAX_BATCH texts, results as objects.
"""
from vendors._toy_model import embed_text

MAX_BATCH = 4
OUTAGE = False  # Lab hook: set True to make every call fail the way Acme fails.


class RateLimitError(Exception):
    pass


class Embedding:
    def __init__(self, index, vector):
        self.index = index
        self.vector = vector


class EmbedResponse:
    def __init__(self, data):
        self.data = data  # list[Embedding]


class AcmeClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def embed(self, inputs, model="acme-embed-2"):
        if OUTAGE:
            raise RateLimitError("429: slow down")
        if len(inputs) > MAX_BATCH:
            raise ValueError(f"Acme accepts at most {MAX_BATCH} inputs per call")
        order = ["animals", "vehicles", "food", "money"]
        return EmbedResponse([Embedding(i, embed_text(t, order)) for i, t in enumerate(inputs)])
