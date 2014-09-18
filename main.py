import time

class LongestWord:

    '''
    Class for finding the longest word in file compose of other words
    present in file.
    '''

    def __init__(self):
        self.count = 0
        self.word_dict = {}
        self.longest_word = ''
        self.second_longest_word = ''
        self.longest_word_len = 0
        self.memoized_dict = {}

    def __word_break(self, word, first_call=False):
        '''
        Use dynamic programing to break the words
        '''

        if word in self.word_dict and not first_call:
            return True
        if word in self.memoized_dict:
            return True

        for i in range(1, len(word)):
            if word[0:i] in self.word_dict:
                suffix_str = word[i:]
                if self.__word_break(suffix_str):
                    self.memoized_dict[word] = None
                    return True
        return False

    def find_composite_word(self):
        '''
        Find the composite in the files.
        '''
        for word in self.word_dict:
            if self.__word_break(word, True):
                self.__value_update(word)

    def __value_update(self, word):
        '''
        Update values.
        '''
        self.count += 1
        if len(word) > self.longest_word_len:
            self.longest_word, self.second_longest_word = word, self.longest_word
            self.longest_word_len = len(self.longest_word)
        elif len(word) > len(self.second_longest_word):
            self.second_longest_word = word
        else:
            pass

    def read_file(self, file_path):
        '''
        Read the word from the file line by line and creates dictionary.
        '''
        with open(file_path, 'r') as input_file:
            for word in input_file:
                word = word.rstrip('\n')
                self.word_dict[word] = None

    def display(self):
        print('Longest Word , Length : ', self.longest_word,',', 
                                                        self.longest_word_len)
        print('Second Longest Word: ', self.second_longest_word)
        print('Total Composite Word Count: ', self.count)


if __name__ == '__main__':
    word_class = LongestWord()
    start = time.clock()
    word_class.read_file('data/wordsforproblem.txt')
    word_class.find_composite_word()
    word_class.display()
    print('Elapsed Time(secs):  {0:.3f}'.format(time.clock() - start))
