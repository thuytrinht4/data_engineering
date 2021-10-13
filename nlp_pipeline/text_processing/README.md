# Text Processing
## Why Do We Need to Process Text?
+ **Extracting plain text**: Textual data can come from a wide variety of sources: the web, PDFs, word documents, speech 
recognition systems, book scans, etc. Your goal is to extract plain text that is free of any source specific markup or 
constructs that are not relevant to your task.
+ **Reducing complexity**: Some features of our language like capitalization, punctuation, and common words such as 
a, of, and the, often help provide structure, but don't add much meaning. Sometimes it's best to remove them if that 
helps reduce the complexity of the procedures you want to apply later.

## What Text Processing steps?
We'll prepare text data from different sources with the following text processing steps:

1. [Cleaning](#Cleaning-to-remove-irrelevant-items)
2. [Normalization](#Normalization)
3. [Tokenization](#Tokenization)
4. [Stop words removal](#Stop-words-removal)
5. [Part-of-Speech tagging and Named Entity Recognition](#Part-of-Speech-and-Name-Entity-Recognition)
6. [Stemming and Lemmatization](#Stemming and Lemmatization)

After performing these steps, your text will capture the essence of what was being conveyed in a form that is easier 
to work with.

### Cleaning to remove irrelevant items
In this project we tackle an example of cleaning text data from a popular source - the web. The process will remove 
irrelevant items such as HTML tags. We'll use helpful tools for cleaning including the requests library, regular 
expressions, and Beautiful Soup.

Documentation for Python Libraries:
   + [Requests](https://docs.python-requests.org/en/master/user/quickstart/#make-a-request)
   + [Regular Expressions](https://docs.python.org/3/library/re.html)
   + [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Normalization
Human language, in this case, the English language, is very complex will all its variations and bells and whistles. 
Normalization is process to reduce some of those complexities of human language by:
   + Converting all text to lowercase
   + Removing punctuation

### Tokenization
Token is a fancy term for a symbol. Usually one token holds some meaning and is not typically split up any further.
In case of natural language processing for English, the tokens are usually individual words. So tokenization is simply 
splitting each sentence into a sequence of words.

There are two main ways to tokenization:
1. Use split() method include in Python built-in functionality
2. Use libraries specially built for NLP task like NLTK (Natural language toolkit)

split() is simply split words base on space and punctuation while NLTK provides more advanced tokenization 
techniques (e.g <Dr.Who> will be split as 2 tokens <Dr.> and <Who> instead of 3 separated tokens <Dr>, <.> and <Who>).

NLTK also provide options to split text into others levels than words level, like sentence-based or regular expression 
based. Check other features of NLTK in [here](https://www.nltk.org/)

### Stop words removal
Stop words are uninformative words like ***in, the, at*** that do not add a lot of meaning to a sentence. They are
typically very commonly occurring words, and we may want to remove them to reduce the size of the vocabulary, and hence 
the complexity of later procedures. 

Stop words is based on a specific corpus or collection of text. Different corpora may have different stop words. Also, 
a word may a stop word in one application, but a useful word in another. 

To remove stop words, we can use: stopwords dictionary from language library like NLTK and Python list comprehension 
with a filtering condition.

### Part-of-Speech and Name Entity Recognition
**Part-of-Speech** (POS) tagging is a process which refers to categorizing words in a text in correspondence with a 
particular part of speech, based on both its definition and its context like Noun, Verb, Adverbs, etc. Identifying how 
words are being used in a sentence can help us better understand what is being said. It can also point out relationships 
between words and recognize cross references. 

POS tagging is very easy with NLTK library using the `pos_tag()` method.

**Named Entities** are typically noun phrases that refer to some specific object, person, or place. Name Entity 
Recognition (NER) is often used to index and search for news articles. for example, on companies of interest.  

NER can be done with NLTK using the `ne_chunk()` method

### Stemming and Lemmatization
**Stemming and Lemmatization** is the process to convert a word or token to its dictionary forms, in order to further 
simplify text data. This helps reduce the complexity while maintaining the essence of meaning that is carried by words. 

**Stemming** is a process of reducing a word to its stem or root form. For instance, <branching>, <branched> and <branches> 
will be reduced to <branch>. Stemming is meant to be a fast and crude operation, carried out by applying very simple 
search and replace style rules. For example, the suffixes "ing" and "ed" can be dropped off, "ies" can be replaced by 
"y", etc. This may result in a stem word that is not complete, but that's okay, as long as all form of that word are 
reduced to the same stem. Thus, capturing the common underlying idea.

There are a few methods for stemming in NLTK, like `PorterStemmer()`, `SnowballStemmer()`, and other language-specific 
stemmers.

**Lemmatization** is another technique used to reduce words to a normalized form, but in this case, the transformation 
actually uses a dictionary to map different variants of a word back to its root. With this approach, we are able to 
reduce non-trival inflections such as `is`, `was` and `were` back to the root `be`. 

The default lemmatizer in NLTK, the `WordNetLemmatizer()`, uses the Wordnet database to reduce words to the root form.
A lemmatizer needs to know or make an assumption about the Part-of-speech for each word it's trying to transform. 
Without other specification, `WordNetLemmatizer()` defaults to nouns. We can override the default by specifying the PoS 
parameter. 

**Stemming vs Lemmatization** they both try to normalize text into its simple form of word. However:
   + Stemming sometimes result in stems that are not complete words in English. But Stemming does not need a dictionary, 
hence, less memory and storage required to operate.
   + Lemmatization used a dictionary to transform, so the final form is always a meaningful word. But we need to 
create/download and load this dictionary to operate Lemmatization, which require more memory and storage.

So, depending on the constraints we have, stemming maybe a less memory intensive option for us to consider. Under no 
constraints, it is also common to do lemmatization first, then stemming.








