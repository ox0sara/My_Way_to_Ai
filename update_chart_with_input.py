import json
from datetime import datetime
import matplotlib.pyplot as plt


try:
    with open("learning_log.json") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []


with open("today_hours.txt") as f:
    hours_today = float(f.read().strip())

today = datetime.now().strftime("%Y-%m-%d")


found = False
for item in data:
    if item["date"] == today:
        item["hours"] = hours_today
        found = True
        break
if not found:
    data.append({"date": today, "hours": hours_today})


with open("learning_log.json", "w") as f:
    json.dump(data, f, indent=2)


dates = [datetime.strptime(item["date"], "%Y-%m-%d") for item in data]
hours = [item["hours"] for item in data]

plt.figure(figsize=(8,4))
plt.plot(dates, hours, marker='o', color='teal')
plt.fill_between(dates, hours, alpha=0.2, color='teal')
plt.title("Daily Learning Hours")
plt.xlabel("Date")
plt.ylabel("Hours")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("learning_chart.png")