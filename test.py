import requests
import subprocess

def update_script():
    # URL of the raw script on GitHub
    url = "https://raw.githubusercontent.com/GeoToboGaming/test/master/test.py"

    # Fetch the raw content of the script
    response = requests.get(url)

    if response.status_code == 200:
        # Overwrite the current script with the fetched content
        with open(__file__, 'w') as f:
            f.write(response.text)
        print("Script updated successfully!")
        # Run the payload or any other desired functionality
        run_payload()
    else:
        print("Failed to update script.")

def run_payload():
    # Add your payload code here
    subprocess.run(["calc.exe"])  # Example payload to open the calculator

if __name__ == "__main__":
    update_script()
