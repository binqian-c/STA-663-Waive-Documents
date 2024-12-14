# 
# Final Project
#
# If you worked with a partner, put their contact info below:
# partner's name: Binqian Chai
# partner's email: bqchai@bu.edu

# Part IV    #part4-1
import math

def compare_dictionaries(d1, d2):
    """ take two feature dictionaries d1 and d2 as inputs
        and compute and return their log similarity score.
    """
    score = 0
    total = 0
    
    for a in d1:
        total += d1[a]
    
    for b in d2:
        
        if b in d1:
            score += math.log( d1[b]/total ) * d2[b]
        else:
            score += math.log( 0.5/total ) * d2[b] 
            
    return score

# Part I

# part 1-3 helper function
def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a list containing 
        the words in txt after it has been “cleaned”
    """
    txt = txt.lower()
    
    for symbol in """.,?"'!;:""":
        txt = txt.replace( symbol , '')
    
    txt = txt.split()
    return txt

#Part III 

# part 3-2 helper function
def stem(s):
    """ accepts a string as a parameter
        The function should then return the stem of s. 
        The stem of a word is the root part of the word, which excludes any 
        prefixes and suffixes.
    """
    
    if s[-1] == 'y':
        s = s[:-1] + 'i'
        return s
    
    elif s[-1] == 'e':
        s = s[:-1] 
        return s
    
    elif s[-3:] == 'ies':
        s = s[:-2] 
        return s
        
    elif s[-3:] == 'ing':
        if len(s) < 6:
            return s
        elif s[-4] == s[-5]:
            if s[-4] in 'flsz':
                s = s[:-3]
                return s
            else:
                s = s[:-4]
                return s
        else:
            s = s[:-3]
            return s
        
    elif s[-1] == 's':
        s = s[:-1]
        rest = stem(s)
        return rest
              
    elif s[-2:] == 'er':
        if len(s) < 5:
            return s
        elif s[-3:] == 'ier':
            s = s[:-2]
            return s
        elif s[-3] == s[-4]:
            if s[-3] in 'flsz':
                s = s[:-2]
                return s
            else:
                s = s[:-3] 
                return s
        else:
            s = s[:-2]
            return s

    elif s[-2:] == 'ed':
        if len(s) < 5:
            return s
        elif s[-3:] == 'ied':
            s = s[:-2]
            return s
        elif s[-3] == s[-4]:
            if s[-3] in 'flsz':
                s = s[:-2]
                return s
            else:
                s = s[:-3]
                return s
        else:
            s = s[:-2]
            return s
        
    else:
        return s
        

class TextModel:
    """ a class that serves as a blueprint for objects that model a body of text 
        (i.e., a collection of one or more text documents), and write each of 
        the feature dictionaries to a different file in order to save and 
        retrieve a text model
    """
    
    # part 1-1
    def __init__(self, model_name):
        """ constructs a new TextModel object by accepting a string model_name 
            as a parameter and initializing six attributes
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        
        #Part III #1
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuations = {}      #another feature: count the frequencies of different types of punctuation
        

    # part 1-2
    def __repr__(self):
        """ returns a string that includes the name of the model as well as 
            the sizes of the dictionaries for each feature of the text.
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        
        #Part III #4
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations))   
        
        return s


    # part 1-4
    def add_string(self, s):
        """ analyzes the string txt and adds its pieces to all of the dictionaries 
            in this text model.
        """
        #Part III #3 sentence_lengths
        sentence_list = s        
        sentence_list = s.replace('?', '.').replace('!', '.').split()
        word_count = 0

        for i in sentence_list:
            if i[-1] != '.':
                word_count += 1
        
            else:
                word_count += 1
                if word_count not in self.sentence_lengths:
                    self.sentence_lengths[word_count] = 1
                else:
                    self.sentence_lengths[word_count] += 1
                word_count = 0
        
        #another feature: punctuations
        punctuation_list = s

        punctuation_list = s.split()
        punctuation_count = 0
        word_count = 0

        for i in punctuation_list:
            if i[-1] not in """.,)]}?"'!;:-""":
                word_count += 1
    
            else:
                word_count += 1
                punctuation_count += 1
        
                if i[-1] not in self.punctuations:
                    self.punctuations[i[-1]] = 1
                else:
                    self.punctuations[i[-1]] += 1
        
                punctuation_count = 0
        
        # part 1-4
        word_list = clean_text(s)
        
        for w in word_list:
            
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1 
            else:
                self.word_lengths[len(w)] += 1 
                
                
        #Part III #3
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
            
        
    # part 1-5
    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        
        self.add_string(text)

   
