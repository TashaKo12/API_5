import os

from terminaltables import AsciiTable
from dotenv import load_dotenv

from hh_ru import get_statistics_of_languages_hh
from sj_com import get_statistics_of_languages_sj

HH_TITLE = "HeadHunter Moscow"
SJ_TITLE = "SuperJob Moscow"


def create_table(title, statistics):
    table_data = [
        [
            "Язык программирования",
            "Вакансий найдено",
            "Вакансий обработано",
            "Средняя зарплата"
        ]
    ]
    for language, vacancies in statistics.items():
        table_data.append([
            language,
            vacancies["vacancies_found"],
            vacancies["vacancies_processed"],
            vacancies["average_salary"]
        ])
    table = AsciiTable(table_data, title)
    return table.table


def main():
    load_dotenv()
    superjob_key = os.getenv("SJ_KEY")

    languages = [
        "Python",
        "Java",
        "Javascript",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "C",
        "Go",
        "Shell"
    ]

    hh_table = create_table(
        HH_TITLE,
        get_statistics_of_languages_hh(
            languages
        )
    )

    sj_table = create_table(
        SJ_TITLE,
        get_statistics_of_languages_sj(
            superjob_key,
            languages
        )
    )
    print(f"{sj_table}\n{hh_table}")


if __name__ == "__main__":
    main()
   