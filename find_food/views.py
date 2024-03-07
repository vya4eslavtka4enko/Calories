from django.shortcuts import render
from django.http import HttpRequest
import pandas

LIST_OF_FOOD = []
ALL_CALORIES = []

def main(request):
    sum_all_calories=0
    if request.method == "POST":
        result = quantity_food(request)
        ALL_CALORIES.append(result[2])
        LIST_OF_FOOD.append(result)
    for item in ALL_CALORIES:
        sum_all_calories+=float(item)
    print(sum_all_calories)
    return render(request,"main.html",{'result':LIST_OF_FOOD,'sum_all_calories':format(sum_all_calories,'.2f')})


def load_data():
    df = pandas.read_csv('data/nutrients_csvfile.csv')
    return df

def quantity_food(request):
    data = load_data()
    kind_food = request.POST.get('kind_food')
    how_many = request.POST.get('how_many')
    for index, row in data.iterrows():
        if kind_food in row['Food']:
            result=float(row['Calories'])/float(row['Grams'])*float(how_many)
    return kind_food,how_many,format(result,'.2f')





