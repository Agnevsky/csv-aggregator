import pytest
import sys
from work_with_file import read_file
from parsargs import get_args


@pytest.mark.parametrize("expected_exception, file", [(FileNotFoundError, "file1.csv"), 
                                                      (FileNotFoundError, "../../namefil2.csv"),
                                                      (FileNotFoundError, "../../myfile.csv")])

def test_error_read_file(expected_exception, file):
    with pytest.raises(expected_exception):
        read_file(file)


@pytest.mark.parametrize("argv, expected_file", [
    (['get_args', '--file', 'test_file.csv'], 'test_file.csv'),
    (['get_args', '--file', 'none.csv'], 'none.csv'),
    (['get_args', '--file', 'none2.csv'], 'none2.csv'),
])
def test_parse_args_file(monkeypatch, argv, expected_file):
    monkeypatch.setattr(sys, 'argv', argv)
    args = get_args()
    assert args.file == expected_file


@pytest.mark.parametrize("argv, expected_file, expected_where", [
    (['get_args', '--file', 'test_file_cars.csv', '--where', 'EngineSize>1.5'], 'test_file_cars.csv', 'EngineSize>1.5'),
    (['get_args', '--file', 'test_file_cars.csv', '--where', 'Year=2015'], 'test_file_cars.csv', 'Year=2015'),
    (['get_args', '--file', 'test_file_cars.csv', '--where', 'PriceUSD<18000'], 'test_file_cars.csv', 'PriceUSD<18000'),
    (['get_args', '--file', 'test_file_cars.csv', '--where', 'Year<=2019'], 'test_file_cars.csv', 'Year<=2019'),
    (['get_args', '--file', 'test_file_cars.csv', '--where', 'PriceUSD>=22500'], 'test_file_cars.csv', 'PriceUSD>=22500'),
])
def test_parse_args_where(monkeypatch, argv, expected_file, expected_where):
    monkeypatch.setattr(sys, 'argv', argv)
    args = get_args()
    assert args.file == expected_file
    assert args.where == expected_where

