import os
for i in range(1,201):
    file_n='/data/Mukuo/A1AR/ucsf_redock/active_better_result/'+'active'+str(i)+'_out_ligand_1'+'.mol2'
    out_n='/data/Mukuo/A1AR/ucsf_redock/active_decoy_mol2_for_plscore/'+'active'+str(i)+'_out_ligand_1'+'.mol2'
    comand='scp -r %s %s' % (file_n,out_n)
    os.system(comand)