import os
import tempfile
from typing import Any, Union

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log, summa


@pytest.mark.parametrize(
    "x, y, expected",
    [(1, 2, 3), (0, 6, 6), (-3, 5.3, 2.3)],
)
def test_log(capsys: CaptureFixture, x: Union[int, float], y: Union[int, float], expected: Union[int, float]) -> None:
    result = summa(x, y)
    assert result == expected
    captured = capsys.readouterr()
    assert f"Функция 'summa' начала работу с входными параметрами: ({x}, {y}), {{}}" in captured.out
    assert "Результат работы:" in captured.out
    assert "Функция 'summa' окончила работу успешно\n" in captured.out


@pytest.mark.parametrize("x, y", [(1, "1"), ([], {})])
def test_log_error(capsys: CaptureFixture, x: Any, y: Any) -> None:
    with pytest.raises(Exception):
        summa(x, y)
    captured = capsys.readouterr()
    assert "Произошла ошибка" in captured.out
    assert "Функция 'summa' окончила работу" in captured.out


@pytest.mark.parametrize("x1, y1, expected1", [(1, 2, 3), (3, 4, 7)])
def test_log_to_file(x1: int, y1: int, expected1: int) -> None:
    filename = "some_placeholder"
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name

    try:
        decorated_summa = log(filename=filename)(summa)
        result = decorated_summa(x1, y1)

        assert result == expected1

        with open(filename, "r") as f:
            content = f.read()

        assert f"Функция 'summa' начала работу с входными параметрами: ({x1}, {y1}), {{}}" in content
        assert f"Результат работы:{expected1}" in content
        assert "Функция 'summa' окончила работу успешно" in content

    finally:
        os.remove(filename)


@pytest.mark.parametrize(
    "x, y",
    [
        ("a", "2"),
        ([], {}),
    ],
)
def test_log_to_file_error(x: Any, y: Any) -> None:
    filename = "some_placeholder"
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name

    decorated_summa = log(filename=filename)(summa)

    try:
        decorated_summa(x, y)
    except Exception:
        with open(filename, "r") as f:
            content = f.read()

        assert f"Функция 'summa' начала работу с входными параметрами: ({x}, {y}), {{}}" in content
        assert "Произошла ошибка " in content
        assert "Функция 'summa' окончила работу" in content

    finally:
        os.remove(filename)
