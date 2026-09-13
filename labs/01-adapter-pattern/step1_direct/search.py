"""Step 1: the core calls Acme directly. It works. Now read it asking what a switch would cost."""
from vendors import acme

DOCS = [
    "Take your cat to the vet once a year.",
    "Check the engine oil before a long road trip.",
    "A simple pizza recipe with bread flour and cheese.",
    "How to budget for tax and invoice payments.",
    "Puppy training tips for new dog owners.",
    "Fuel prices and the cost of running a car.",
]

client = acme.AcmeClient(api_key="lab-key")


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))  # vectors are already unit length


def build_index(docs):
    index = []
    for start in range(0, len(docs), acme.MAX_BATCH):  # Acme's batch limit
        batch = docs[start : start + acme.MAX_BATCH]
        response = client.embed(inputs=batch, model="acme-embed-2")  # Acme's call shape
        index += zip(batch, [item.vector for item in response.data])  # Acme's response shape
    return index


def search(index, query):
    try:
        response = client.embed(inputs=[query], model="acme-embed-2")  # Acme's call shape again
    except acme.RateLimitError:  # Acme's error type
        return "search is temporarily unavailable"
    query_vector = response.data[0].vector  # Acme's response shape again
    best_doc, _ = max(index, key=lambda entry: cosine(entry[1], query_vector))
    return best_doc


if __name__ == "__main__":
    index = build_index(DOCS)
    for query in ["my kitten is sick", "what should I cook tonight", "how much tax do I owe"]:
        print(f"{query!r:32} -> {search(index, query)}")
