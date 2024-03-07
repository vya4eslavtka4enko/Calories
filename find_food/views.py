from django.shortcuts import render
from django.http import HttpRequest
import pandas
import csv

LIST_ADD = ['']
ADD_DISH = []
LIST_QUANTITY = []
LIST_CALORIES = []
def main(request):
    quantity = quantity_food(request)
    data = load_data()
    for index, row in data.iterrows():
        if str(quantity[0]) in row['Food']:
            print(1)



    return render(request,"main.html",{'data':quantity})


def load_data():
    df = pandas.read_csv('data/nutrients_csvfile.csv')
    return df

def quantity_food(request):
    if request.method == "POST":
        kind_food = request.POST.get('kind_food')
        how_many = request.POST.get('how_many')
        return kind_food,how_many





