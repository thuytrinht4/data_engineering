# Natural Language Processing Pipeline
Natural Language Processing pipeline is a process that start with raw text in whatever form it is available, process it, 
extract relevant features, and build models to accomplish various NLP tasks. 

As in a data engineering process, we need to know how these different stages in the pipeline depend on each other; 
understand how to make design decisions, how to choose existing libraries, and tools to perform each step.

# How NLP Pipelines Work
The 3 stages of an NLP pipeline are: Text Processing > Feature Extraction > Modeling.
   + **Text Processing**: Take raw input text, clean it, normalize it, and convert it into a form that is suitable for 
feature extraction.
   + **Feature Extraction**: Extract and produce feature representations that are appropriate for the type of NLP task you 
are trying to accomplish and the type of model you are planning to use.
   + **Modeling**: Design a statistical or machine learning model, fit its parameters to training data, use an optimization 
procedure, and then use it to make predictions about unseen data.

This process isn't always linear and may require additional steps. Let's say, you spend some time implementing text 
processing functions, then make some simple feature extractors, and then design a baseline statistical model. But then,
maybe you are not happy with the results. So you go back and rethink what features you need, and that in turn, can make
you change your processing routines. Therefore, the above three stages is a very simplified view of NLP pipeline.

# Project Outlines
1. Text Processing 
   + Cleaning 
   + Normalization 
   + Tokenization 
   + Stop Word Removal 
   + Part of Speech Tagging 
   + Named Entity Recognition 
   + Stemming and Lemmatization

2. Feature Extraction 
   + Bag of Words
   + TF-IDF
   + Word Embeddings

3. Modeling