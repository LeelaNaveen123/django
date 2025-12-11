import json
import matplotlib.pyplot as plt
from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):

    # Load JSON
    json_path = os.path.join(BASE_DIR, "empdetails.json")
    with open(json_path, "r") as file:
        empdetails = json.load(file)

    names = list(empdetails.keys())
    compensation = list(empdetails.values())

    # Create pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(
        compensation,
        labels=names,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Employee Compensation Pie Chart")
    plt.axis("equal")

    # Save chart to static folder
    static_dir = os.path.join(BASE_DIR, "app", "static")
    os.makedirs(static_dir, exist_ok=True)

    chart_path = os.path.join(static_dir, "piechart.png")
    plt.savefig(chart_path)
    plt.close()

    return render(request, "index.html", {"chart": "piechart.png"})

