# Rescore
The rescoring module uses pocket similarity search algorithm PPS-align to obtain the top 50 template pockets with similarity score, and the compound library was then rescored using the ligand similarity comparison algorithm LS-align with the corresponding cocrystal ligand as the template ligands.
## Executing program
Rescoring module needs two steps before running the program:
1. prepare the screening compounds (MOL2 format) and pocket ('.POC' format) into the input folder.
put all compounds (MOL2 format) into (user_input/results_docking/ligand_mol2/) subfolder.
put the pocket file (named as "nativepocket.poc") into the (user_input/results_docking/pocket/) subfolder.
The pocket is like as:



# use tool :  python run_LS.py new_dir_name
