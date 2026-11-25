# Weekly-Electricity
# ⚡ Weekly Electricity Consumption Matrix

## 📌 Project Overview

The **Weekly Electricity Consumption Matrix** is a Python-based application designed to record and analyse electricity consumption of different household appliances over seven days.

The system stores appliance-wise electricity readings in a two-dimensional matrix, calculates daily and weekly consumption totals, and identifies appliances and days that exceed predefined electricity consumption limits.

It helps users understand electricity usage patterns and encourages efficient energy consumption.

## 🎯 Objectives

- Record electricity consumption of multiple appliances.
- Store daily readings for seven days.
- Calculate appliance-wise weekly consumption.
- Calculate total daily electricity consumption.
- Calculate total weekly electricity consumption.
- Compare consumption against predefined limits.
- Identify appliances with excessive consumption.
- Identify days with high electricity usage.
- Generate a detailed electricity consumption report.

## 🔌 Appliances Considered

The project supports household appliances such as:

1. Fan
2. Light
3. Television
4. Refrigerator
5. Washing Machine

Additional appliances can also be entered by the user.

## 📊 Electricity Consumption Limits

The project uses the following sample weekly consumption limits:

| Appliance | Weekly Limit |
|---|---:|
| Fan | 15 kWh |
| Light | 5 kWh |
| Television | 10 kWh |
| Refrigerator | 25 kWh |
| Washing Machine | 12 kWh |

**Daily Household Consumption Limit:** 10 kWh.

**Note:** These are illustrative academic limits, not official electricity consumption standards.

## 🚀 Features

1. Multiple appliance input.
2. Seven-day electricity consumption recording.
3. Two-dimensional matrix representation.
4. Daily electricity consumption calculation.
5. Appliance-wise weekly consumption calculation.
6. Total weekly electricity calculation.
7. Excess consumption identification.
8. Daily usage limit checking.
9. Highest consumption day identification.
10. Lowest consumption day identification.
11. Detailed electricity usage report.

## 🧮 Calculation Methods

### 1. Appliance-wise Weekly Consumption

```text
Weekly Appliance Consumption =
Monday + Tuesday + Wednesday
+ Thursday + Friday + Saturday + Sunday
```

### 2. Daily Electricity Consumption

```text
Daily Consumption =
Sum of all appliance readings for that day
```

### 3. Total Weekly Consumption

```text
Total Weekly Consumption =
Sum of all appliance weekly totals
```

### 4. Excess Consumption Detection

```text
If Appliance Consumption > Weekly Limit:
    Display Excess Consumption Warning
Else:
    Display Within Limit
```

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## 🐍 Python Concepts Used

- Variables and Data Types
- Lists
- Dictionaries
- Two-Dimensional Data Representation
- Conditional Statements
- For Loops
- While Loops
- Functions
- Arithmetic Operators
- Built-in Functions (`sum()`, `max()`, `min()`)
- User Input and Output

## 📁 Project Structure

```text
Weekly-Electricity-Consumption-Matrix/
│
├── electricity_matrix.py
├── README.md
├── problem_statement.txt
├── objectives.txt
├── assumptions.txt
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
│
└── output_screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Download or clone the GitHub repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Execute the following command:

```bash
python electricity_matrix.py
```

**Step 6:** Enter the number of appliances.

**Step 7:** Enter the appliance names.

**Step 8:** Enter electricity consumption readings for all seven days.

**Step 9:** View the weekly consumption matrix and analysis report.

## 🧪 Test Cases

| Test Case | Input / Condition | Expected Result |
|---|---|---|
| TC01 | Fan consumes 2 kWh daily | Weekly total = 14 kWh |
| TC02 | Light consumes 1 kWh daily | Weekly total = 7 kWh |
| TC03 | Television consumes 2 kWh daily | Weekly total = 14 kWh |
| TC04 | Refrigerator consumes 4 kWh daily | Weekly total = 28 kWh |
| TC05 | Washing machine consumes 2 kWh daily | Weekly total = 14 kWh |
| TC06 | Daily household usage = 12 kWh | High consumption warning |
| TC07 | Daily household usage = 8 kWh | Normal consumption |
| TC08 | All appliance readings are zero | Weekly consumption = 0 kWh |

## 📊 Expected Output

The program displays:

- Weekly electricity consumption matrix.
- Appliance-wise weekly consumption.
- Daily electricity consumption.
- Total weekly electricity consumption.
- Highest consumption day.
- Lowest consumption day.
- Appliance-wise excess consumption warnings.
- Daily high consumption warnings.
- Final electricity analysis report.

## ⚠️ Assumptions

- The analysis covers exactly seven days.
- All readings are entered in kWh.
- Consumption values cannot be negative.
- Weekly appliance limits are predefined for selected appliances.
- The daily household consumption limit is 10 kWh.
- Appliances without predefined weekly limits are reported separately.

## 📝 Conclusion

The Weekly Electricity Consumption Matrix provides a simple and effective method for recording and analysing household electricity usage using Python.

It calculates daily and appliance-wise consumption, determines total weekly usage, and identifies excessive electricity consumption using predefined limits.

This project demonstrates the practical application of Python lists, dictionaries, loops, conditional statements, functions, and matrix-based data representation in a real-world electricity monitoring system.

---

**Project Name:** Weekly Electricity Consumption Matrix

**Subject:** Python Activity-Based Learning
name:sree hasini
sectoin:5
**Programming Language:** Python 3

**Project Type:** Case Study
