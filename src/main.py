from src.nlp.nlp import nlp0
from src.nlp.nlp import nlp1
from src.get_background_graph.subgraph import subgraph
from src.get_background_graph.background import background
from src.get_background_graph.background_graph import background_graph

from src.matrix.background_standard import background_standard
from src.matrix.degree1 import pre_degree1
from src.matrix.degree1 import degree1

from src.matrix.degree2 import degree2
from src.matrix.processing_diagonal import processing_diagonal
from src.similarity.sim_deg import sim_deg
from src.layer_divided.one_word_case import one_word_case
from src.layer_divided.no_sharing_word import no_sharing_word
import numpy as np


def main(cn_layer):
    c = []
    counter = 0
    for a in cn_layer:
        if counter < 2:
            c.append(nlp0(a))  # 自然语言处理过后的layer 进行other处理
        else:
            c.append(nlp1(a))
        counter += 1
    # print(c)
    cn_sub_graph = []
    for a in c:
        cn_sub_graph.append(subgraph(a))
        # 将layer中重复的单词删掉到只剩一个，并赋给权值.

    # 进行layer分层处理
    cn_sub_graph = one_word_case(cn_sub_graph)

    cn_sub_graph = no_sharing_word(cn_sub_graph)
    cn_sub_graph = background(cn_sub_graph)
    # 在同一个layer中，把两个vertex形成边，并赋给边权值。
    # 并且对于(vertex1,vertex2),vertex1<vertex2

    cn_background = background_graph(cn_sub_graph)
    # 把不同layer中的相同的边删除到只剩一个，并赋给权值
    vertex1, cn_list_edge, cn_list_weight = background_standard(cn_background)
    # 把顶点symbolize,这里list_edge的size是list_weight的2倍
    cn_matrix = pre_degree1(cn_list_edge, cn_list_weight, cn_background)
    # 产生初始化矩阵，把边的权值填入
    cn_matrix1 = degree1(cn_matrix)
    # 把degree1的值填入
    # print(np.around(cn_matrix1, decimals=3))
    cn_matrix1 = processing_diagonal(cn_matrix1)
    # 将对角线全置为1
    cn_matrix2 = degree2(cn_matrix1)
    # 把degree2的值填入
    # print(np.around(cn_matrix2,decimals=1))
    return vertex1, cn_matrix2


def result(cn_layer, us_layer):
    cn_layer = cn_layer
    us_layer = us_layer
    vertex1, a = main(cn_layer)
    vertex2, b = main(us_layer)

    result1 = sim_deg(vertex1, a, vertex2, b)
    print(result1, end='\n')
    return result1






