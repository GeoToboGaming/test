import requests
import subprocess

def update_script():
    url = "https://raw.githubusercontent.com/GeoToboGaming/test/master/test.py"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        with open("updated_script.py", "w") as f:
            f.write(response.text)
        print("Script updated successfully!")
        run_payload()
    except Exception as e:
        print(f"Failed to update script: {e}")

if __name__ == "__main__":
    update_script()


def run_payload():
    # Add your payload code here
    subprocess.run(["calc.exe"])  # Example payload to open the calculator

if __name__ == "__main__":
    update_script()
