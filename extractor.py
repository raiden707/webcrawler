import requests
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords  

stopwords=set(stopwords.words('english'))

url = "https://realpython.com/"

pTagList = []

def hTagExtraction(url):
    """
    Return all headings from a given URL H1 - H6
    :return:
    """
    html = requests.get(url).content

    unicode_str = html.decode("utf8")
    encoded_str = unicode_str.encode("ascii", 'ignore')
    soup = BeautifulSoup(encoded_str, "html.parser")
        
    heading_list = [soup.find_all(header) for header in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] ]
    
    [print(headings) for headings in heading_list if len(headings) != 0]

    


def pTagExtraction(url):
    """
    <p> text extraction
    :return:
    """
    html = requests.get(url).content

    unicode_str = html.decode("utf8")
    encoded_str = unicode_str.encode("ascii", 'ignore')
    soup = BeautifulSoup(encoded_str, "html.parser")

    paragraph = soup.find_all("p")

    paraCount = 0
    for tag in paragraph:
        if tag.text != "":
            paraCount += 1
            pTagList.append(tag.text.lower())

    word_count=0
    for i in pTagList:
        for word in i:
            word_count+=1
    return word_count

def remove_stopwords(pTagList):
    """
    remove stopwords
    """

    output_array=[]
    for sentence in pTagList:
        temp_list=[]
        for word in sentence.split():
            if word.lower() not in stopwords:
                temp_list.append(word)
        output_array.append(' '.join(temp_list))

    word_count = 0
    for i in output_array:
        for x in i:
            word_count+=1
    return(word_count)

def stopWordCount():
    """
    Prints the number of stopwords in a file
    """
    
    print("Number of stopwords removed:", pTagExtraction(url) - remove_stopwords(pTagList))

(hTagExtraction(url))