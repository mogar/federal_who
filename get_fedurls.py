#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def scrape_federal_page(url):
    '''
    Fetch the url and parse it for Federalist Papers.
    Pages are assumed to match LoC format as of 2021 01 01.
    Each Federalist Paper at the URL will be saved to it's own file in a ./papers directory.
    '''
    # fetch
    page = requests.get(url)
    
    # papers are in <div id="s-lg-box-####" class="s-lib-box s-lib-box-std">
    # Table of Contents is also in that div class
    # paper title are in <h2 class="s-lib-box-title">
    # paper contents are in <div id="s-lg-content-#######" class="  clearfix">
    # paper contents are the first s-lg-content div after the title
    
    # TODO: parse, write to files
    soup = BeautifulSoup(page.content, 'html.parser')
    papers = results.find_all('section', class_='s-lib-box s-lib-box-std')
    
    files = []
    for paper in papers:
        title = paper.find('section', class_='s-lib-box-title').text
        if title == "Table of Contents":
            continue
        title.replace(" ", "_")
        title.replace(".", "")
        fname = "papers/" + title + ".html"
        f = open(fname, "w")
        f.write(paper)
        f.close()
        files.append(fname)
    
    return files
    
def scrape_all_federal_pages():
    '''
    Scrape all of the Federalist Papers from the Library of Congress.
    Return a list of the files created.
    '''
    
    num_federalist_papers = 85
    fedurls = ["https://guides.loc.gov/federalist-papers/text-1-10",
                "https://guides.loc.gov/federalist-papers/text-11-20",
                "https://guides.loc.gov/federalist-papers/text-21-30",
                "https://guides.loc.gov/federalist-papers/text-31-40",
                "https://guides.loc.gov/federalist-papers/text-41-50",
                "https://guides.loc.gov/federalist-papers/text-51-60",
                "https://guides.loc.gov/federalist-papers/text-61-70",
                "https://guides.loc.gov/federalist-papers/text-71-80",
                "https://guides.loc.gov/federalist-papers/text-81-85"]

    files = []
    for url in fedurls:
        files.extend(scrape_federal_page(url))
    
    return files
    
if __name__ == "__main__":
    files = scrape_all_federal_pages()
    print(files)