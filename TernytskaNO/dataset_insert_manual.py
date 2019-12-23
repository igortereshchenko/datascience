import TernytskaNO.dataset_structure as ds

def new_line(dataset, lat_spc, status, c_year, w_prime):
    dataset.update({
        lat_spc: {
            "status": status
            ,"cen-year": c_year
            ,"wire-prime": w_prime
              }
                 }
                 )

new_line(ds.tree_census, "Tilia Americana", "dead", 2006, "Yes")
new_line(ds.tree_census, "Acer Platanodies", "good", 2005, "No")
new_line(ds.tree_census, "Pyrys Calleryana", "excellent", 2005, "No")
print(ds.tree_census)