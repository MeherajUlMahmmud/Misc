class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_trigram = False
        self.document_ids = set()


class PhraseTrie:
    def __init__(self):
        self.root_node = Node()

    def add_trigram(self, trigram, document_id):
        current_node = self.root_node
        for word in trigram:
            if word not in current_node.children:
                current_node.children[word] = Node()
            current_node = current_node.children[word]
        current_node.is_end_of_trigram = True
        current_node.document_ids.add(document_id)

    def find_common_phrases(self):
        common_phrases = []
        self._dfs_search(self.root_node, [], common_phrases)
        return common_phrases

    def _dfs_search(self, node, phrase, common_phrases):
        if node.is_end_of_trigram and len(node.document_ids) > 1:
            common_phrases.append((" ".join(phrase), node.document_ids))

        for word, next_node in node.children.items():
            self._dfs_search(next_node, phrase + [word], common_phrases)


def get_trigrams_from_text(text):
    words = text.split()
    trigram_list = []
    if len(words) >= 3:
        for i in range(len(words) - 2):
            trigram_list.append(words[i:i+3])
    return trigram_list


def load_document(file_name):
    with open(file_name, 'r') as f:
        content = f.read().lower()
    return content


def find_common_phrases_across_documents(documents):
    phrase_trie = PhraseTrie()

    for document_index, file_name in enumerate(documents):
        content = load_document(file_name)
        trigrams = get_trigrams_from_text(content)

        for trigram in trigrams:
            phrase_trie.add_trigram(trigram, document_index)

    common_phrases = phrase_trie.find_common_phrases()

    if common_phrases:
        print("Common phrases found across documents:")
        for phrase, document_ids in common_phrases:
            if len(document_ids) > 1:
                print(f"Phrase: '{phrase}' appears in both documents")
    else:
        print("No common phrases found.")


document_files = ['doc1.txt', 'doc2.txt']
find_common_phrases_across_documents(document_files)
