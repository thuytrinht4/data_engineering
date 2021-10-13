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