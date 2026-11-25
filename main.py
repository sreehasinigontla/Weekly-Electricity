
# Weekly Electricity Consumption Matrix

# Seven days of the week
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Sample appliance weekly limits (kWh)
appliance_limits = {
    "fan": 15,
    "light": 5,
    "television": 10,
    "refrigerator": 25,
    "washing machine": 12
}

# Daily household consumption limit
DAILY_LIMIT = 10


# Function to get valid positive integer
def get_integer(message):

    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid integer.")


# Function to get valid consumption
def get_consumption(message):

    while True:
        try:
            value = float(input(message))

            if value >= 0:
                return value

            print("Consumption cannot be negative.")

        except ValueError:
            print("Enter a valid number.")


# Function to calculate appliance totals
def calculate_appliance_totals(matrix):

    totals = {}

    for appliance in matrix:

        totals[appliance] = sum(matrix[appliance])

    return totals


# Function to calculate daily totals
def calculate_daily_totals(matrix):

    daily_totals = []

    for i in range(7):

        total = 0

        for appliance in matrix:

            total += matrix[appliance][i]

        daily_totals.append(total)

    return daily_totals


# Function to display consumption matrix
def display_matrix(matrix):

    print("\n========== WEEKLY CONSUMPTION MATRIX ==========")

    print("Appliance".ljust(20), end="")

    for day in days:
        print(day[:3].rjust(10), end="")

    print()

    for appliance in matrix:

        print(appliance.title().ljust(20), end="")

        for reading in matrix[appliance]:

            print(str(round(reading, 2)).rjust(10), end="")

        print()


# Function to identify excessive consumption
def check_limits(appliance_totals, daily_totals):

    print("\n========== EXCESS CONSUMPTION REPORT ==========")

    # Check appliance-wise weekly limits
    print("\nAppliance-wise Analysis:")

    for appliance in appliance_totals:

        total = appliance_totals[appliance]

        limit = appliance_limits.get(appliance)

        if limit is not None:

            if total > limit:

                print(
                    appliance.title(),
                    "- EXCEEDED LIMIT:",
                    round(total, 2),
                    "kWh (Limit:",
                    limit,
                    "kWh)"
                )

            else:

                print(
                    appliance.title(),
                    "- Within limit:",
                    round(total, 2),
                    "kWh"
                )

        else:

            print(
                appliance.title(),
                "- No predefined weekly limit available."
            )

    # Check daily household limits
    print("\nDaily Consumption Analysis:")

    for i in range(7):

        if daily_totals[i] > DAILY_LIMIT:

            print(
                days[i],
                "- HIGH CONSUMPTION:",
                round(daily_totals[i], 2),
                "kWh"
            )

        else:

            print(
                days[i],
                "- Normal:",
                round(daily_totals[i], 2),
                "kWh"
            )


# Main Program
print("==============================================")
print("   WEEKLY ELECTRICITY CONSUMPTION MATRIX")
print("==============================================")

# Get number of appliances
n = get_integer("\nEnter number of appliances: ")

# Create empty matrix
matrix = {}

# Input appliance readings
for i in range(n):

    print("\n---------- Appliance", i + 1, "----------")

    appliance = input("Enter appliance name: ").strip().lower()

    while appliance == "" or appliance in matrix:
        if appliance == "":
            print("Appliance name cannot be empty.")
        else:
            print("Appliance already entered.")

        appliance = input("Enter another appliance name: ").strip().lower()

    matrix[appliance] = []

    print("\nEnter daily consumption in kWh:")

    for day in days:

        reading = get_consumption(day + ": ")

        matrix[appliance].append(reading)


# Calculate appliance-wise totals
appliance_totals = calculate_appliance_totals(matrix)

# Calculate daily totals
daily_totals = calculate_daily_totals(matrix)

# Display consumption matrix
display_matrix(matrix)


# Display appliance-wise weekly totals
print("\n========== APPLIANCE WEEKLY TOTALS ==========")

for appliance in appliance_totals:

    print(
        appliance.title(),
        ":",
        round(appliance_totals[appliance], 2),
        "kWh"
    )


# Display daily totals
print("\n========== DAILY CONSUMPTION TOTALS ==========")

for i in range(7):

    print(
        days[i],
        ":",
        round(daily_totals[i], 2),
        "kWh"
    )


# Calculate total weekly consumption
weekly_total = sum(appliance_totals.values())

print("\nTotal Weekly Consumption:", round(weekly_total, 2), "kWh")


# Find highest and lowest consumption days
highest_day = max(daily_totals)
lowest_day = min(daily_totals)

print("\nHighest Consumption Day:")

for i in range(7):

    if daily_totals[i] == highest_day:
        print(days[i], "-", round(highest_day, 2), "kWh")


print("\nLowest Consumption Day:")

for i in range(7):

    if daily_totals[i] == lowest_day:
        print(days[i], "-", round(lowest_day, 2), "kWh")


# Check consumption limits
check_limits(appliance_totals, daily_totals)


print("\n==============================================")
print("Electricity Consumption Analysis Completed!")
print("==============================================")
