# Campus Seach Engine

## About
Building a local query-based **search engine** to assist searching and indexing over local area networks. Custom searching and results display.
* **Crawling**: Using Scrapy, BeautifulSoup to scrap Internet and Intranet websites of IIT Guwahati relevant to the campus and preparing dataset to be indexed
* **Indexing**: Using Whoosh to index the scraped data, based on schemas defined namely TITLE, PATH and CONTENT
* **Ranking**: Page ranking algorithms to be implemented to implement relevant search results

## Dependencies
* Scrapy
* BeautifulSoup
* Whoosh
* Django

## Code Files
* datablogger.py: running the scrapy script for scraping www.iitg.ac.in
* whoosh.py: indexing the scraped data according to schemas created
* search.py: running searches on the indexed data

#### Project Deployment
Django based back-end used to deploy the Search engine in the form of a website with comaptible search results on local IITG websites. Project is currently being developed under Students' Web Committee (SWC) IIT Guwahati and has a expansive scope.
