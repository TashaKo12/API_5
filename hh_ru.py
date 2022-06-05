from collections import defaultdict
from itertools import count

import requests 


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


def static_hh_ru(language):
    for page in count(0, 1):
        response = get_vacancies_hh(language, page=page)
        vacancies_count = response["found"]
        if page >= response["pages"] - 1:
            break
    return vacancies_count

def get_statistics_of_languages_hh(languages):
    statistics = defaultdict()
    for language in languages:
        statistics[language] = static_hh_ru(language)
    return statistics


def main():
    languages = [
        "Python",
        "Java",
        "Javascript",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "Cobol",
        "Go",
        "Shell"
    ]

    print(get_statistics_of_languages_hh(languages))

if __name__ == "__main__":
    main()