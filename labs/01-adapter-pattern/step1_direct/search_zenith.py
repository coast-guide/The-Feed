"""Step 1: the same program after switching to Zenith. Diff it against search.py."""
from vendors import zenith

DOCS = [
    "Take your cat to the vet once a year.",
    "Check the engine oil before a long road trip.",
    "A simple pizza recipe with bread flour and cheese.",
    "How to budget for tax and invoice payments.",
    "Puppy training tips for new dog owners.",
    "Fuel prices and the cost of running a car.",
]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))  # vectors are already unit length


def build_index(docs):
    index = []
    for doc in docs:  # Zenith takes one text per call
        response = zenith.embed_content(doc, model="zenith-text-1")  # Zenith's call shape
        index.append((doc, response["embedding"]["values"]))  # Zenith's response shape
    return index


def search(index, query):
    try:
        response = zenith.embed_content(query, model="zenith-text-1")  # Zenith's call shape again
    except zenith.ZenithError as error:  # Zenith's error type
        if error.code != 429:
            raise
        return "search is temporarily unavailable"
    query_vector = response["embedding"]["values"]  # Zenith's response shape again
    best_doc, _ = max(index, key=lambda entry: cosine(entry[1], query_vector))
    return best_doc


if __name__ == "__main__":
    index = build_index(DOCS)
    for query in ["my kitten is sick", "what should I cook tonight", "how much tax do I owe"]:
        print(f"{query!r:32} -> {search(index, query)}")
