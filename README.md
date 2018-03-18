# HINT_RASberry
Product Built during Hack in The North 

## Idea – Hack in the North 3.0 - KnowMedy

**Abstract** : Using disease profiles which contains severity and symptoms ,our code first predicts the possible disease the person can have. Now, we help the user by providing useful blogs and resources like medications, doctors to consult, home remedies, precautions, etc from all over the web. We will be having user accounts, and thus the user will upvote and downvote the resources based on his/her experience. Also, if a disease is encountered for the first time, the search algorithm is used for that time and the data is stored for any further requests. 
>The unique selling point of our product is the prediction of disease on the basis of severity, which makes it all the more appealing. 


**Workflow** : The portal will open up to a login page. Once the user logs in, he/she will see search bars, where one can add symptoms and their respective severity. Once the form is submitted, the data goes to the back end to get predicted by the trained model that we have built. The database used for training the model has been taken from the source of University of Columbia. After the prediction finishes, we are blessed with the name of the disease the user has (as per our model). Now, taking it as an input and doing metasearches on different popular websites like [www.nhp.gov.in] , [www.webmd.uk], we scrape relevant data as mentioned in the abstract above and showcase it to the user. Now, the data will be represented in form of cards with upvote and downvote buttons. As we are promising a multi-user platform here, every user can upvote or downvote a particular resource related to a particular disease and the data then will be showcased in the sorted order of 'upvotes-downvotes" accordingly. In this way, we are trying to create a platform where you can share your likes and dislikes about a particular medical information and can help other users to make a choice.


**Technologies used** : 
- Machine Learning - NLP,KNN, Decision Tree Classifier, Different Bagging and Boosting Algorithms
- Front end - HTML,CSS
- Back end - Django
- Web Scraping - BeautifulSoup, Selenium


