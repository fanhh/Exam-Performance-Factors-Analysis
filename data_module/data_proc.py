import numpy as np

def average_score(row):
    """Get the overall average exam score"""
    total = row['math score'] + row['reading score'] + row['writing score']
    return total/300

def quantify_binary(row):
    """Quantify the string data into numbers"""
    if row in ['free/reduced', 'completed']:
        return 1
    return 0

def education_qunaity(degree):
    """Quantify the string data into numbers"""
    if degree == "master's degree":
        return 1
    elif degree == "bachelor's degree":
        return 0.8
    elif degree in ["some college", "associate's degree"]:
        return 0.6
    return 0.4

def quantify_df(db):
    """Create new columns in the dataframe for the linear models"""
    return db.assign(overall_score = db.apply(average_score, axis=1), 
                   parental_level_of_education = db.get('parental level of education').apply(education_qunaity),
                   school_lunch = db.get('lunch').apply(quantify_binary),
                   exam_prep = db.get('test preparation course').apply(quantify_binary)).drop(
                   columns=['parental level of education','lunch', 'test preparation course'])

def su(any_numbers):
    """Convert number into standard units"""
    return (any_numbers - any_numbers.mean()) / np.std(any_numbers)

    