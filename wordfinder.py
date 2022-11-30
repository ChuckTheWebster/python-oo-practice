from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create list of words from file and
        prints how many words are in the list"""
        self.file = open(path)
        self.words = self.populate_words(self.file)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder file={self.file} words={self.words}>"

    def populate_words(self, file):
        """Populates a list with words from a file"""
        words = []
        for line in file:
            fixed_word = line.strip()
            words.append(fixed_word)

        return words

    def random(self):
        """Returns a random word from instance's list of words"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """WordFinder that filters out empty lines and comments"""

    def __init__(self, file):
        """Create a list of words from file but filters out empty lines
        and comments, and prints how many words are in the list"""
        super().__init__(file)
        self.words = self.fix_words()

    def __repr__(self):
        return f"<SpecialWordFinder file={self.file} words={self.words}>"

    def fix_words(self):
        """Creates a new list that filters out empty strings and strings that
        start with '#'"""
        special_words = []
        for word in self.words:
            if not word.startswith("#") and not word == "":
                special_words.append(word)
        return special_words


# "/Users/petrachoir/Desktop/words.txt"
# "/usr/share/dict/words"
