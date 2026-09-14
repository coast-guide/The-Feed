"""Step 2: the core declares the port it needs and names no vendor. Diff it against step1_direct/search.py."""
from typing import Protocol

DOCS = [
    "Take your cat to the vet once a year.",
    "Check the engine oil before a long road trip.",
    "A simple pizza recipe with bread flour and cheese.",
    "How to budget for tax and invoice payments.",
    "Puppy training tips for new dog owners.",
    "Fuel prices and the cost of running a car.",
]


class EmbedderUnavailable(Exception):
    """The core's own word for "try again later", whatever a vendor calls it."""


class Embedder(Protocol):  # The port: what the core needs, in the core's terms
    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per text, in order. Raise EmbedderUnavailable if the service is down."""


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))  # vectors are already unit length


def build_index(embedder, docs):
    return list(zip(docs, embedder.embed(docs)))


def search(embedder, index, query):
    try:
        [query_vector] = embedder.embed([query])
    except EmbedderUnavailable:
        return "search is temporarily unavailable"
    best_doc, _ = max(index, key=lambda entry: cosine(entry[1], query_vector))
    return best_doc
