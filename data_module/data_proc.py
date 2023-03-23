import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def average_score(row):
    """
    Get the overall average exam score.
    ---
    parameters:
    row = a row of dataframe
    ---
    Return a number
    """
    total = row['math score'] + row['reading score'] + row['writing score']
    return total/3

def quantify_binary(row):
    """
    Quantify the string data into numbers.
    ---
    parameter:
    row = a string
    ---
    Return an int
    """
    if row in ['free/reduced', 'completed']:
        return 1
    return 0

def education_qunaity(degree):
    """
    Quantify the string data into numbers.
    ---
    parameter:
    degree = a string
    ---
    Return a float
    """
    if degree == "master's degree":
        return 1
    elif degree == "bachelor's degree":
        return 0.8
    elif degree in ["some college", "associate's degree"]:
        return 0.6
    return 0.4

def quantify_df(db):
    """
    Create new columns in the dataframe for the linear models.
    ---
    parameter:
    db = a dataframe
    ---
    Return a dataframe
    """
    # quanity the parental level of education, lunch, test preparation course columns
    # Replace all the old columns with the quanify ones
    return db.assign(overall_score = db.apply(average_score, axis=1), 
                   parental_level_of_education = db.get('parental level of education').apply(education_qunaity),
                   school_lunch = db.get('lunch').apply(quantify_binary),
                   exam_prep = db.get('test preparation course').apply(quantify_binary)).drop(
                   columns=['parental level of education','lunch', 'test preparation course'])

def su(numbers):
    """
    Convert number into standard units.
    ---
    parameter:
    numbers = a series of numbers
    ---
    Return a float
    """
    return (numbers - numbers.mean()) / np.std(numbers)

def letter_grade(grade):
    """
    Convert the oveall exam score to grade.
    ---
    Parameter:
    grade = an float
    ---
    Return a string
    """
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    return 'F'

def grades_count(db, factor):
    """
    Draw plot for the grades that's \
    lower than b distrubiton for each \
    factor.
    ---
    Parameters:
    db = a dataframe
    factor = a string
    """
    # Assign a new column called score by apply function to the row
    grade_db = db.assign(score= db.apply(average_score, axis=1))
    # Assign a new column called grade by apply function to the score column
    grade_db = grade_db.assign(grades= grade_db.get('score').apply(letter_grade))
    # Filter out all the grades that's above a C
    grade_db = grade_db[(grade_db.get('grades') == 'F') | (grade_db.get('grades') == 'D')
                       |(grade_db.get('grades') == 'C')].groupby(factor).count().reset_index()
    # Plot the bar chart
    grade_db.plot(kind='bar', x=factor, y='grades', title='Overall grades lower than B', figsize=(5,5))
