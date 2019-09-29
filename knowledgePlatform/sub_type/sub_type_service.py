from knowledgePlatform.sub_type.models import SubType
from knowledgePlatform.top_type.models import TopType


def get_all_sub_type(active):
    sub_type_list = SubType.objects.filter(is_active=active)
    return sub_type_list
