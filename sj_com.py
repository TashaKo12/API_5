from itertools import count
from collections import defaultdict

import requests

from salary import predict_rub_salary


def get_sj_vacancies(key, language="Python", page=0):
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


def get_language_sj_statistics(language, superjob_key):
    average_salaries = []
    for page in count(0, 1):
        response = get_sj_vacancies(superjob_key, language, page=page)

        for vacancy in response["objects"]:
            if not (vacancy["payment_from"] or vacancy["payment_to"]):
                continue
            if not vacancy["currency"] == "rub":
                continue
            average_salaries.append(predict_rub_salary(
                vacancy["payment_from"],
                vacancy["payment_to"]
            ))

        if not response["more"]:
            break

    vacancy_count = response["total"]
    if len(average_salaries):
        average_salary = int(sum(average_salaries) / len(average_salaries))
    else:
        average_salary = None

    vacancies_for_language = {
        "vacancies_found": vacancy_count,
        "vacancies_processed": len(average_salaries),
        "average_salary": average_salary
    }
    return vacancies_for_language


def get_statistics_of_sj_languages(key, languages):
    statistics = defaultdict()
    for language in languages:
        statistics[language] = get_language_sj_statistics(language, key)
    return statistics


