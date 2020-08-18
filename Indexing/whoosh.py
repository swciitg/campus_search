import pandas as pd
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
import string
import sys
import urllib.request
import socket, urllib3

# Makedir
import os, os.path
if not os.path.exists("schema"):
    os.mkdir("schema")

from html.parser import HTMLParser
from whoosh.qparser import QueryParser

df=pd.read_csv('dataset.csv')


ana = analysis.StemmingAnalyzer()
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
ix = create_in("schema", schema)

def indexing():
    timeout = 3
    socket.setdefaulttimeout(timeout)
    

    writer = ix.writer()
    count = 0

    # with open('Final_Links/final_links.txt') as fp, open('data/content_data/mytemp/content.txt', 'w+') as f:
        # for line in fp:
    for (columnName, columnData) in df['url_to'].iteritems():
        count += 1
        url = columnData
        try:
            response = urllib.request.urlopen(url)
            html_content = response.read()
            soup = BeautifulSoup(html_content)
            content_text = soup.get_text()
            print(content_text)

            # f.write(html_content)

            writer.add_document(title=url, path=url,
                                content=content_text)
            # writer.add_document(title=url, path=url,
            #                     content=url)
        except Exception as e:
            print(e)
            print ("Caught exception e at " + url)
        print (str(count) + " in " + " URL:" + url)

    writer.commit()
    print ("Indexing Completed !")


indexing()
