# Skriv ett kort pythonscript som klonar ner ett repo, 
# skapar en branch och pushar den branchen till repot.
# Kräver import subprocess.
# Tips: använd subprocess.run() för att exekverar gitkommandon.

import subprocess

# Användaren ska kunna ange reponamn, branchnamn, och git-klientens path.

repo_name = input("Ange reponamn: ")
branch_name = input("Ange branchnamn: ")
git_path = input("Ange git-klientens path (om ingen angiven, används standardvärdet 'git'): ")

# Skapa git-klientens path om ingen angiven.

if not git_path:
    git_path = "git"

# Klona ner repot.

subprocess.run([git_path, "clone", f"https://github.com/{repo_name}.git"], check=True)

# Gå till repot.

subprocess.run([git_path, "cd", repo_name], check=True)

# Skapa en ny branch.

subprocess.run([git_path, "checkout", "-b", branch_name], check=True)

# Pusha den nya branchen till repot.

subprocess.run([git_path, "push", "-u", "origin", branch_name], check=True)

print("Branchen har skapats och pushats till repot.")

