import pandas as pd
import os

#creating function for loading data 
def load_data(dataset_name): 
    """
    This function loads the data using the relative path. 

    The function first obtains the path ofthe notebook, then the main directory to finally locate the data directory. 

    Only require input is the data file name. Data should be stored in data/raw for function to work
    """
    # Get the directory the notebook is in
    notebook_dir = os.getcwd()
    project_path = os.path.join(notebook_dir,"..")
    data_path = os.path.join(project_path, "data", "raw", dataset_name)
    df=pd.read_csv(data_path)
    return df