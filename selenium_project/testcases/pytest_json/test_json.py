import json
import pytest
import os


def get_json_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data['keys']

data_json_0 = get_json_data(
    r'.\testcases\pytest_json\test.json')




# 假设我们有一个函数需要测试，这里我们简单地返回输入的数据

def process_data(data):
    return data

# 使用 pytest.mark.parametrize 方法传入数据


@pytest.mark.parametrize("data", data_json_0)
    
def test_process_data(data):
    assert process_data(data) == data




if __name__ == '__main__':
    print(os.getcwd())
