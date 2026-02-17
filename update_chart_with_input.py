""" import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
from datetime import datetime, timedelta

# خواندن فایل لاگ
try:
    with open("learning_log.json") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# خواندن ساعت امروز
with open("today_hours.txt") as f:
    hours_today = float(f.read().strip())

# گرفتن تاریخ امروز
today_dt = datetime.now()
today_str = today_dt.strftime("%Y-%m-%d")

# اضافه کردن یا به‌روزرسانی امروز
found = False
for item in data:
    if item["date"] == today_str:
        item["hours"] = hours_today
        found = True
        break
if not found:
    data.append({"date": today_str, "hours": hours_today})

# ذخیره فایل لاگ
with open("learning_log.json", "w") as f:
    json.dump(data, f, indent=2)

# ساخت یک دیکشنری برای دسترسی سریع به داده‌ها
data_dict = {}
for item in data:
    try:
        dt = datetime.strptime(item["date"], "%Y-%m-%d")
        if dt.year == today_dt.year:
            data_dict[dt.date()] = item["hours"]
    except ValueError:
        print(f"Skipping invalid date: {item['date']}")

# ساخت تمام روزهای سال جاری
start_of_year = datetime(today_dt.year, 1, 1).date()
end_of_year = datetime(today_dt.year, 12, 31).date()
delta = timedelta(days=1)

all_dates = []
all_hours = []
current_day = start_of_year
while current_day <= end_of_year:
    all_dates.append(current_day)
    all_hours.append(data_dict.get(current_day, 0))  # اگر داده نیست 0
    current_day += delta

# تولید نمودار
plt.figure(figsize=(18,6))
plt.plot(all_dates, all_hours, marker='o', markersize=2, color='teal')
plt.fill_between(all_dates, all_hours, alpha=0.2, color='teal')
plt.title(f"Daily Learning Hours - {today_dt.year}")
plt.xlabel("Date")
plt.ylabel("Hours")
plt.xticks(rotation=45)

# برای خوانایی محور X، هر ماه یک تیک بزنیم
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))

plt.tight_layout()
plt.savefig("learning_chart.png")
print("Chart generated successfully!") """

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
from datetime import datetime
import calendar

# Read the log file
try:
    with open("learning_log.json") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# Read today's hours
with open("today_hours.txt") as f:
    hours_today = float(f.read().strip())

# Get today's date
today_dt = datetime.now()
today_str = today_dt.strftime("%Y-%m-%d")

# Add or update today's record
found = False
for item in data:
    if item["date"] == today_str:
        item["hours"] = hours_today
        found = True
        break
if not found:
    data.append({"date": today_str, "hours": hours_today})

# Save the updated log
with open("learning_log.json", "w") as f:
    json.dump(data, f, indent=2)

# Get current month info
year = today_dt.year
month = today_dt.month
num_days = calendar.monthrange(year, month)[1]

# Build a dictionary for current month's data
data_dict = {}
for item in data:
    try:
        dt = datetime.strptime(item["date"], "%Y-%m-%d")
        if dt.year == year and dt.month == month:
            data_dict[dt.day] = item["hours"]
    except ValueError:
        print(f"Skipping invalid date: {item['date']}")

# Create full list of days in the month
days = list(range(1, num_days + 1))
hours = [data_dict.get(day, 0) for day in days]  # missing days = 0

# Calculate total hours for the month
total_hours = sum(hours)
print(f"Total hours this month: {total_hours}")

# Assign colors based on hours
colors = []
for h in hours:
    if h < 2:
        colors.append("#FFD580")  # pale orange
    elif 2 <= h <= 4:
        colors.append("#90EE90")  # pale green
    elif 4 < h <= 8:
        colors.append("#FF9999")  # pale red
    else:
        colors.append("#ADD8E6")  # pale blue for any unusual value >8

# Generate the colored bar chart
plt.figure(figsize=(12,5))
plt.bar(days, hours, color=colors, edgecolor='black', alpha=0.7)
plt.title(f"Daily Learning Hours - {today_dt.strftime('%B %Y')}")
plt.xlabel("Day of Month")
plt.ylabel("Hours")
plt.xticks(days)
plt.tight_layout()
plt.savefig("learning_chart.png")

print("Monthly colored bar chart generated successfully!")