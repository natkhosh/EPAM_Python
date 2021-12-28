import json

# from homework10.task_1.task_1 import *

path_file_price = '../task_1/price.json'
path_file_growth = '../task_1/growth.json'
path_file_pe = '../task_1/pe.json'
path_file_profit = '../task_1/profit.json'


def test_positive():
    """Testing that created json file with top 10 companies"""
    with open(path_file_price, 'r') as json_file:
        data = json.load(json_file)
        assert len(data) == 10
    with open(path_file_profit, 'r') as json_file:
        data = json.load(json_file)
        assert len(data) == 10


def test_negative():
    """Testing that created json file contains less than 10 companies"""
    with open(path_file_growth, 'r') as json_file:
        data = json.load(json_file)
        assert len(data) != 0
    with open(path_file_pe, 'r') as json_file:
        data = json.load(json_file)
        assert len(data) != 0
