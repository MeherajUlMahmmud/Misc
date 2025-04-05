import re


def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)
    return words


def load_keywords(filename):
    with open(filename, 'r') as file:
        content = file.read()
        content = content.replace("'", "")
        content = content.replace(",", "")
        content = content.split()
    return content


def keyword_frequency_count(documents, keywords):
    keyword_count = {}
    for keyword in keywords:
        keyword = keyword.lower()
        keyword_count[keyword] = 0

    for document in documents:
        words = read_file(document)
        for word in words:
            if word in keyword_count:
                keyword_count[word] += 1

    return keyword_count


documents = ['doc1.txt', 'doc2.txt']
keywords = load_keywords('keywords.txt')

result = keyword_frequency_count(documents, keywords)

print("Keyword Frequency Count:")
for keyword in result:
    count = result[keyword]
    print("'" + keyword + "' occurs " + str(count) + " times.")
