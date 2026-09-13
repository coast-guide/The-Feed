"""The toy "model" behind both fake vendors.

An embedding turns text into a list of numbers so that similar texts get similar lists.
This toy counts words per topic. Real models learn hundreds of dimensions, but the property
this lab needs is the same: a vector only means something next to vectors from the same model.
Both vendors use the same topics in a different order, so their vectors have the same length
but live in different spaces.
"""
import math

TOPICS = {
    "animals": {"cat", "cats", "dog", "dogs", "kitten", "puppy", "pet", "pets", "vet"},
    "vehicles": {"car", "cars", "engine", "road", "fuel", "tyre", "drive"},
    "food": {"pizza", "bread", "cheese", "pasta", "cook", "recipe"},
    "money": {"price", "tax", "invoice", "salary", "budget", "cost"},
}


def embed_text(text, order):
    words = text.lower().replace(".", " ").replace("?", " ").replace(",", " ").split()
    counts = [sum(w in TOPICS[t] for w in words) for t in order]
    norm = math.sqrt(sum(c * c for c in counts)) or 1.0
    return [c / norm for c in counts]
