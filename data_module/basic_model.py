from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def my_model():
    """
    Initalize the linear model
    """
    return LinearRegression()

def datasplit(x, y, train=0.8, test=0.2):
    """
    Split the data into subsets for training
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test, train_size=train)
    return x_train, x_test, y_train, y_test

def score_predict_train(model, x, y):
    """
    Title: How to Build a Regression Model in Python
    Author: Chanin Nantasenamat
    Date: 2020
    Code version: 2.0
    Availability: (https://towardsdatascience.com
    /how-to-build-a-regression-model-in-python-9a10685c7f09)
    """
    predict_train = model.predict(x)
    print('Intercept: ' + str(model.intercept_))
    print('Mean sqaured Error(MSE): ' + str(mean_squared_error(y, predict_train)))
    print('R^2: ' + str(r2_score(y, predict_train)))
    return predict_train
          
          
def score_predict_test(model, x, y):
    """
    Title: How to Build a Regression Model in Python
    Author: Chanin Nantasenamat
    Date: 2020
    Code version: 2.0
    Availability: (https://towardsdatascience.com
    /how-to-build-a-regression-model-in-python-9a10685c7f09)
    """
    predict_test = model.predict(x)
    print('Intercept: ' + str(model.intercept_))
    print('Mean sqaured Error(MSE): ' + str(mean_squared_error(y, predict_test)))
    print('R^2: ' + str(r2_score(y, predict_test)))
    return predict_test

def linear_eq(model):
    """
    Print out the equation of the linear model
    """
    print(f'predicted_y = {model.intercept_} + {model.coef_[0]}PE +' +
          f'{model.coef_[1]}l + {model.coef_[2]}ep')
    
