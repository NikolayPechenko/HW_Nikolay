class WordsFinder:

    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                linel = []
                for line in file:
                    line = line.lower()
                    for j in punctuation:
                        line = line.replace(j, '')
                    line = line.split()
                    linel.extend(line)
                all_words[i] = linel
        return all_words

    def find(self, word):
        finds = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                finds[k] = v.index(word.lower()) + 1
        return finds

    def count(self, word):
        counts = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                counts[k] = v.count(word.lower())
        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
