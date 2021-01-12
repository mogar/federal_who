
# Who wrote the Federalist Papers

Sharon Bertsch McGrayne's book on Bayesian history, The Theory That Would Not Die, has an entire chapter on how Bayesian data analysis was used to analyze The Federalist Papers. There are 85 of these papers, each written by one of three authors during the formation of the United States as a country. Most of these papers have a known author, but for 11 of the papers we aren't sure who exactly wrote it. Figuring out who wrote those papers (Hamilton or Madison) was apparently one of the first major achievements of academic Bayesian reasoning after WWII.

After reading in "Unix: a history and a memoir" that one of Kernighan's colleagues at Bell Labs was also interested in the Federalist Papers, I figured I'd get in on the act.

This repo is my experimentation on figuring out who wrote those questionable Federalist Papers. I'm not a data analyst by training, so I'm primarily using this as an excuse to learn more about how it's done. Back in the 60s it took a team of PhDs and students years to figure this stuff out. Here's hoping I can do better on my own by using modern tools and methods.

I'm going into this without looking up the results of prior investigations, but at the end I'll compare what I find to them.

See here for a good overview of the Federalist Papers history: https://priceonomics.com/how-statistics-solved-a-175-year-old-mystery-about/

# Pre-Reqs

* python3
* requests
* Beautiful Soup

# Usage

git clone ...
cd federal_who
./get_fedurls.py # get all the federalist papers from the Library of Congress
./federalyze.py # perform analysis and print results

# Analysis Methods and Results

Ideas:

* histogram of words, then nearest neighbor
* look up some methods