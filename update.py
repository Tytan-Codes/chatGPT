import subprocess

# Set the GitHub repository URL and the script file name
github_url = "https://github.com/tytan-codes/chatGPT.git"
script_name = "main.py"

# Get the latest commit hash from the GitHub repository
cmd = "git ls-remote " + github_url + " HEAD"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting latest commit hash from GitHub.")
    exit()
latest_commit = result.stdout.decode().split()[0]

# Check if the latest commit is already downloaded
cmd = "git rev-parse HEAD"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting current commit hash.")
    exit()
current_commit = result.stdout.decode().strip()
if current_commit == latest_commit:
    print("You are running the latest version of the script.")
else:
    # Update to the latest commit
    cmd = "git pull"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error updating script from GitHub.")
        exit()
    print("Script updated successfully.")

