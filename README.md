# Rescore
The rescoring module uses pocket similarity search algorithm PPS-align to obtain the top 50 template pockets with similarity score, and the compound library was then rescored using the ligand similarity comparison algorithm LS-align with the corresponding cocrystal ligand as the template ligands.
## Executing program
Rescoring module needs two steps before running the program:
1. prepare the screening compounds (MOL2 format) and pocket ('.POC' format) into the input folder.
put all compounds (MOL2 format) into (user_input/results_docking/ligand_mol2/) subfolder.
put the pocket file (named as "5N2S.poc") into the (user_input/results_docking/pocket/) subfolder.
The pocket is like as:
```
POC     5N2S
ATOM    253  N   VAL A  49       6.937   3.497 -28.457  1.00 34.68           N
ATOM    254  CA  VAL A  49       6.465   2.179 -28.887  1.00 34.68           C
ATOM    255  C   VAL A  49       5.665   2.297 -30.179  1.00 34.68           C
ATOM    256  O   VAL A  49       5.965   1.651 -31.192  1.00 34.68           O
...
TRE
```
2. run_LS.py
```
python run_LS.py
```



# use tool :  python run_LS.py new_dir_name
