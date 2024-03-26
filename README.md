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
```
20	active_CHEMBL475817	0.8297
