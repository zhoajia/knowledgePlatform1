from django.core.paginator import Paginator


def has_same_column(obj, colunm_name, colunm_value):
    pass


class ResultDate:
    """
    分页数据分装 \n
    total、obj属性请勿直接调用;\n
    total->总数量\n
    obj->对象列表\n
    """
    __total = 0
    __obj = None

    def __init__(self, total, obj):
        self.total = total
        self.obj = obj


def find_by_page(query_set_list, page_number):
    """
    分页工具类
    固定按10个每页
    :param query_set_list: 查询出来的query_set对象
    :param page_number: 页码
    :return: 分页好的对象 ， 总个数
    """
    total = len(query_set_list)
    paginator = Paginator(query_set_list, 10)
    result_list = paginator.page(page_number).object_list
    return result_list, total
