from src.main import result
from src.input_data.input_data import test_cn_layer, test_us_layer

if __name__ == '__main__':
    result(test_cn_layer, test_us_layer[0])

    # for i in test_us_layer:
    #
    #     result(test_cn_layer, i)


