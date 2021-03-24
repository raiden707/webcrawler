# Basic webcrawler made in python using BeautifulSoup

It has the following functions:

1. hTagExtraction
This finds all H1 through H6 tags in a given site and appends them to a list.

2. pTagExtraction
This finds all paragraph tags in a given site and then appends them to a list

3. remove_stopwords
This function removes all the stopwords within the pTagList array. More information on stopwords can be found here: https://www.nltk.org/book/ch02.html

# Usage

1. Install the prerequisites

```
pip install -r requirements.txt 
```
2. Add your URL to the url variable
3. Call the method you would like to invoke

**You need to run either the H tag extractor or the P tag extractor before the stopword removal functions otherwise the function will try and find stopwords within an empty list.**
