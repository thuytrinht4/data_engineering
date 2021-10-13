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

1. Cleaning to remove irrelevant items, such as HTML tags
2. Normalizing by converting to all lowercase and removing punctuation
3. Splitting text into words or tokens
4. Removing words that are too common, also known as stop words
5. Identifying different parts of speech and named entities
6. Converting words into their dictionary forms, using stemming and lemmatization

After performing these steps, your text will capture the essence of what was being conveyed in a form that is easier 
to work with.

### Cleaning
In this project we tackle an example of cleaning text data from a popular source - the web. We'll use helpful 
tools for cleaning, including the requests library, regular expressions, and Beautiful Soup.

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

