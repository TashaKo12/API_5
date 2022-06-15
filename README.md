
# Моя будущая профессия
## Описание
Проект создан для загрузки данных о зарплатах различных программистов, в зависимости от языка программирования. Поиск производится по hh.ru и SuperJob. 


## Установка
Скачайте необходимые файлы, затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже.
Создайте бота у отца ботов. Создайте новый канал в Telegram.

Установите зависимости командой:
```python
  pip install -r requirements.txt
```

## Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.

Для получения необходимых изображений необходимо написать:

```python
  python table.py
```

## Переменные окружения
Часть настроек проекта берётся из переменных окружения. 
Переменные окружения - это переменные, значения которых присваиваются программе Python извне.
Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Пример содержания файла `.env`:

```python
SJ_KEY="SJ_KEY"
```

Получить токен `SJ_KEY` можно на сайте [API SuperJob](https://api.superjob.ru/). 

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
