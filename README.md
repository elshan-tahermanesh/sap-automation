# 🚀 SAP GUI Automation Script

A **Python template** for automating tasks in **SAP GUI** using the official **SAP Scripting API**.  
This script is designed for easy customization – simply use SAP's **Script Recorder**, copy the generated code, and paste it into the template.

---

## ✨ Features
- **Auto-connect** to existing SAP GUI sessions.
- **Auto-launch** SAP Logon if it's not already running.
- **Ready-to-use template** with a `process_material()` function for your custom SAP logic.
- **Color-coded output** for better readability (via `colorama`).
- Works seamlessly with **SAP Script Recording**.

---

## 📦 Requirements
- **Windows OS** with **SAP GUI for Windows** installed.
- **SAP GUI Scripting** must be enabled:
  - Go to `Options > Accessibility & Scripting > Scripting`.
  - Check **"Enable Scripting"**.
- **Python 3.8+** installed.

### Python Packages
Install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔧 Usage
1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/elshan-tahermanesh/sap-automation.git
   cd sap-automation
   ```

2. **Record your SAP steps**:
   - Open SAP GUI.
   - Go to `Customize Local Layout (Alt + F12) > Script Recording and Playback`.
   - Record your actions and copy the generated VBScript code.

3. **Insert your SAP logic**:
   Paste your recorded SAP code into the `process_material()` function inside `sap_automation.py`.

4. **Run the script**:
   ```bash
   python sap_automation.py
   ```

---

## 📂 Example Structure
Your custom code should go inside this placeholder:
```python
def process_material():
    try:
        session = connect_to_sap()

        # Example placeholder logic:
        # session.findById("wnd[0]/tbar[0]/okcd").text = "/nMM03"
        # session.findById("wnd[0]").sendVKey(0)

        print(Fore.GREEN + " SAP session is ready. Add your logic here.")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")
```

---

## ⚠️ Disclaimer
This script is intended for **educational and productivity purposes only**.  
Ensure you have permission to automate processes in your SAP environment.  
The author is **not responsible** for any misuse or damages caused by this script.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

**💡 Pro Tip:**  
Use this as a **starter template** for any SAP GUI automation project. You only need to modify the `process_material()` function to suit your requirements.


============================
LICENSE (MIT)
============================
MIT License

Copyright (c) 2025 Elshan Tahermanesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


============================
requirements.txt
============================
pywin32
colorama
psutil
