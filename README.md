# Scrapping-customer-reviews-from-playstore

The basic idea of this project is scrapping customer reviews from playstore, the whole project is developed in Jupyter notebook.

Packages used - Google-play-scraper is a module that helps in scraping App data from the Google Play store by providing methods that make our job easy.

Pandas is also used, alongside with requests.

Just copy paste the URL of the review page that we want to scrape, google-play-scraper will allow us to read the review of the app and that can be normalized in a data frame for furthur analysis.

From the code we can see the data frame, some analysis and visualization of the customer reviews that we have scraped.

There's a part 2 for this project as we are only scraping the customer reviews, we can use that content for some analysis, that part wll be covered in the repo - 

For a headsup, I have covered some part in this repo itself, now we will be using the most useful NLTKpackage, stopwords and corpus.

Use the URL in the code so that we can use the stop words to remove the unwanted words and keep the important ones for the analysis, later we use word tokenizer to make our work simple.

