# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populate_suffixtrie_from(string)

    def populate_suffixtrie_from(self, string: str):

        for start_index in range(0, len(string)):
            parent_entry = self.root

            for char_index in range(start_index, len(string)):
                char = string[char_index]

                char_entry = parent_entry.get(char)
                if char_entry is None:
                    char_entry = {}
                    parent_entry[char] = char_entry

                parent_entry = char_entry

            parent_entry[self.endSymbol] = True
        pass

    def contains(self, string: str):
        entry = self.root

        for char in string:
            entry = entry.get(char)
            if entry is None:
                return False
        return entry.get(self.endSymbol, False)
