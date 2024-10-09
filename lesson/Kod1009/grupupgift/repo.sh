import subprocess

# Variables
repo_url = 'https://github.com/ChasAcademy-HasanBalkanci/Python.git'  
new_branch = 'feature_lesson'              

# Clone the repository
subprocess.run(['git', 'clone', https://github.com/ChasAcademy-HasanBalkanci/Python.git])

# Navigate into the repository directory
repo_name = repo_url.split('/')[-1].replace('.git', '')
subprocess.run(['cd', repo_name])

# Create a new branch
subprocess.run(['git', 'checkout', '-b', new_branch])

# Push the new branch to the remote repository
subprocess.run(['git', 'push', '-u', 'origin', new_branch])
