import os
import subprocess
import ctypes
import sys

def is_admin():
    """Check if the script is running with admin rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def request_admin_permissions():
    """Request admin permissions if not already granted."""
    if not is_admin():
        print("Requesting admin permissions...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        exit()

def open_batch_file():
    """Open the config.bat file without showing the console."""
    try:
        bat_file = os.path.join(os.path.dirname(__file__), "config.bat")
        if os.path.exists(bat_file):
            # Use subprocess to run the batch file without a console window
            subprocess.run([bat_file], creationflags=subprocess.CREATE_NO_WINDOW)  
            print(f"{bat_file} executed successfully.")
        else:
            print(f"{bat_file} not found.")
    except Exception as e:
        print(f"Failed to open batch file: {e}")

def launch_main_script():
    """Launch the main.py script after gaining admin rights."""
    try:
        main_script = os.path.join(os.path.dirname(__file__), "main.py")
        if os.path.exists(main_script):
            subprocess.run([sys.executable, main_script], shell=True)  
            print(f"{main_script} executed successfully.")
        else:
            print(f"{main_script} not found.")
    except Exception as e:
        print(f"Failed to run main.py: {e}")

def main():
    """Main function to request admin permissions and open scripts."""
    request_admin_permissions()
    open_batch_file()
    launch_main_script()

if __name__ == "__main__":
    main()
