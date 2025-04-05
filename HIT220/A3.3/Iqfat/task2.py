class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_phrase = False
        self.document_ids = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase, document_id):
        node = self.root
        for word in phrase:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]

        node.is_end_of_phrase = True

        node.document_ids.add(document_id)

    def search_common_phrases(self):
        results = []

        self._dfs(self.root, [], results)

        return results

    def _dfs(self, node, phrase, results):
        if node.is_end_of_phrase and len(node.document_ids) > 1:
            results.append((" ".join(phrase), node.document_ids))

        for word in node.children:
            child_node = node.children[word]
            self._dfs(child_node, phrase + [word], results)


def extract_trigrams(text):
    words = text.split()

    trigrams = []

    for i in range(len(words) - 2):
        trigram = words[i:i+3]
        trigrams.append(trigram)

    return trigrams


def read_document(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    return text


def detect_common_phrases(documents):
    trie = Trie()

    for document_id, filename in enumerate(documents):
        text = read_document(filename)

        trigrams = extract_trigrams(text)

        for trigram in trigrams:
            trie.insert(trigram, document_id)

    common_phrases = trie.search_common_phrases()

    if len(common_phrases) > 0:
        print("Common phrases found in multiple documents:")
        for phrase, doc_ids in common_phrases:
            if len(doc_ids) > 1:
                print(f"'{phrase}' found in both documents")
    else:
        print("No common phrases found.")


documents = ['doc1.txt', 'doc2.txt']
detect_common_phrases(documents)
