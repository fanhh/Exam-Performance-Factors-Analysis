import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def parents_education_score(db):
    """
    Plot the performance of each group of studetns, \ 
    with paretns from different education backgroud.
    In ascending order.
    """
    new_sample = db.drop(columns=['gender','race/ethnicity', 
                                  'lunch', 'test preparation course'])
    score_mean = new_sample.groupby(
        'parental level of education').mean().sort_values(
                                   ['math score', 'reading score', 'writing score'])
    score_mean.plot(kind='bar', figsize=(3,3), 
                    ec='w', title=('exam score with parents' +
                                   'from different educational backgroubd'))

def overall_lunch(db):
    """
    Plot a bar chart of overall perfromance \
    of exam score with students that get free \
    lunch vs no free lunch.
    """
    new_sample = db.drop(columns=['gender','race/ethnicity', 
                                  'parental level of education', 
                                  'test preparation course'])
    score_mean = new_sample.groupby(
        'lunch').mean().sort_values(['math score', 
                                     'reading score', 
                                     'writing score'])
    score_mean.plot(kind='bar', figsize=(3,3),
                    ec='w', title=('free/reduced lunch exam score '
                                   + 'VS Standard lunch exam score'))

def test_prep(db):
    """
    Plot a bar chart of all the exam performance \
    among students with exam prep or not.
    """
    new_sample = db.drop(columns=['gender','race/ethnicity', 
                                  'parental level of education',
                                  'lunch'])
    score_mean = new_sample.groupby('test preparation course').mean().sort_values(['math score', 
                                                            'reading score', 'writing score'])
    score_mean.plot(kind='bar', figsize=(3,3), 
                    ec='w', title='Test prep vs No test prep exam score')

def predict_model(train, predict, test):
    """
    Title: How to Build a Regression Model in Python
    Author: Chanin Nantasenamat
    Date: 2020
    Code version: 2.0
    Availability: (https://towardsdatascience.com
    /how-to-build-a-regression-model-in-python-9a10685c7f09)
    Plot a scatter plot the predict data and experimetn data. \
    And with a best fit line
    """
    plt.figure(figsize=(10,5))
    plt.subplot(2,1,2)
    plt.scatter(x=train, y=predict,alpha=0.3)
    line = np.poly1d(np.polyfit(train, predict, 1))
    plt.plot(test, line(test))
    plt.xlabel('actual score in standard units')
    plt.ylabel('predicted score in standard units')
    plt.show()

def actual(predict, test):
    """
    Title: How to Build a Regression Model in Python
    Author: Chanin Nantasenamat
    Date: 2020
    Code version: 2.0
    Availability: (https://towardsdatascience.com
    /how-to-build-a-regression-model-in-python-9a10685c7f09)
    Plot a scatter plot the experiment data. \
    And with a best fit line
    """
    plt.figure(figsize=(10,5))
    plt.subplot(2,1,2)
    plt.scatter(x=test, y=predict,alpha=0.3)
    line = np.poly1d(np.polyfit(test, predict, 1))
    plt.plot(test, line(test))
    plt.xlabel('score in standard units')
    plt.show()
