from collections import defaultdict
from itertools import count

import requests

from salary import predict_rub_salary


def get_vacancies_hh(language="Python", page=0):
    link_hh = "https://api.hh.ru/vacancies/"
    params = {
        "specialization": "1.221",
        "area": "1",
        "period": 30,
        "text": language,
        "page": page
    }
    response = requests.get(link_hh, params=params)
    response.raise_for_status()
    return response.json()


def found_static_hh_ru(language="Python"):
    average_salaries = []
    for page in count(0, 1):
        response = get_vacancies_hh(language, page=page)

        if page >= response["pages"] - 1:
            break
        
        for vacancy in response["items"]:
            if not vacancy["salary"]:
                continue
            if not vacancy["salary"]["currency"] == "RUR":
                continue
            average_salaries.append(predict_rub_salary(
                vacancy["salary"]["from"],
                vacancy["salary"]["to"]
            ))
    vacancy_count = response["found"]

    if len(average_salaries):
        average_salary = int(sum(average_salaries) / len(average_salaries))
    else:
        average_salary = "-"

    found_information_hh_ru = {
        "vacancies_found": vacancy_count,
        "vacancies_processed": len(average_salaries),
        "average_salary": average_salary
    }

    return found_information_hh_ru



def get_statistics_of_languages_hh(languages):
    statistics = defaultdict()
    for language in languages:
        statistics[language] = found_static_hh_ru(language)
    return statistics

