# Boston Weather Logging Lab  
### Custom Logging Project – Experiment Tracking (Lab Assignment)

This repository contains a fully customized Python logging project built for Lab Assignment 6 in the Experiment Tracking & MLOps course.  
It demonstrates **real-world logging practices**, modular code design, structured analysis, and the usage of a weather dataset for exploratory analytics.

This project is entirely original and designed with a **Boston weather dataset**, featuring advanced logging, multi-file modular architecture, and robust exception handling.

---

## 📁 Project Structure
```bash
PYTHON-LOGGING-LAB/
│
├── app/
│   ├── boston_weather_analyzer.py   # Performs analytics (avg temp, min temp, missing values)
│   ├── loader.py                    # Loads the dataset safely with full logging
│   └── logger_setup.py              # Configures file + console log handlers
│
├── data/
│   └── boston_weather_data.csv       # Real dataset containing Boston temperature values
│
├── logs/
│   └── boston_weather_app.log        # Auto-generated log file capturing all runtime events
│
├── venv/                              # Virtual environment (excluded from GitHub)
│
└── main.py                            # Main application entry point

Each module is independent, logged, and reusable—designed to mimic a real production project.
```
---

## 🎯 Project Purpose

This project demonstrates:
```bash
- How to configure **Python logging** with:
  - Console logs
  - File logs
  - Log formatting
  - Debug, Info, Warning, Error levels
- How to design a **modular Python application** using packages
- How to track application behavior via logs
- How to handle dataset loading issues with exceptions
- How to analyze weather data using clean functions
```
---

## 🌦 Dataset Description (Boston Weather Data)

The project uses a CSV dataset containing Boston temperature readings.  
The columns typically include:
```bash
- `Max_TemperatureC`
- `Mean_TemperatureC`
- `Min_TemperatureC`
- `Date`
```
These columns allow computation of:
```bash
- Average maximum temperature  
- Maximum of minimum temperatures  
- Missing value analysis  
```
This dataset is stored in:
```bash
data/boston_weather_data.csv
```
---

## 🧠 Application Workflow


### **1️⃣ Logger Initialization**

```bash
`logger_setup.py` configures:

- A log file: `logs/boston_weather_app.log`
- Console output
- Log format containing timestamp, module name, log level, and message
- Logging level set to `DEBUG` to capture full pipeline activity
```
### **2️⃣ Dataset Loading**

```bash`
loader.py`:

- Loads CSV data safely with `pandas`
- Logs file paths, dataset shape, and any exceptions (FileNotFound, parsing issues, etc.)
```
### **3️⃣ Weather Analysis**
```bash
`boston_weather_analyzer.py` computes:

#### ✔ Average Temperature  
Detected dynamically using pattern matching.

#### ✔ Maximum of Minimum Temperatures  
Ensures dataset compatibility by detecting the correct temperature column.

#### ✔ Missing Value Report  
Logs missing values for all columns.
```

### **4️⃣ Orchestration**

```bash
`main.py`:

- Initializes logger  
- Loads dataset  
- Triggers analysis functions  
- Logs all results  
- Handles errors gracefully  
```
---

## ▶️ Running the Project

### **1. Create a virtual environment**

```bash
python3 -m venv venv
```
2. Activate the virtual environment

Mac/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install pandas
```

4. Run the app
```bash
python main.py
```
If everything works, you will see output like:
```bash
INFO - Weather analysis application started
INFO - Loading dataset from data/boston_weather_data.csv
INFO - Average Temperature: 14.94
INFO - Maximum of Minimum Temperatures: 19.0
INFO - Missing Values Report Generated
INFO - Application finished successfully
```
A full log file will be created in:
```bash
logs/boston_weather_app.log

```

---

🧩 Logging Features Demonstrated

Feature	Description
File Logging	All logs are stored in logs/boston_weather_app.log
Console Logging	Live logs during runtime
Log Levels	DEBUG, INFO, WARNING, ERROR
Exception Logging	Tracebacks captured with .exception()
Dynamic Column Detection	No hard-coded column names
Modular Architecture	Separate loader, analyzer, and logger modules


---

🛠 Tech Stack
	•	Python 3

	•	pandas for dataset handling

	•	Logging module (built-in)

	•	Virtual environment for isolation

---

📌 Why This Lab Is Unique
	•	Different dataset (Boston weather)

	•	Different analysis strategy

	•	Custom analyzer (max min temp instead of wind/dew point)

	•	Custom file names and module names

	•	Clean project structure

	•	Advanced logging patterns beyond the sample lab

