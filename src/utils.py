import json
import logging
import os
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    filename="../logs/utils.log",
    filemode="w",
)
utils_logger = logging.getLogger("utils")


def financial_transaction_data(path_to_the_JSON_file: str) -> Any:
    """Функция, считывающая JSON-файл и выводящая содержимое"""

    utils_logger.debug("Проверяем существует ли файл по указанному пути")
    if not os.path.exists(path_to_the_JSON_file):

        utils_logger.error("Файл по указанному пути не найден")
        return []

    try:
        utils_logger.debug("Считываем JSON-файл и возвращаем его содержимое")
        with open(path_to_the_JSON_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            utils_logger.info("Функция выполнена успешно")
            return data

    except (json.JSONDecodeError, FileNotFoundError) as ex:
        utils_logger.error(f"Произошла ошибка: {ex}")
        return []
