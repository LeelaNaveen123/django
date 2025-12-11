import json
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.conf import settings
import os

def home(request):
    # Load empdetails.json
    json_path = os.path.join(settings.BASE_DIR, "empdetails.json")
    with open(json_path, "r") as file:
        empdetails = json.load(file)

    names = list(empdetails.keys())
    values = list(empdetails.values())

    # Create pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=names, autopct="%1.1f%%", startangle=90)
    plt.title("Employee Compensation")
    plt.axis("equal")

    # Save to static folder
    static_path = os.path.join(settings.BASE_DIR, "app", "static", "piechart.png")
    plt.savefig(static_path)
    plt.close()

    return render(request, "index.html")
