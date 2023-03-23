from data_module import basic_model
from data_module import data_proc
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

test_db = pd.read_csv('data/exams.csv')

def test_quantify_binary():
    assert callable(data_proc.quantify_binary)
    assert isinstance(data_proc.quantify_binary('abs'), int)
    assert data_proc.quantify_binary('abs') == 0
    assert data_proc.quantify_binary('free/reduced') == 1
    assert data_proc.quantify_binary('completed') == 1
                                     
def test_education_qunaity():
    assert callable(data_proc.education_qunaity)
    assert isinstance(data_proc.education_qunaity('master'), int)                          
    assert data_proc.education_qunaity('master') == 0.4
    assert data_proc.education_qunaity('some college') == 0.6
    assert data_proc.education_qunaity("bachelor's degree") == 0.8
    assert data_proc.education_qunaity("master's degree") == 1
                                                                                                               
def test_su():
    assert callable(data_proc.su)
    assert isinstance(data_proc.su(test_db.get('math score')), pd.core.series.Series)
    assert data_proc.su(test_db.get('math score')).sum() > 0
    assert len(data_proc.su(test_db.get('math score'))) == 1000                    