from file_based_checks.common.RunTest import RunTest


class CrefTestPack(RunTest):

    def create_stg_df(self):
        pass

    def create_final_df(self):
        pass

    def create_file_df(self):
        pass

    def run_test(self):
        print(f"file_path {self.file_path}")
        print(f"table_name {self.table_name}")

    def __init__(self, file_path, table_name):
        self.file_path = file_path
        self.table_name = table_name


# obj = CrefTestPack('hdfs_file_path', 'd_fin_table')
