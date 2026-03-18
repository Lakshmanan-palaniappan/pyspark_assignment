def with_country(emp,country):
    return emp.join(country,emp.state==country.country_code)