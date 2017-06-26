## Sentiment Analysis

ABSA (aspect-based sentiment analysis) is an automated system that uses machine learning and natural language processing to generate a digestable, human-understandable, and browsable summary of the opinions expressed in a corpus of social media data. ABSA's summary aims to provide the user with an at-a-glance understanding of an account's features (or *aspects*) as well as users' attitudes towards these features. 

ABSA generates a summary of this form in a completely automated fashion from the raw text (and metadata) of social media data. The items in blue at the top are the "aspects" that ABSA has extracted from the texts ("sex", "relationship", "democracy" etc.). These are the salient features of the account content that reviewers often comment on. 

## Social Media Scraping

Under the folder fb and Twitter are two parts of the separate programs that take user input of a facebook account page name or twitter handle/hashtag and return complete data for these accounts, and gave a dashboard of activity overview within the selected period for each account.

### Code Overview

If you are interested in exploring ABSA's code, the main directories of interest are `./classes`, which contains the code for ABSA's primary summary-generation pipeline, and `./modeling`, which contains the code for training/optimizing the machine learning models that currently power ABSA.  

### References

The problem of automatic review summarization has been addressed in academic literature. See especially: 

* Blair-Goldensohn et al.'s ["Building a Sentiment Summarizer for Local Service Reviews"](http://www.ryanmcd.com/papers/local_service_summ.pdf) (2008)
* Bing Liu's [Sentiment Analysis and Opinion Mining](http://www.cs.uic.edu/~liub/FBS/SentimentAnalysis-and-OpinionMining.pdf) (2012)
* Hu & Liu's [Mining and Summarizing Customer Reviews](http://users.cis.fiu.edu/~lli003/Sum/KDD/2004/p168-hu.pdf) (2004)
