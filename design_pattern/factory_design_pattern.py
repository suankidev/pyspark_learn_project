from file_based_checks.ups1.CrefTestPack import CrefTestPack
from file_based_checks.ups2.GatewayCheck import GatewayCheck

hdfs_path = "hdfs_location"
table_name = "d_fin_table"
location = 'GATEWAY'

argument_list = {'hdfs_file': hdfs_path, 'table_name': table_name, 'location': location}


def init_check(checks='Default'):
    factory = {
        'GATEWAY': GatewayCheck,
        'CREF': CrefTestPack
    }

    return factory[checks](argument_list)


init_check(location).run_test()
