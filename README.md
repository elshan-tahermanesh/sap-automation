# SAP GUI Automation Script

This repository contains a **Python template** for automating tasks in **SAP GUI** using the **SAP Scripting API**.  
Users can easily extend this script by recording SAP steps with the built-in **Script Recorder** and pasting the generated code inside the script.

---

## **Features**
- Automatically connects to SAP GUI.
- Starts **SAP Logon** if it's not already running.
- Provides a clean function (`process_material()`) where you can insert your own SAP automation logic.
- Uses **color-coded console output** for better readability.

---

## **Requirements**
- **Windows** with **SAP GUI for Windows** installed.
- **SAP GUI Scripting** must be enabled:
  - In SAP Logon, go to `Options > Accessibility & Scripting > Scripting`.
  - Enable "Allow Scripting".
- **Python 3.8+** installed.

### **Python Packages**
Install the required packages:
```bash
pip install pywin32 colorama psutil
