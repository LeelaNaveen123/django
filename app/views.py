import json
import matplotlib.pyplot as plt
from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    json_path = os.path.join(settings.BASE_DIR, "empdetails.json")

    with open(json_path, "r") as f:
        empdetails = json.load(f)

    names = list(empdetails.keys())
    values = list(empdetails.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=names, autopct="%1.1f%%", startangle=90)
    plt.title("Employee Compensation")
    plt.axis("equal")

    # Save piechart in static directory
    chart_path = os.path.join(settings.BASE_DIR, "app", "static", "piechart.png")
    plt.savefig(chart_path)
    plt.close()

    return render(request, "index.html")

