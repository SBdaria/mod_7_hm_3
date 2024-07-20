class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                list_of_words = []
                for line in file:
                    l = line.lower()
                    chars_to_remove = [',', '.', '=', '!', '?', ';', ':', '-']
                    for char in chars_to_remove:
                        l = l.replace(char, '')
                    line_of_words = l.split()
                    for k in line_of_words:
                        list_of_words.append(k)
                all_words[i] = list_of_words
        return all_words


    def find(self, word):
        pos_of_word = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            for i in range(len(words)):
                if words[i].lower() == word.lower():
                    pos_of_word[name] = i + 1
                    break
        return pos_of_word

    def count(self, word):
        count_of_word = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = 0
            for i in range(len(words)):
                if words[i].lower() == word.lower():
                    count += 1
            count_of_word[name] = count
        return count_of_word

if __name__ == '__main__':
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))