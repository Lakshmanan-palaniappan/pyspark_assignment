from pyspark.sql.functions import col
def filter_m(emp,dept):
    return emp.join(dept,emp.department==dept.dept_id)\
        .filter(col("employee_name").startswith("m"))