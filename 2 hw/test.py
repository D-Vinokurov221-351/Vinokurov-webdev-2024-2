import subprocess
import pytest
import sys

from people_sort import sort_people_by_age, Person

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact': [
        (5, 120),
        (0, 1),
        (6, 720),
        (4, 24),
        (30, 265252859812191058636308480000000)
    ],
    'show_employee': [
        (['Иванов Иван Иванович', '30000'], 'Иванов Иван Иванович: 30000 ₽'),
        (['Иванов Иван Иванович', '100000'], 'Иванов Иван Иванович: 100000 ₽'),
        (['Иванов Иван Иванович', '-1'], 'Иванов Иван Иванович: -1 ₽')
    ],
    'show_employee_short': [
        ('Иванов Иван Иванович', 'Иванов Иван Иванович: 100000 ₽'),
        ('Иванов Иван', 'Иванов Иван: 100000 ₽')
    ],
    'sum_and_sub': [
        ([1,2],(3, -1)),
        ([5,8],(13, -3)),
        ([9,4],(13, 5)),
        ([100,-3],(97, 103)),
        ([250,170],(420, 80))
    ],
    'my_sum': [
        ([1, 2, 3, 4, 5, 15],30),
        ([10, 20, 30, 40, 50, 150],300),
        ([2.5, 3.5, 4.5, 5.5, 16],32),
        ([1, 1, 1, -3],0),
        ([-1, -1, -1, -3],-6)
    ],
    'email_validation': [
        (['lara@mospolytech.ru','brian-23@mospolytech.ru','britts_54@mospolytech.ru','invalid_email'],['lara@mospolytech.ru', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.ru']),
        (['lara@mospolytech.ru','brian-23@mospolytech.ru','britts_54@mospolytech.ru'],['lara@mospolytech.ru', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.ru']),
        (['lara_mospolytech.ru','brian-23_mospolytech.ru','britts_54_mospolytech.ru','invalid_email'],[]),
        (['donpablo@krasauchick.ru'],['donpablo@krasauchick.ru'])
    ],
    'average_scores': [
        ([(89, 90, 78), (90, 91, 85), (91, 92, 83, 89, 90.5)], (90.0, 91.0, 82.0)),
        ([(89, 90, 78), (90, 91, 85), (91, 92, 83, 89, 90.5)], (90.0, 91.0, 82.0)),
        ([(89, 90, 78), (90, 91, 85), (91, 92, 83, 89, 90.5)], (90.0, 91.0, 82.0))
    ],
    'phone_numbers': [
        (3, ['8895462130', '89875641230', '89195969878'], ['+7 (895) 462-13-0', '+7 (987) 564-12-30', '+7 (919) 596-98-78']),
        (3, ['07895462130', '079875641230', '079195969878'], ['+7 (895) 462-13-0', '+7 (987) 564-12-30', '+7 (919) 596-98-78']),
        (3, ['995462130', '9875641230', '9195969878'], ['+7 (995) 462-13-0', '+7 (987) 564-12-30', '+7 (919) 596-98-78']),
        (3, ['08895462130', '89875641230', '9195969878'], ['+7 (895) 462-13-0', '+7 (987) 564-12-30', '+7 (919) 596-98-78'])
    ],
    'people': [
        (3, [Person('Mike', 'Thomson', 20, 'M'), 
             Person('Robert', 'Bustle', 32, 'M'), 
             Person('Andria', 'Bustle', 30, 'F')], 
         ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']),
         (3, [Person('Mike', 'Thomson', 20, 'M'), 
             Person('Robert', 'Bustle', 23, 'M'), 
             Person('Andria', 'Bustle', 23, 'F')], 
         ['Mr. Mike Thomson', 'Mr. Robert Bustle', 'Ms. Andria Bustle']),
         (3, [Person('Don', 'Pablo', 20, 'F'), 
             Person('Robert', 'Bustle', 32, 'M'), 
             Person('Andria', 'Bustle', 30, 'F')], 
         ['Ms. Don Pablo', 'Ms. Andria Bustle', 'Mr. Robert Bustle'])
    ],
    'complex_numbers': [
        ((2, 1), (5, 6), (7.00+7.00j, -3.00-5.00j, 4.00+17.00j, 0.26229508196721313-0.11475409836065571j, '2.24+1.00i', '7.81+6.00i')),
        ((2, 4), (9, 6), (11+10j, -7-2j, -6+48j, 0.3589743589743589+0.20512820512820515j, '4.47+4.00i', '10.82+6.00i')),
        ((2, 8), (2, 6), (4+14j, 2j, -44+28j, 1.2999999999999998+0.09999999999999998j, '8.25+8.00i', '6.32+6.00i'))
    ],
    'circle_square_mk': [
        (1, 1000000, 3.140808),
        (2, 1000000, 12.5764),
        (3, 1000000, 28.271808),
        (4, 1000000, 50.23744)
    ]
}

from fact import fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from my_sum import my_sum
from my_sum_argv import my_sum_argv
from files_sort import files_sort
from file_search import file_search
from email_validation import filter_mail
from fibonacci import fibonacci
from average_scores import compute_average_scores
from plane_angle import Point, plane_angle
from phone_number import format_phone_numbers
from complex_numbers import complex_numbers
from circle_square_mk import circle_square_mk


@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(input_data[0],input_data[1]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['show_employee_short'])
def test_show_employee_short(input_data, expected):
    assert show_employee(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(input_data[0],input_data[1]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected

def test_my_sum_argv(capsys):
    sys.argv = ['my_sum_argv.py', '1', '2', '3', '4']
    my_sum_argv()
    captured = capsys.readouterr()
    assert float(captured.out.strip()) == 10

def test_my_sum_argv_empty(capsys):
    sys.argv = ['my_sum_argv.py']
    my_sum_argv()
    captured = capsys.readouterr()
    assert float(captured.out.strip()) == 0

def test_my_sum_argv_negative_numbers(capsys):
    sys.argv = ['my_sum_argv.py', '-1', '-2', '-3']
    my_sum_argv()
    captured = capsys.readouterr()
    assert float(captured.out.strip()) == -6

def test_my_sum_argv_mixed_numbers(capsys):
    sys.argv = ['my_sum_argv.py', '1.5', '2', '-3.5']
    my_sum_argv()
    captured = capsys.readouterr()
    assert float(captured.out.strip()) == 0.0

def test_files_sort_first(capsys):
    sys.argv = ['files_sort.py', 'test/first']
    files_sort('test/first')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'a.txt\nb.txt\nc.txt'

def test_files_sort_second(capsys):
    sys.argv = ['files_sort.py', 'test/second']
    files_sort('test/second')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'ashop.txt\nbshop.txt\ncshop.txt'

def test_files_sort_third(capsys):
    sys.argv = ['files_sort.py', 'test/third']
    files_sort('test/third')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'arena.txt\nbomb.txt\ncisco.txt'

def test_files_sort_fourth(capsys):
    sys.argv = ['files_sort.py', 'test/third']
    files_sort('test/fourth')
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

def test_file_search_first(capsys):
    sys.argv = ['file_search.py']
    file_search('a.txt')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'a\nf\ni\nl\ne'

def test_file_search_second(capsys):
    sys.argv = ['file_search.py']
    file_search('ashop.txt')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'ashop\nf\ni\nl\ne'

def test_file_search_third(capsys):
    sys.argv = ['file_search.py']
    file_search('arena.txt')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'arena\nf\ni\nl\ne'

def test_file_search_fourth(capsys):
    sys.argv = ['file_search.py']
    file_search('cisco.txt')
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

def test_file_search_fourth(capsys):
    sys.argv = ['file_search.py']
    file_search('uncensured.txt')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Файл uncensured.txt не найден'

@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    assert filter_mail(input_data) == expected

def test_fibonacci_first(capsys):
    sys.argv = ['fibonacci.py']
    fibonacci(3)
    captured = capsys.readouterr()
    assert captured.out.strip() == '[0, 1, 1]'

def test_fibonacci_second(capsys):
    sys.argv = ['fibonacci.py']
    fibonacci(5)
    captured = capsys.readouterr()
    assert captured.out.strip() == '[0, 1, 1, 8, 27]'

def test_fibonacci_third(capsys):
    sys.argv = ['fibonacci.py']
    fibonacci(8)
    captured = capsys.readouterr()
    assert captured.out.strip() == '[0, 1, 1, 8, 27, 125, 512, 2197]'

def test_fibonacci_fourth(capsys):
    sys.argv = ['fibonacci.py']
    fibonacci(10)
    captured = capsys.readouterr()
    assert captured.out.strip() == '[0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]'

@pytest.mark.parametrize("input_data, expected", test_data['average_scores'])
def test_compute_average_scores(input_data, expected):
    assert compute_average_scores(input_data) == expected

def test_plane_angle_first():
    assert plane_angle(Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(1, 1, 1)) == 90.0

def test_plane_angle_second():    
    assert plane_angle(Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 6), Point(3, 0, 0)) == 180.0

def test_plane_angle_third():    
    assert plane_angle(Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 1), Point(0, 1, 1)) == 0.0

@pytest.mark.parametrize("N, phone_numbers, expected", test_data['phone_numbers'])
def test_format_phone_numbers(N, phone_numbers, expected):
    assert format_phone_numbers(N, phone_numbers) == expected

@pytest.mark.parametrize("N, people, expected", test_data['people'])
def test_sort_people_by_age(N, people, expected):
    assert sort_people_by_age(N, people) == expected

@pytest.mark.parametrize("a, b, expected", test_data['complex_numbers'])
def test_complex_numbers(a, b, expected):
    assert complex_numbers(a, b) == expected

@pytest.mark.parametrize("r, n, expected", test_data['circle_square_mk'])
def test_circle_square_mk(r, n, expected):
    assert abs(circle_square_mk(r, n) - expected) < 0.08













