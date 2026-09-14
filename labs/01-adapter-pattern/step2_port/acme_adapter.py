"""Step 2: the only file that knows Acme. It translates Acme into the core's Embedder port."""
from step2_port.search import EmbedderUnavailable
from vendors import acme


class AcmeEmbedder:
    def __init__(self, api_key, model="acme-embed-2"):
        self.client = acme.AcmeClient(api_key=api_key)
        self.model = model

    def embed(self, texts):
        vectors = []
        for start in range(0, len(texts), acme.MAX_BATCH):  # Acme's batch limit
            batch = texts[start : start + acme.MAX_BATCH]
            try:
                response = self.client.embed(inputs=batch, model=self.model)  # Acme's call shape
            except acme.RateLimitError as error:  # Acme's error type, translated to the core's
                raise EmbedderUnavailable("Acme is rate limiting") from error
            vectors += [item.vector for item in response.data]  # Acme's response shape
        return vectors
