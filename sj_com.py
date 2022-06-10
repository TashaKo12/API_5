from itertools import count
from collections import defaultdict

import requests




def predict_rub_salary(salary_from=None, salary_to=None):
    if salary_from and salary_to:
        expected_salary = int(salary_to + salary_from) / 2
    elif salary_to:
        expected_salary = salary_to * 1.2
    elif salary_from:
        expected_salary = salary_from * 0.8
    return expected_salary


def get_vacancies_sj(key, language="Python", page=0):
    url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {
        "X-Api-App-Id": key
    }

    params = {
        "town": "Moscow",
        "period": 30,
        "catalogues": 48,
        "keyword": language,
        "page": page
    }
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def get_language_statistics_sj(language, superjob_key):
    count_used = 0
    average_salaries = []
    for page in count(0, 1):
        response = get_vacancies_sj(superjob_key, language, page=page)

        for vacancy in response["objects"]:
            if not vacancy["payment_from"] or vacancy["payment_to"]:
                continue
            if not vacancy["currency"] == "rub":
                continue
            average_salaries.append(predict_rub_salary(
                vacancy["payment_from"],
                vacancy["payment_to"]
            ))
            count_used += 1

        if not response["more"]:
            break

    vacancy_count = response["total"]
    if len(average_salaries):
        average_salary = int(sum(average_salaries) / len(average_salaries))
    else:
        average_salary = "-"

    vacancies_for_language = {
        "vacancies_found": vacancy_count,
        "vacancies_processed": count_used,
        "average_salary": average_salary
    }
    return vacancies_for_language


def get_statistics_of_languages_sj(key, languages):
    statistics = defaultdict()
    for language in languages:
        statistics[language] = get_language_statistics_sj(language, key)
    return statistics



