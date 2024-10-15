import os
import subprocess

notebook_directory = "./notebooks"

for filename in os.listdir(notebook_directory):
    if filename.endswith(".ipynb"):

        f_path = os.path.join(notebook_directory, filename)

        subprocess.run(["jupyter", "nbconvert", "--to", "script", f_path])
