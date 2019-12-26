import TernytskaNO.integratoin.dataset_stucture_common as ds
import TernytskaNO.validator.lib as lib_1
import PindaMV.validator.lib as lib_2

def new_line(dataset, lat_spc, c_year, status, w_other, inf, w_prime):
    dataset.update({
        lat_spc: {
                "status": status
                ,"cen-year": c_year
                ,"wire-other": w_other
                ,"inf-other": inf
                ,"wire-prime": w_prime

                 }
                    }
    )



def spc_latin_val(text = ""):
    new_str = input(text)
    while not lib_1.spc_latin_validator(new_str):
        new_str = input(text)
    return str(new_str)


def cen_year_val(text = ""):
    new_str = input(text)
    while not lib_1.cen_year_validator(new_str):
        new_str = input(text)
    return str(new_str)


def status_val(text = ""):
    new_str = input(text)
    while not lib_1.status_validator(new_str):
        new_str = input(text)
    return str(new_str)


def wire_other_val(text = ""):
    new_str = input(text)
    while not lib_2.wire_other_validator(new_str):
        new_str = input(text)
    return str(new_str)


def inf_other_val(text = ""):
    new_str = input(text)
    while not lib_2.inf_other_validator(new_str):
        new_str = input(text)
    return str(new_str)


def wire_prime_val(text = ""):
    new_str = input(text)
    while not lib_1.wire_prime_validator(new_str):
        new_str = input(text)
    return str(new_str)


lat_spc = spc_latin_val("Введіть латинську назву: ")
c_year = cen_year_val("Введіть рік: ")
status = status_val("Введіть стан: ")
w_other = wire_other_val("Чи є гілки: ")
inf = inf_other_val("Чи є конфлікти з інфраструктурою: ")
w_prime = wire_prime_val("Чи є інші гілки: ")

new_line(ds.tree_census, lat_spc, c_year, status, w_other, inf, w_other)
print(ds.tree_census)