# Part II
    
    #part 2-1
    def save_model(self):
        """ saves the TextModel object self by writing its various feature 
            dictionaries to files
        """
        f1 = open(str(self.name) + '_' + 'words', 'w')
        f1.write(str(self.words))
        f1.close()
        
        f2 = open(str(self.name)+ '_' + 'word_lengths', 'w')
        f2.write(str(self.word_lengths))
        f2.close()
        
        #Part III #3
        f3 = open(str(self.name)+ '_' + 'stems', 'w')
        f3.write(str(self.stems))
        f3.close()
    
        f4 = open(str(self.name)+ '_' + 'sentence_lengths', 'w')
        f4.write(str(self.sentence_lengths))
        f4.close()
        
        f5 = open(str(self.name)+ '_' + 'punctuations', 'w')
        f5.write(str(self.punctuations))
        f5.close()
        
    
    #part 2-2
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object from 
            their files and assigns them to the attributes of the called TextModel
        """
        f1 = open(str(self.name) + '_' + 'words', 'r')
        f1_str = f1.read()
        f1.close()
        self.words = dict(eval(f1_str))
        
        f2 = open(str(self.name) + '_' + 'word_lengths', 'r')
        f2_str = f2.read()
        f2.close()
        self.word_lengths = dict(eval(f2_str))
        
        #Part III #3
        f3 = open(str(self.name) + '_' + 'stems', 'r')
        f3_str = f3.read()
        f3.close()
        self.stems = dict(eval(f3_str))
        
        f4 = open(str(self.name) + '_' + 'sentence_lengths', 'r')
        f4_str = f4.read()
        f4.close()
        self.sentence_lengths = dict(eval(f4_str))
        
        f5 = open(str(self.name) + '_' + 'punctuations', 'r')
        f5_str = f5.read()
        f5.close()
        self.punctuations = dict(eval(f5_str))
        
# Part IV   

    #part4-2
    def similarity_scores(self, other):
        """ computes and returns a list of log similarity scores measuring the 
            similarity of self and other.
        """
        word_score = [ compare_dictionaries(other.words, self.words) ]
        word_lengths_score = [ compare_dictionaries(other.word_lengths,self.word_lengths) ]
        stems_score = [ compare_dictionaries(other.stems,self.stems) ]
        sentence_lengths_score = [compare_dictionaries(other.sentence_lengths,self.sentence_lengths)]
        punctuations_score = [compare_dictionaries(other.punctuations,self.punctuations)]
        
        score_list = word_score + word_lengths_score + stems_score + sentence_lengths_score + punctuations_score
        return score_list
    
    #part4-3
    def classify(self, source1, source2):
        """ compares the called TextModel object (self) to two other “source” 
            TextModel objects (source1 and source2) and determines which of 
            these other TextModels is the more likely source of the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print ( 'scores for', source1.name + ':', scores1 )
        print ( 'scores for', source2.name + ':', scores2 )
        
        weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] + 6*scores1[3] + 8*scores1[4] 
        weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2] + 6*scores2[3] + 8*scores2[4] 

        if weighted_sum1 > weighted_sum2:
            print( self.name, 'is more likely to have come from', source1.name )
        
        elif weighted_sum1 == weighted_sum2:
            print( self.name, 'are equally likely to have come from', source1.name, 'and', source2.name )
        
        else:
            print( self.name, 'is more likely to have come from', source2.name )
        
    
# Sample
def sample_file_write(filename):
    """ A function that demonstrates how to write a Python dictionary to an 
        easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.

def sample_file_read(filename):
    """ A function that demonstrates how to read a Python dictionary from a 
        file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)


def run_tests():
    """ choose several bodies of text and compute similarity scores """
    source1 = TextModel('J.K.Rowling')
    source1.add_file('J.K.RowlingModel.txt')

    source2 = TextModel('Shakespeare')
    source2.add_file('Shakespearemodel.txt')

    new1 = TextModel('J.K.Rowling_cut')
    new1.add_file('J.K.Rowlingcut.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('Shakespeare_cut')
    new2.add_file('Shakespearecut.txt')
    new2.classify(source1,source2)
    
    new3 = TextModel('Golden Voice')
    new3.add_file('Goldenvoice.txt')
    new3.classify(source1,source2)
    
    new4 = TextModel('WR120')
    new4.add_file('wr120imitation.txt')
    new4.classify(source1,source2)
    
