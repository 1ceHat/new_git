class WordsFinder:

    def __init__(self, *files_name):
        self.file_names = list(files_name)

    def __remove_punctuation(self, string):
        symbols = [',', '.', '=', '!', '?', ';', ':', ' -', '\n', ' —']
        modified_string = string.lower()

        for symbol in symbols:
            modified_string = modified_string.replace(symbol, '')

        return modified_string

    def get_all_words(self):
        dict_words = {}
        for file_name in self.file_names:
            list_words = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = self.__remove_punctuation(line)
                    for word in line.split(' '):
                        if word == '':
                            continue
                        list_words.append(word)
            dict_words[file_name] = list_words
        return dict_words

    def find(self, word):
        dict_words = self.get_all_words()
        dict_founded_words = {}
        for file, words in dict_words.items():
            word_position = words.index(word.lower())
            if word_position > -1:
                dict_founded_words[file] = word_position + 1
        return dict_founded_words

    def count(self, word):
        dict_words = self.get_all_words()
        dict_founded_words = {}
        for file, words in dict_words.items():
            dict_founded_words[file] = words.count(word.lower())
        return dict_founded_words


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))