#!/usr/bin/env python3

"""
Python DateTime Module Examples
----------------------------
Demonstrates various operations with dates and times using the datetime module.
"""

from datetime import datetime, date, time, timedelta
import pytz  # For timezone operations

# 1. Basic Date and Time Operations
print("1. Basic Date and Time Operations")
print("-" * 35)

# Get current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")
print(f"Date: {current_datetime.date()}")
print(f"Time: {current_datetime.time()}")

# Access individual components
print("\nDateTime Components:")
print(f"Year: {current_datetime.year}")
print(f"Month: {current_datetime.month}")
print(f"Day: {current_datetime.day}")
print(f"Hour: {current_datetime.hour}")
print(f"Minute: {current_datetime.minute}")
print(f"Second: {current_datetime.second}")
print(f"Microsecond: {current_datetime.microsecond}")

print("\n")

# 2. Creating Date Objects
print("2. Creating Date Objects")
print("-" * 35)

# Create a specific date
specific_date = datetime(2024, 12, 31, 23, 59, 59)
print(f"Specific date: {specific_date}")

# Create date from timestamp
timestamp = 1735689600  # December 31, 2024, 00:00:00 UTC
date_from_timestamp = datetime.fromtimestamp(timestamp)
print(f"Date from timestamp: {date_from_timestamp}")

# Today's date
today = date.today()
print(f"Today's date: {today}")

print("\n")

# 3. Date Formatting (strftime)
print("3. Date Formatting")
print("-" * 35)

current_date = datetime.now()

# Different format examples
print("Date formatting examples:")
print(f"Full datetime: {current_date.strftime('%c')}")
print(f"Date only (MM/DD/YY): {current_date.strftime('%m/%d/%y')}")
print(f"Date only (DD-MM-YYYY): {current_date.strftime('%d-%m-%Y')}")
print(f"Full month name: {current_date.strftime('%B')}")
print(f"Short month name: {current_date.strftime('%b')}")
print(f"Full weekday name: {current_date.strftime('%A')}")
print(f"Short weekday name: {current_date.strftime('%a')}")
print(f"Century: {current_date.strftime('%C')}")
print(f"Time (24-hour): {current_date.strftime('%H:%M:%S')}")
print(f"Time (12-hour): {current_date.strftime('%I:%M:%S %p')}")

print("\n")

# 4. Date Calculations
print("4. Date Calculations")
print("-" * 35)

# Add days to a date
future_date = current_date + timedelta(days=30)
print(f"Date after 30 days: {future_date.date()}")

# Subtract days
past_date = current_date - timedelta(days=30)
print(f"Date 30 days ago: {past_date.date()}")

# Complex timedelta
complex_future = current_date + timedelta(
    days=30,
    hours=12,
    minutes=30,
    seconds=15
)
print(f"Complex future date: {complex_future}")

# Calculate time difference
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
time_difference = date2 - date1
print(f"Days between Jan 1 and Dec 31, 2024: {time_difference.days}")

print("\n")

# 5. Working with Time Zones
print("5. Working with Time Zones")
print("-" * 35)

# Current time in UTC
utc_now = datetime.now(pytz.UTC)
print(f"Current UTC time: {utc_now}")

# Convert to different time zones
timezones = ['US/Pacific', 'US/Eastern', 'Europe/London', 'Asia/Tokyo']
for tz_name in timezones:
    tz = pytz.timezone(tz_name)
    local_time = utc_now.astimezone(tz)
    print(f"Time in {tz_name}: {local_time}")

print("\n")

# 6. Parsing Dates from Strings
print("6. Parsing Dates from Strings")
print("-" * 35)

# Parse different date formats
date_strings = [
    "2024-12-31",
    "31/12/2024",
    "Dec 31 2024",
    "31-12-2024 23:59:59"
]

print("Parsing different date formats:")
try:
    # ISO format
    date1 = datetime.strptime(date_strings[0], "%Y-%m-%d")
    print(f"ISO format: {date1}")
    
    # DD/MM/YYYY format
    date2 = datetime.strptime(date_strings[1], "%d/%m/%Y")
    print(f"DD/MM/YYYY format: {date2}")
    
    # Month DD YYYY format
    date3 = datetime.strptime(date_strings[2], "%b %d %Y")
    print(f"Month DD YYYY format: {date3}")
    
    # DD-MM-YYYY HH:MM:SS format
    date4 = datetime.strptime(date_strings[3], "%d-%m-%Y %H:%M:%S")
    print(f"DD-MM-YYYY HH:MM:SS format: {date4}")
except ValueError as e:
    print(f"Error parsing date: {e}")

print("\n")

# 7. Practical Examples
print("7. Practical Examples")
print("-" * 35)

# Calculate age from birthdate
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Example birthdate
birthdate = date(1990, 6, 15)
age = calculate_age(birthdate)
print(f"Age for birthdate {birthdate}: {age} years")

# Check if a year is leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(f"\nIs 2024 a leap year? {is_leap_year(2024)}")
print(f"Is 2025 a leap year? {is_leap_year(2025)}")

# Get first and last day of current month
def get_month_bounds(date_obj):
    first_day = date_obj.replace(day=1)
    # Using timedelta to subtract one day from first day of next month
    if date_obj.month == 12:
        last_day = date_obj.replace(year=date_obj.year + 1, month=1, day=1) - timedelta(days=1)
    else:
        last_day = date_obj.replace(month=date_obj.month + 1, day=1) - timedelta(days=1)
    return first_day, last_day

first, last = get_month_bounds(current_date)
print(f"\nFirst day of current month: {first}")
print(f"Last day of current month: {last}")
