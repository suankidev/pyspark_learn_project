from file_based_checks.cref.CrefTestPack import CrefTestPack

hdfs_path = "hdfs_location"
table_name = "d_fin_table"
location = 'cref'


def init_check():
    obj = None
    if location == 'cref':
        obj = CrefTestPack(hdfs_path, table_name)
        return obj
    return obj



init_object = init_check()
init_object.run_test()
