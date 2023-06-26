import os
import pandas as pd
import shutil
import time

df = pd.read_csv('/data/Mukuo/Aurora_B/L-score/EViS-main/user_input/results_docking/ligands_mol2/L_Score_result.csv') #-> the list need a header:'name' 
start = time.time()
ligand_file_path = '/data/Mukuo/Aurora_B/L-score/EViS-main/user_input/results_docking/ligands_mol2/'
ligand_save_path = '/data/Mukuo/Aurora_B/L-score/EViS-main/user_input/results_docking/ligands_mol2/L_Score_result/'
for j,filename in enumerate(os.listdir(ligand_file_path)):
    old_dir = os.path.join(ligand_file_path,filename)
    if j%100 ==0:
        print(time.time()-start,j)
    for i in range(len(df)):
        if str(df['name'][i]) == filename:
            new_dir = os.path.join(ligand_save_path,filename)
            shutil.copy(old_dir,new_dir)
