import pytest
import csv
import os
os.chdir(os.path.dirname(__file__))

def read_csv_data(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            yield row

@pytest.mark.parametrize("x,y,z", read_csv_data('./csv_data/ddt.csv'))
def test_add(x,y,z):
    assert int(x) + int(y) < int(z)

if __name__ == '__main__':
    #data_list_0 = read_csv_data('./testcases/pytest_csv_ddt/csv_data/ddt.csv') 
        # 处理文件内容

    #print(data_list_0)
    pytest.main(['-s', 'test_csv_ddt.py'])


