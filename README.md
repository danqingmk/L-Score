# L-Score
The rescoring module uses pocket similarity search algorithm PPS-align to obtain the top 50 template pockets with similarity score, and the compound library was then rescored using the ligand similarity comparison algorithm LS-align with the corresponding cocrystal ligand as the template ligands.
## Installation
Rescoring module is built on Python3, we recommend using Anaconda environment as enviroment management. The virtual environment can be created as follows:
```
conda create -n your_environment python==3.7
conda activate your_environment
```
Download the source code of rescore from GitHub:
```
git clone https://github.com/danqingmk/L-Score.git
```
## Executing program
Rescoring module needs two steps before running the program:
1. prepare the screening compounds (MOL2 format) and pocket ('.POC' format) into the input folder.
put all compounds (MOL2 format) into (user_input/results_docking/ligand_mol2/) subfolder.
put the pocket file (named as "4AF3.poc") into the (user_input/results_docking/pocket/) subfolder.
The pocket is like as:
```
POC     4AF3
ATOM      1  N   LEU A  83      22.048 -28.324 -12.736  1.00 66.94           N  
ATOM      2  CA  LEU A  83      22.513 -26.988 -12.326  1.00 67.60           C  
ATOM      3  C   LEU A  83      23.247 -26.970 -10.976  1.00 68.95           C  
ATOM      4  O   LEU A  83      24.299 -26.348 -10.841  1.00 71.15           O  
ATOM      5  CB  LEU A  83      21.340 -25.998 -12.295  1.00 65.27           C  
ATOM      6  CG  LEU A  83      20.742 -25.539 -13.638  1.00 65.01           C  
ATOM      7  CD1 LEU A  83      19.453 -24.785 -13.366  1.00 63.47           C  
ATOM      8  CD2 LEU A  83      21.694 -24.676 -14.465  1.00 62.76           C  
ATOM      9  N   GLY A  84      22.709 -27.656  -9.980  1.00 70.39           N  
ATOM     10  CA  GLY A  84      23.266 -27.567  -8.627  1.00 73.87           C  
ATOM     11  C   GLY A  84      24.722 -27.969  -8.445  1.00 74.98           C  
...
TRE
```
2. run_LS.py
```
python run_LS.py
```
## Examples of results
```
Ranking	    Compound ID	        Rescore
1	active_CHEMBL4100838	0.8648
2	active_CHEMBL4068526	0.8633
3	active_CHEMBL2023494	0.854
4	active_CHEMBL4074076	0.85
5	active_CHEMBL1171837	0.8492
6	active_CHEMBL4059858	0.8461
7	active_CHEMBL4847875	0.844
8	active_CHEMBL4063659	0.8425
9	active_CHEMBL5197530	0.842
10	active_CHEMBL3646210	0.8396
11	active_CHEMBL4085366	0.8396
12	active_CHEMBL5186979	0.8373
13	active_CHEMBL3646211	0.8342
14	active_CHEMBL4466555	0.8326
15	active_CHEMBL4583679	0.8322
16	active_CHEMBL4851635	0.8318
17	active_CHEMBL4471379	0.8313
18	active_CHEMBL4081527	0.8303
19	active_CHEMBL4436123	0.8299
20	active_CHEMBL475817	0.8297
```
