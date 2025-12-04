from collections import defaultdict
import numpy as np


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.tokens = corpus.split()
        self.term_dict = None

    def get_term_dict(self):
        """
        Build a dictionary where each word maps to a list of words
        that follow it in the corpus.
        """
        term_dict = defaultdict(list)

        for i in range(len(self.tokens) - 1):
            current_word = self.tokens[i]
            next_word = self.tokens[i + 1]
            term_dict[current_word].append(next_word)

        self.term_dict = dict(term_dict)
        return self.term_dict

    def generate(self, seed_term=None, term_count=15):
        """
        Generate text using a first-order Markov chain.
        Raises ValueError if the seed term is invalid.
        """
        if self.term_dict is None:
            self.get_term_dict()

        # Seed handling for autograder
        if seed_term is not None:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current = seed_term
        else:
            current = np.random.choice(list(self.term_dict.keys()))

        output = [current]

        for _ in range(term_count - 1):
            followers = self.term_dict.get(current, [])
            if followers:
                current = np.random.choice(followers)
            else:
                current = np.random.choice(list(self.term_dict.keys()))
            output.append(current)

        return " ".join(output)