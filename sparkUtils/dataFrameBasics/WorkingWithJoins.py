from common_utils.sparkUtils import get_spark_session


class WorkingWithJoins:

    def __init__(self):
        self.spark = get_spark_session()
        self.emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
                    (2, "Rose", 1, "2010", "20", "M", 4000), \
                    (3, "Williams", 1, "2010", "10", "M", 1000), \
                    (4, "Jones", 2, "2005", "10", "F", 2000), \
                    (5, "Brown", 2, "2010", "40", "", -1), \
                    (6, "Brown", 2, "2010", "50", "", -1) \
                    ]
        self.empColumns = ["emp_id", "name", "superior_emp_id", "year_joined", \
                           "emp_dept_id", "gender", "salary"]

        self.empDF = self.spark.createDataFrame(data=self.emp, schema=self.empColumns)
        # empDF.printSchema()
        # empDF.show(truncate=False)

        self.dept = [("Finance", 10),
                     ("Marketing", 20),
                     ("Sales", 30),
                     ("IT", 40)
                     ]
        self.deptColumns = ["dept_name", "dept_id"]
        self.deptDF = self.spark.createDataFrame(data=self.dept, schema=self.deptColumns)

    def working_with_inner_join(self):
        emp_df = self.empDF
        dept_df = self.deptDF

        emp_df.show()
        dept_df.show()

        #emp_df.join(dept_df, emp_df.emp_dept_id == dept_df.dept_id, "inner").show(10, False)

        #all are same
        #emp_df.join(dept_df, emp_df.emp_dept_id == dept_df.dept_id, "outer").show(10, False)
        #emp_df.join(dept_df, emp_df.emp_dept_id == dept_df.dept_id, "full").show(10, False)
        #emp_df.join(dept_df, emp_df.emp_dept_id == dept_df.dept_id, "fullouter").show(10, False)

        #left outer join both are same
        emp_df.join(dept_df, emp_df.emp_dept_id == dept_df.dept_id, "left").show(10, False)
        emp_df.join(dept_df, emp_df.emp_dept_id == dept_df.dept_id, "leftouter").show(10, False)








def working_with_join():
    obj = WorkingWithJoins()
    obj.working_with_inner_join()


"""
+------+--------+---------------+-----------+-----------+------+------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|
+------+--------+---------------+-----------+-----------+------+------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|
|     2|    Rose|              1|       2010|         20|     M|  4000|
|     3|Williams|              1|       2010|         10|     M|  1000|
|     4|   Jones|              2|       2005|         10|     F|  2000|
|     5|   Brown|              2|       2010|         40|      |    -1|
|     6|   Brown|              2|       2010|         50|      |    -1|
+------+--------+---------------+-----------+-----------+------+------+

+---------+-------+
|dept_name|dept_id|
+---------+-------+
|  Finance|     10|
|Marketing|     20|
|    Sales|     30|
|       IT|     40|
+---------+-------+


:inner join  --> 30 and 50 is not there
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|name    |superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|1     |Smith   |-1             |2018       |10         |M     |3000  |Finance  |10     |
|3     |Williams|1              |2010       |10         |M     |1000  |Finance  |10     |
|4     |Jones   |2              |2005       |10         |F     |2000  |Finance  |10     |
|2     |Rose    |1              |2010       |20         |M     |4000  |Marketing|20     |
|5     |Brown   |2              |2010       |40         |      |-1    |IT       |40     |
+------+--------+---------------+-----------+-----------+------+------+---------+-------+

:outer --> full outer, outer ,full
Outer a.k.a full, fullouter join returns all rows from both datasets, where join expression doesn’t match it returns null on respective record columns.

+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|name    |superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|6     |Brown   |2              |2010       |50         |      |-1    |null     |null   |
|1     |Smith   |-1             |2018       |10         |M     |3000  |Finance  |10     |
|3     |Williams|1              |2010       |10         |M     |1000  |Finance  |10     |
|4     |Jones   |2              |2005       |10         |F     |2000  |Finance  |10     |
|null  |null    |null           |null       |null       |null  |null  |Sales    |30     |
|2     |Rose    |1              |2010       |20         |M     |4000  |Marketing|20     |
|5     |Brown   |2              |2010       |40         |      |-1    |IT       |40     |
+------+--------+---------------+-----------+-----------+------+------+---------+-------+

:Left a.k.a Leftouter join returns all rows from the left dataset regardless of match found on the right dataset 
when join expression doesn’t match, it assigns null for that record and drops records from right where match not found

+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|name    |superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|6     |Brown   |2              |2010       |50         |      |-1    |null     |null   |
|1     |Smith   |-1             |2018       |10         |M     |3000  |Finance  |10     |
|3     |Williams|1              |2010       |10         |M     |1000  |Finance  |10     |
|4     |Jones   |2              |2005       |10         |F     |2000  |Finance  |10     |
|2     |Rose    |1              |2010       |20         |M     |4000  |Marketing|20     |
|5     |Brown   |2              |2010       |40         |      |-1    |IT       |40     |
+------+--------+---------------+-----------+-----------+------+------+---------+-------+




"""
