

class Tokenizer:

    def __init__(self):
        self.on_word = None

    def read(self, text):
        assert self.on_word is not None

        for word in text.split():
            if len(word) > 0:
                self.on_word(word)
