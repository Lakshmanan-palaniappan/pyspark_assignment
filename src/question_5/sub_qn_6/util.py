def joins(emp,dept):
    return emp.join(dept,emp.department==dept.dept_id)