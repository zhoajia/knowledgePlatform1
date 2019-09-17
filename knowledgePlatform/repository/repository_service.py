# 仓库 service
from knowledgePlatform.repository.models import RepositoryEntity
import datetime


# 查询所有的仓库
def get_all_repository(repository_type_arg, repository_level):
    query_set_list = RepositoryEntity.objects.filter(repository_type=repository_type_arg, level=repository_level)
    l = []
    for item in query_set_list:
        d = dict()
        d["repository_name"] = item.repository_name
        d["id"] = item.id
        d["is_active"] = "生效" if item.is_active == 1 else "失效"
        d["create_date"] = item.create_date.strftime('%Y-%m-%d %H:%M:%S')
        d["update_date"] = item.update_date.strftime('%Y-%m-%d %H:%M:%S')
        d["flag"] = 1

        sub_l = []
        query_set_sub_list = RepositoryEntity.objects.filter(parent_id=item.id)
        for sub_item in query_set_sub_list:
            sub_d = dict()
            sub_d["repository_name"] = sub_item.repository_name
            sub_d["id"] = sub_item.id
            sub_d["is_active"] = "生效" if sub_item.is_active == 1 else "失效"
            sub_d["create_date"] = sub_item.create_date.strftime('%Y-%m-%d %H:%M:%S')
            sub_d["update_date"] = sub_item.update_date.strftime('%Y-%m-%d %H:%M:%S')
            sub_l.append(sub_d)

        d['children'] = sub_l

        l.append(d)
    return l


def repository_create(repository_entity:RepositoryEntity):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    repository_entity.create_date = date
    repository_entity.update_date = date
    repository_entity.save()
    return "ok"
