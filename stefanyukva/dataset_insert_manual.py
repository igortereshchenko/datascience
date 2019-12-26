import stefanyukva.dataset_structure as d_struct

def add_str(dataset: dict, boroname: str, cb_num: int, st_accem: int, st_senate: int):
    dataset[boroname]={
        d_struct.CB_NUM: cb_num,
        d_struct.ST_ACCEM: st_accem,
        d_struct.ST_SENATE: st_senate,

    }

#if __name__ == "__main__":
