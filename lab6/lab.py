"""6.009 Lab 6 -- Autocomplete"""
# NO ADDITIONAL IMPORTS!
from text_tokenize import tokenize_sentences
import pdb

class Trie:
    def __init__(self):
        """
        Initialize an empty trie.
        """
        self.value = None
        self.children = {}
        self.type = type(None)

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.  If the given key is not in
        the trie, raise a KeyError.  If the given key is of the wrong type,
        raise a TypeError.
        """
        if type(key) != str and type(key) != tuple:
            raise TypeError
        if not isinstance(key, self.type):
            raise TypeError
        
        current_trie = self
        for i in range(len(key)):
            x = key[i:i+1]

            if x not in current_trie.children:
                raise KeyError
            
            current_trie = current_trie.children[x] #update to new trie

        if current_trie.value == None:
            raise KeyError
        return current_trie.value

    def __setitem__(self, key, value):
        """
        Add a key with the given value to the trie, or reassign the associated
        value if it is already present in the trie.  Assume that key is an
        immutable ordered sequence.  Raise a TypeError if the given key is of
        the wrong type.
        """
        if type(key) != str and type(key) != tuple:
            raise TypeError
        current_trie = self
        if self.type == type(None):
            self.type = type(key)
        if self.type != type(key):
            raise TypeError
        for i in range(len(key)):
            x = key[i:i+1]
            if x not in current_trie.children: #update new trie completely
                new_trie = Trie()
                new_trie.type = type(x)
                current_trie.children[x] = new_trie
                current_trie = new_trie
                continue

            current_trie = current_trie.children[x]
                
                
        current_trie.value = value 
    
    def __delitem__(self, key):
        """
        Delete the given key from the trie if it exists.
        """
        self.__setitem__(key, None)

    def __contains__(self, key):
        """
        Return True if key is in the trie and has a value, return False otherwise.
        """
        try:
            self.__getitem__(key)
            return(True)
        except:
            return(False)
        
    def __iter__(self):
        """
        Generator of (key, value) pairs for all keys/values in this trie and
        its children.  Must be a generator or iterator!
        """
        if self.value != None:
            yield((self.type(), self.value))

        for i in self.children:

            yield from ((i+key, val) for key, val in self.children[i])


def make_word_trie(text):
    """
    Given a piece of text as a single string, return a Trie whose keys are the
    words in the text, and whose values are the number of times the associated
    word appears in the text
    """
    sentences = tokenize_sentences(text)
    counter = Trie()
    for sentence in sentences:
        words = sentence.split() #each string into a list of words
        for word in words:
            if word in counter:
                counter[word] += 1
            if word not in counter:
                counter[word] = 1
    return counter


def make_phrase_trie(text):
    """
    Given a piece of text as a single string, return a Trie whose keys are the
    sentences in the text (as tuples of individual words) and whose values are
    the number of times the associated sentence appears in the text.
    """
    sentences = tokenize_sentences(text)
    counter = Trie()
    for sentence in sentences:
        words = sentence.split() #each sentence converted to list of words
        phrase = tuple(words) #made each list of words into tuple
        if phrase in counter:
            counter[phrase] += 1
        if phrase not in counter:
            counter[phrase] = 1
    return counter


def autocomplete(trie, prefix, max_count=None):
    """
    Return the list of the most-frequently occurring elements that start with
    the given prefix.  Include only the top max_count elements if max_count is
    specified, otherwise return all.

    Raise a TypeError if the given prefix is of an inappropriate type for the
    trie.
    """

    if type(prefix) != trie.type:
        raise TypeError
    
    new_trie = trie
    words_frequency = []
    try:
        if type(prefix) == tuple:
            for elem in prefix:
                new_trie = new_trie.children[(elem,)]
        else:
            for elem in prefix:
                new_trie = new_trie.children[elem] #if no children can be found it means prefix is not in tree
    except:
        return[]
    
    # if new_trie.value !=None:
    #     words_frequency.append((prefix, new_trie.value))
    for keyval in new_trie:
        #print(keyval)
        words_frequency.append((prefix + keyval[0], keyval[1]))

    words_frequency.sort(key = lambda x: x[1], reverse=True) #sorts possible words in descending order of frequency
    if max_count != None:
       return [i[0] for i in (words_frequency[:max_count])] #takes the first max_count words
    else:
        return [i[0] for i in words_frequency]
    

def single_del(word, trie):
    ans = []
    for i in range(len(word)):
        #pdb.set_trace()
        word2 = word[0:i] + word[i+1:]

        if word2 in trie:
            ans.append((word2, trie[word2]))
    return(ans)

def transpose(word, trie):
    ans = []
    for i in range(len(word)-1):
        word2 = word[0:i] + word[i+1] + word[i] + word[i+2:]
        if word2 in trie:
            ans.append((word2, trie[word2]))
    return(ans)
def single_insert(word, trie, alphabet):
    ans = []
    for letter in alphabet:

        word4 = letter + word
        if word4 in trie:
            ans.append((word4, trie[word4])) #inserts at beginning

        for i in range(len(word)):
            if i == 0:
                continue
            #if letter == 'o':
                #pdb.set_trace()
            word2 = word[0:i] + letter + word[i:] #inserts everywhere else
            if word2 in trie:
                ans.append((word2, trie[word2]))
    return(ans)
def replace(word, trie, alphabet):
    ans = []
    for letter in alphabet:
        for i in range(len(word)):
            word2 = word[0:i] + letter + word[i+1:]
            if word2 in trie:
                ans.append((word2, trie[word2]))
    return(ans)


def autocorrect(trie, prefix, max_count=None):
    """
    Return the list of the most-frequent words that start with prefix or that
    are valid words that differ from prefix by a small edit.  Include up to
    max_count elements from the autocompletion.  If autocompletion produces
    fewer than max_count elements, include the most-frequently-occurring valid
    edits of the given word as well, up to max_count total elements.

    Do not use a brute-force method that involves generating/looping over
    all the words in the trie.
    """
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    suggestions = autocomplete(trie, prefix, max_count)
    if max_count == 0:
        return []
    if max_count != None:
        remaining = max_count- len(suggestions)
    if max_count == None or remaining >0:
        valid_edits = single_del(prefix, trie) + transpose(prefix, trie) + single_insert(prefix, trie, alphabet) + replace(prefix, trie, alphabet)
        valid_edits = list(set(valid_edits))
        valid_edits.sort(key = lambda x: x[1], reverse=True)
        if max_count == None:
            ans = [i[0] for i in valid_edits] + suggestions
            ans = list(set(ans))
        else:
            add = [i[0] for i in (valid_edits[:remaining])]
            ans = suggestions + add
        return ans
    else:
        return(suggestions)

def word_filter(trie, pattern, words= None, letter = None):
    """
    Return list of (word, freq) for all words in trie that match pattern.
    pattern is a string, interpreted as explained below:
         * matches any sequence of zero or more characters,
         ? matches any single character,
         otherwise char in pattern char must equal char in word.

    Do not use a brute-force method that involves generating/looping over
    all the words in the trie.
    """
    next_char = pattern[0:1]
    avails = [a for a in trie.children]

    if words == None:
        words = set()
    if letter == None:
        letter = ''  
    if pattern == '':
        return words
    if trie.children == {}:
        return words
    if letter in trie:
        words.add(letter)

    if trie.value != None:
        words.append((letter, trie.value))


    if next_char == '?':
        new_letter= avails.pop()
        letter = letter + new_letter
        continued = word_filter(trie.children[new_letter], pattern[1:], words, letter)
    if next_char == '*':
        accept_pattern = '?*' + pattern[1:]
        accepted = word_filter(trie.children, accept_pattern, words, letter)
        ignore = pattern[1:]
        ignored = word_filter(trie.children, ignore, words, letter)





# you can include test cases of your own in the block below.
if __name__ == '__main__':
    pass
