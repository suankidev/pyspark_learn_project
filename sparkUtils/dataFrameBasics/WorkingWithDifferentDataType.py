import pyspark.sql

from common_utils.sparkUtils import get_flight_df, get_spark_session, get_retail_data
from pyspark.sql.functions import lit, col, instr, round, bround, initcap, lower, upper
from pyspark.sql.functions import regexp_extract, regexp_replace, translate, locate, expr

'''
Booleans         --> make sure value is not null eeNullsagfe()
Numbers
Strings
Dates and timestamps
Handling null
Complex types
User-defined functions
'''


class WorkingWithDifferentDataType:
    retail_df = get_retail_data()

    @staticmethod
    def one():
        flight_df = get_flight_df()
        retail_df = get_retail_data()
        spark = get_spark_session()

        # retail_df.printSchema()
        '''root
 |-- InvoiceNo: string (nullable = true)
 |-- StockCode: string (nullable = true)
 |-- Description: string (nullable = true)
 |-- Quantity: integer (nullable = true)
 |-- InvoiceDate: string (nullable = true)
 |-- UnitPrice: double (nullable = true)
 |-- CustomerID: double (nullable = true)
 |-- Country: string (nullable = true)
 +---------+---------+-----------------------------------+--------+-------------------+---------+----------+--------------+
|InvoiceNo|StockCode|Description                        |Quantity|InvoiceDate        |UnitPrice|CustomerID|Country       |
+---------+---------+-----------------------------------+--------+-------------------+---------+----------+--------------+
|536365   |85123A   |WHITE HANGING HEART T-LIGHT HOLDER |6       |2010-12-01 08:26:00|2.55     |17850.0   |United Kingdom|
|536365   |71053    |WHITE METAL LANTERN                |6       |2010-12-01 08:26:00|3.39     |17850.0   |United Kingdom|
|536365   |84406B   |CREAM CUPID HEARTS COAT HANGER     |8       |2010-12-01 08:26:00|2.75     |17850.0   |United Kingdom|
|536365   |84029G   |KNITTED UNION FLAG HOT WATER BOTTLE|6       |2010-12-01 08:26:00|3.39     |17850.0   |United Kingdom|
|536365   |84029E   |RED WOOLLY HOTTIE WHITE HEART.     |6       |2010-12-01 08:26:00|3.39     |17850.0   |United Kingdom|
+---------+---------+-----------------------------------+--------+-------------------+---------+----------+--------------+
only showing top 5 rows
 '''

        # retail_df.show(5, False)
        '''Converting to Spark Types'''
        '''The lit function. This function converts a
type in another language to its correspnding Spark representation.'''

        df = retail_df.select(lit(5), lit('five'), lit(5.0))
        # df.show()

        '''Working with Booleans'''

        df = retail_df.where(col('InvoiceNo') == 536365).select(col('InvoiceNo'), col('Description'))

        price_filter = col('UnitPrice') > 600
        descriptor_filter = instr(col('description'), 'POSTAGE') >= 1

        retail_df.where(col('StockCode').isin('DOT')).where(price_filter | descriptor_filter)

        df.show(5, False)

        dot_code_filter = col("StockCode") == 'DOT'

        retail_df.withColumn('isExpensive', dot_code_filter & (price_filter | descriptor_filter)) \
            .where(col('isExpensive')).show(5, False)

        stock_code = {'DOT', '71053', 'test'}

        retail_df.where(col('StockCode').isin(*stock_code)).show(5, False)

        retail_df.where(not (dot_code_filter & (price_filter | descriptor_filter))).select('description',
                                                                                           'unitprice').show()

    @staticmethod
    def working_with_number():
        fabricated_value = pow(col('quantity') * col('UnitPrice'), 2) + 5
        df = retail_df.select(col('customerid'), fabricated_value.alias('realQuantity'))

        df = retail_df.select(round(lit(2.5)), bround(lit(2.5)))
        df.show(5, False)

    @staticmethod
    def working_with_string():
        retail_df = WorkingWithDifferentDataType.retail_df

        '''initcap to capatalise '''

        df = retail_df.select(initcap(col('Description')), lower(col('description')), upper(col('description')))
        df.show(2, False)

        from pyspark.sql.functions import ltrim, rtrim, trim, rpad, lpad

        '''Note that if lpad or rpad takes a number less than the length of the string, 
        it will always remove 
        values from the right side of the string'''

        df = retail_df.select(ltrim(lit('    hello    ')), rpad(lit('Hello'), 8, '--'))
        df.show(2, False)

    @staticmethod
    def working_with_regular_expression():
        retail_df = WorkingWithDifferentDataType.retail_df

        regex_string = 'BLACK|WHITE|RED|GREEN|BLUE'
        extract_string = '(BLACK|WHITE|RED|GREEN|BLUE)'
        extract_string_one = '(^WHITE)'

        # find regex_string  in description column and replace it with 'COLOR' value
        df = retail_df.select(regexp_replace(col('Description'), regex_string, 'COLOR').alias('color_clean'),
                              col('description'))

        df.show(5, False)

        # replace given characters with other characters

        df = retail_df.select(translate(col('description'), 'LEET', '1337'))

        df.show(5, False)

        # pulling out first mention color
        '''Extract a specific group matched by a Java regex, from the specified string column. 
        If the regex did not match, or the specified group did not match, an empty string is returned'''

        df = retail_df.select(regexp_extract(col('description'), extract_string, 1).alias('extract_column'),
                              col('description'))

        df.show(5, False)

        df = retail_df.select(regexp_extract(col('description'), extract_string_one, 1).alias('extract_column'),
                              col('description'))

        df.show(5, False)

        '''check if the description contain the value BLACK or WHITE'''

        filter_black = instr(col('description'), 'BLACK') >= 1
        filter_white = instr(col('description'), 'RED') >= 1

        df = retail_df.withColumn('has_simple_color', (filter_black | filter_white)).where('has_simple_color') \
            .select('description')

        df.show(5, False)

        '''what if we have multiple value to find in a column , if exist or not'''

        simple_color = ['black', 'red', 'white', 'green', 'blue']

        def color_locator(column, color_string):
            return locate(color_string.upper(), column) \
                .cast("boolean") \
                .alias("is_" + color_string)

        selected_columns = [color_locator(retail_df.Description, c) for c in simple_color]
        selected_columns.append(expr("*"))  # has to a be Column type
        df = retail_df.select(*selected_columns).where(expr("is_white OR is_red")) \
            .select("Description")

        df.show(3, False)

        df = retail_df.select(locate('RED', col('description')).alias('description_located'), col('description'))
        df.show(5, False)





def working_with_different_data_types():
    # WorkingWithDifferentDataType().one()
    # WorkingWithDifferentDataType.working_with_number()
    # WorkingWithDifferentDataType.working_with_string()
    WorkingWithDifferentDataType.working_with_regular_expression()
