import win32com.client
import os
import time
import subprocess
import psutil
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Path to the SAP Logon executable
SAP_PATH = "saplogon.exe"

# Function to start SAP Logon if not already running
def start_sap():
    try:
        if not os.path.exists(SAP_PATH):
            print(Fore.RED + " SAP Logon executable not found.")
            exit(1)

        if not any("saplogon.exe" in p.name().lower() for p in psutil.process_iter()):
            subprocess.Popen(SAP_PATH)
            print(Fore.YELLOW + " Starting SAP Logon...")
            time.sleep(10)  # Give SAP some time to launch
        else:
            print(Fore.CYAN + " SAP Logon is already running.")
    except Exception as e:
        print(Fore.RED + f" Failed to start SAP Logon: {e}")
        exit(1)

# Function to connect to an existing SAP GUI session
def connect_to_sap():
    try:
        sapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = sapGuiAuto.GetScriptingEngine()

        if application.Children.Count == 0:
            raise Exception("No SAP connections found.")
        connection = application.Children(0)

        if connection.Children.Count == 0:
            raise Exception("No active sessions found.")
        session = connection.Children(0)

        print(Fore.GREEN + " Connected to SAP.")
        return session

    except Exception as e:
        print(Fore.RED + f" Initial connection failed: {e}")
        print(Fore.YELLOW + " Trying to start SAP Logon...")
        start_sap()
        time.sleep(15)

        try:
            sapGuiAuto = win32com.client.GetObject("SAPGUI")
            application = sapGuiAuto.GetScriptingEngine()

            if application.Children.Count == 0:
                raise Exception("No SAP connections found after starting SAP.")
            connection = application.Children(0)

            if connection.Children.Count == 0:
                raise Exception("No active sessions found after starting SAP.")
            session = connection.Children(0)

            print(Fore.GREEN + " Connected after starting SAP Logon.")
            return session
        except Exception as e2:
            print(Fore.RED + f" Failed to connect to SAP: {e2}")
            exit(1)

# Placeholder function (customize with actual SAP automation)
def process_material():
    try:
        session = connect_to_sap()


        # Example placeholder logic


        print(Fore.GREEN + " SAP session is ready. Add your logic here.")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")

# Main entry point
if __name__ == "__main__":
    print(Fore.GREEN + " SAP Automation Starting...")

    print(Fore.YELLOW + " Loading", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    time.sleep(1)

    process_material()
