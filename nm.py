import subprocess
import time

app_path = "C:\Program Files (x86)\FuH\Docklight V2.4\Docklight.exe"

while True:
    # Start the application
    subprocess.Popen(app_path)
    
    # Wait for a while (e.g., 60 seconds)
    time.sleep(60)
    
    # Check if the application is still running, and if not, restart it
    while True:
        try:
            poll = subprocess.Popen(app_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE).poll()
            if poll is None:
                # The application is still running
                break
            else:
                # The application has exited, so restart it
                break
        except FileNotFoundError:
            # Handle the case where the application executable is not found
            print(f"Application not found: {app_path}")
            break
        except Exception as e:
            # Handle other exceptions
            print(f"Error: {e}")
    
    # Optionally, you can add a delay between restarts to avoid overloading your system
    time.sleep(60)
