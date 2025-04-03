# Log File Analyzer

## 📌 Overview
The **Log File Analyzer** is a Python-based tool designed to read, parse, and analyze application log files. It provides insightful summaries of log levels, services, and common errors, with an optional filtering feature based on date/time. The analysis results can be saved in a structured CSV format.

## ✨ Features
- ✅ Parses structured log files and extracts key information:
  - Timestamp
  - Service name
  - Log level (INFO, ERROR, WARN, etc.)
  - Log message
- ✅ Aggregates log data:
  - Count of log entries by log level
  - Count of log entries by service
  - Most common ERROR message
- ✅ Outputs analysis results to both the console and a CSV file
- ✅ Handles malformed log lines gracefully
- ✅ Supports filtering logs based on user-specified date/time range
- ✅ Includes unit tests for validation

## 📁 Project Structure
```
  log_analyzer/ 
       │── log_analyzer/ 
             ├── main.py  
             ├── parser.py  
             ├── analyzer.py  
             ├── filters.py 
       │── logs/  
             ├── sample.log 
       │── output/  
             ├── summary.csv 
       │── tests/  
             ├── test_parser.py  
             ├── test_analyzer.py 
             ├── test_filters.py 
      │── README.md 
      │── requirements.txt
```

## ⚙️ Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yogesh-mp/log_analyzer.git
cd log_analyzer
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Analyzer
```sh
python log_analyzer/main.py 
```

### 5️⃣ View the Output
The analysis results will be saved in `output/summary.csv`. You can also view the console output for immediate insights.

### 6️⃣ Run Tests
```sh
pytest tests/
```

