import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def execute_notebook(notebook_path):
    with open(notebook_path, encoding='utf-8') as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)
        
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(notebook, {'metadata': {'path': os.path.dirname(notebook_path)}})

    with open(notebook_path, 'w', encoding='utf-8') as nb_file:
        nbformat.write(notebook, nb_file)

def execute_notebooks(notebook_list):
    for notebook in notebook_list:
        execute_notebook(notebook)



if __name__ == "__main__":
    notebooks_to_run = ["01-Data-wrangling.ipynb", "02-Statistics_Analysis-2024.ipynb", "03-Plotting.ipynb"]

    execute_notebooks(notebooks_to_run)