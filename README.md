# 🚀 SAP GUI Automation Template

<p align="center">
  <strong>Automate SAP GUI Tasks with Python and SAP Scripting API</strong>
</p>

<p align="center">
  A reusable Python template for SAP GUI automation, designed to work seamlessly with SAP Script Recorder output.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue" />
  <img src="https://img.shields.io/badge/SAP_GUI-Supported-yellow" />
  <img src="https://img.shields.io/badge/Windows-Only-blue" />
  <img src="https://img.shields.io/badge/SAP_Scripting-Enabled-green" />
  <img src="https://img.shields.io/badge/License-MIT-success" />
</p>

---

## 📖 Overview

SAP GUI Automation Template is a Python-based starter project that simplifies the development of SAP GUI automation scripts using the official SAP Scripting API.

Instead of manually writing complex automation logic from scratch, users can simply record their actions with SAP Script Recorder and paste the generated code directly into the provided template.

The template automatically handles:

* SAP GUI detection
* SAP Logon startup
* Session connection
* Error handling
* Console output formatting

This allows developers, SAP users, and automation engineers to focus only on the business process they want to automate.

---

## ✨ Features

### 🔌 SAP Connection Management

* Automatically detects running SAP GUI sessions
* Automatically launches SAP Logon if not already running
* Connects to existing SAP sessions
* Handles connection errors gracefully

### 🤖 Automation Ready

* Compatible with SAP Script Recorder
* Supports recorded VBScript conversion
* Simple integration into existing SAP workflows
* Reusable template structure

### 🎨 Improved User Experience

* Colorized console output
* Clear status messages
* Success and error notifications
* Easy debugging

### ⚡ Productivity Benefits

* Eliminate repetitive manual tasks
* Reduce human error
* Speed up SAP operations
* Reuse automation across projects

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│   Python Script     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ SAP Scripting API   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      SAP GUI        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     SAP System      │
└─────────────────────┘
```

---

## 📦 Requirements

### Operating System

* Windows 10 / 11
* SAP GUI for Windows installed

### SAP Configuration

SAP GUI Scripting must be enabled:

1. Open SAP GUI
2. Go to:

```text
Options
 └─ Accessibility & Scripting
     └─ Scripting
```

3. Enable:

```text
Enable Scripting
```

### Python

* Python 3.8 or newer

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/elshan-tahermanesh/sap-automation.git
cd sap-automation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📚 Dependencies

```text
pywin32
colorama
psutil
```

Or install manually:

```bash
pip install pywin32 colorama psutil
```

---

## 🎬 Recording SAP Actions

To automate a process:

### Step 1

Open SAP GUI.

### Step 2

Open Script Recorder:

```text
Customize Local Layout (Alt + F12)
 └─ Script Recording and Playback
```

### Step 3

Start recording.

### Step 4

Perform the SAP actions you want to automate.

### Step 5

Stop recording.

### Step 6

Copy the generated VBScript code.

---

## 🔧 Adding Your Automation Logic

Open:

```text
sap_automation.py
```

Locate:

```python
def process_material():
    pass
```

Paste your recorded SAP commands inside this function.

Example:

```python
def process_material():
    try:
        session = connect_to_sap()

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nMM03"
        session.findById("wnd[0]").sendVKey(0)

        print("Automation completed.")

    except Exception as e:
        print(f"Error: {e}")
```

---

## ▶️ Running the Script

Start the automation:

```bash
python sap_automation.py
```

Example output:

```text
[SYSTEM] SAP GUI detected
[SYSTEM] Connected to session
[SYSTEM] Starting automation
[SUCCESS] Process completed
```

---

## 📂 Project Structure

```text
sap-automation/
│
├── sap_automation.py
├── requirements.txt
├── LICENSE
├── README.md
│
├── screenshots/
│   ├── demo.png
│   └── recorder.png
│
└── examples/
    └── sample_recording.vbs
```

---

## 🎯 Use Cases

This template can be used for:

* Material Master Automation
* Purchase Order Processing
* Quality Management Tasks
* Production Planning Operations
* Data Extraction
* Mass Data Updates
* Reporting Automation
* Custom SAP Workflows

---

## 🖼️ Screenshots

Create a folder:

```text
screenshots/
```

Add screenshots such as:

```text
screenshots/
├── sap-logon.png
├── recorder.png
├── automation.png
└── console-output.png
```

Then embed them here:

```md
![SAP Logon](screenshots/sap-logon.png)

![Script Recorder](screenshots/recorder.png)

![Automation](screenshots/automation.png)
```

---

## ⚠️ Disclaimer

This project is intended for:

* Educational purposes
* Productivity enhancement
* Internal business automation

Always ensure that you have permission to automate processes within your SAP environment.

The author assumes no responsibility for misuse, data loss, or unauthorized automation activities.

---

## 👨‍💻 Author

**Elshan Tahermanesh**

* Network Engineer
* SAP Automation Developer
* M.Sc. Computer Science
* University of Rostock

GitHub:

https://github.com/elshan-tahermanesh

---

## 🤝 Contributions

Contributions, improvements, and suggestions are welcome.

Feel free to:

* Open an issue
* Submit a pull request
* Suggest new features

---

## ⭐ Support

If you find this project useful, please consider giving it a star.

⭐ Star the repository to support future development.

---

## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.
