"""Step 2: the composition root, the one place that picks a vendor and hands it to the core."""
from step2_port.acme_adapter import AcmeEmbedder
from step2_port.search import DOCS, build_index, search

if __name__ == "__main__":
    embedder = AcmeEmbedder(api_key="lab-key")
    index = build_index(embedder, DOCS)
    for query in ["my kitten is sick", "what should I cook tonight", "how much tax do I owe"]:
        print(f"{query!r:32} -> {search(embedder, index, query)}")
