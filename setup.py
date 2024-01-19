from setuptools import setup, find_packages
import os
import codecs

# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AdvancedTwitterSentimentAnalysis',
    version='1.0.0',

    description='Advanced analysis of Twitter sentiments. This tool searches and analyzes tweets to determine public sentiment on various topics, providing insights into overall emotions and opinions expressed in tweets.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/YourGitHubUsername/AdvancedTwitterSentimentAnalysis',

    author='Your Name',
    author_email='your.email@example.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],

    keywords='sentiment analysis twitter nlp text analysis tweepy textblob',

    packages=find_packages(),
    python_requires='>=3.7, <4',

    install_requires=['tweepy', 'textblob', 'matplotlib'],

    project_urls={
        'Bug Reports': 'https://github.com/data-geek-astronomy/twitter-sentimental-analysis',
        'Source': 'https://github.com/data-geek-astronomy/twitter-sentimental-analysis',
    },
)
