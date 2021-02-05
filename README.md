# Nature Crawler

This script describes a customized crawler to 
collect information of articles published in 
"https://www.nature.com/nature/articles?type=article". 
Specifically, the title, the corresponding author, 
and the subjects of an article are of interest.

## Requirement

To run this file, the user is required to install python==3.8.5
and scrapy==2.4.1. A summary of the packages is added in the file
"requirement.txt"

## Instruction

1. In the root directory, a user can run the script
   `scrapy crawl nature -O URLs.json` in the shell to use crawler
   named "nature" and collect URLs of articles following a depth-
   first-search method. The user can stop the crawling by pressing 
   the key binding `ctrl + C`. 
   The crawled URLs will be stored in the "URLs.json" file.
   
2. Next, the user can run the script 
   `scrapy crawl article -O article.json` to collect information 
   of articles using the URLs stored in the previous step 
   and save the crawled results to the "article.json" file.

3. Last, the user can run the analysis script following 
   `python articleAnalysis.py` in the terminal to perform some
   toy analysis with the crawled data. 
