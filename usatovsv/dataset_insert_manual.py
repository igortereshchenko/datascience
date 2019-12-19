import usatovsv.dataset_structure as d
def inp(dataset:dict(),zip_code,cb_num,wire_2nd,spc_latin):
    values = dict()

    values['cb_num']=cb_num

    values['wire_wnd']=wire_2nd

    values['spc_latin']=spc_latin

    dataset[zip_code]=values
    return dataset
print(inp(d.dataset,120,1,1,1))
