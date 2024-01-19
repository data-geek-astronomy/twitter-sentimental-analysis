

# Twitter-Sentiment-Analysis

This script can tell people's sentiments regarding any events happening in the world by analyzing tweets related to that event. It will search for tweets about any topic and analyze each tweet to see how positive or negative its emotion is. 



## Getting Started
 
First, log in from your Twitter account and go to [Twitter Apps](https://apps.twitter.com/). Create a new app ([How to create twitter app](http://www.letscodepro.com/twitter-sentiment-analysis/)) and goto __Keys and access tokens__ and copy Consumer Key, Consumer Secret, Access Token and Access Token Secret. We will need them later. 

### Installation

Download or Clone the repo, Navigate to the directory containing the files, and run
```
python setup.py install
```
or if you have different versions of Python installed then
```
python3 setup.py install 
```
to install the dependencies.


### Usage

Once you have created an app on Twitter and installed all the dependencies by running __setup.py__, open main.py and paste your Consumer Key, Consumer Secret, Access Token, and Access Token Secret. After that save and run the script. You will be prompted to enter the keyword/hashtag you want to analyze and the number of tweets you want to analyze. Once the analysis is completed, a pie chart will be generated disclosing the analysis results.

## Built With

* Python 3.6
* tweeps
* text blob
* matplotlib
*seaborn
*pandas
*
## Contributing

1. Fork it
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request

## Authors

Aravind Kumar Nalukurthi

## License

This project is licensed under 
