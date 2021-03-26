import time
import requests
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize 


stopwords=set(stopwords.words('english'))


url = "https://www.thehometeam.ae"

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

    headings = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    h1 = soup.find_all(headings[0])
    h2 = soup.find_all(headings[1])
    h3 = soup.find_all(headings[2])
    h4 = soup.find_all(headings[3])
    h5 = soup.find_all(headings[4])
    h6 = soup.find_all(headings[5])

    y = [re.sub(r'<.+?>', r'', str(a)) for a in (h1, h2, h3, h4, h5, h6)]

    head = 1
    for item in y:
        if item != '[]':
            print('H',head,'==>',item[1:-1],)
            head += 1


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
            #print("Paragraph " + str(paraCount) + " " + tag.text)
            pTagList.append(tag.text.lower())

    word_count=0
    for i in pTagList:
        for word in i:
            word_count+=1
    return(word_count)




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

print("Amount of stopwords removed:", pTagExtraction(url) - remove_stopwords(pTagList))