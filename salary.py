def predict_rub_salary(salary_from=None, salary_to=None):
    if salary_from and salary_to:
        expected_salary = int(salary_to + salary_from) / 2
    elif salary_to:
        expected_salary = salary_to * 1.2
    elif salary_from:
        expected_salary = salary_from * 0.8
    return expected_salary
