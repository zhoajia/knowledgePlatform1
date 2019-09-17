from knowledgePlatform.webservice.models import WebServiceEntity
from knowledgePlatform.webservice.models import WebServiceParam
from knowledgePlatform.repository.models import RepositoryEntity
import datetime


def get_all_webservice(repository_id):
    query_webservice_set = WebServiceEntity.objects.filter(is_active=1, parent=repository_id)
    l = []
    for item in query_webservice_set:
        d = dict()
        d['id'] = item.id
        d['webservice_name'] = item.webservice_name
        d['webservice_desc'] = item.webservice_desc
        d['webservice_html'] = item.webservice_html
        d['webservice_res_desc'] = item.webservice_res_desc
        d['desc'] = item.desc

        sub_a_l = []
        query_webservice_param_a_set = WebServiceParam.objects.filter(is_active=1, webservice=item.id, type=1)
        for sub_a_item in query_webservice_param_a_set:
            sub_a_d = dict()
            sub_a_d['id'] = sub_a_item.id
            sub_a_d['param_name'] = sub_a_item.param_name
            sub_a_d['param_value'] = sub_a_item.param_value
            sub_a_l.append(sub_a_d)

        d['a'] = sub_a_l

        sub_b_l = []
        query_webservice_param_b_set = WebServiceParam.objects.filter(is_active=1, webservice=item.id, type=2)
        for sub_b_item in query_webservice_param_b_set:
            sub_b_d = dict()
            sub_b_d['id'] = sub_b_item.id
            sub_b_d['param_name'] = sub_b_item.param_name
            sub_b_d['param_value'] = sub_b_item.param_value
            sub_b_l.append(sub_b_item)

        d['b'] = sub_b_l

        l.append(d)
    return l


def get_webservice_info_by_id(webservice_id):
    webservice_entity = WebServiceEntity.objects.get(id=webservice_id)
    d = dict()
    d['id'] = webservice_entity.id
    d['webservice_name'] = webservice_entity.webservice_name
    d['webservice_desc'] = webservice_entity.webservice_desc
    d['webservice_html'] = webservice_entity.webservice_html
    d['webservice_res_desc'] = webservice_entity.webservice_res_desc
    d['desc'] = webservice_entity.desc
    return d


def webservice_add(webservice_name, webservice_desc, webservice_html, parent):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    repository_entity = RepositoryEntity.objects.get(id=parent)

    webservice_entity = WebServiceEntity()
    webservice_entity.webservice_name = webservice_name
    webservice_entity.webservice_desc = webservice_desc
    webservice_entity.webservice_html = webservice_html
    webservice_entity.is_active = 1
    webservice_entity.create_date = date
    webservice_entity.update_date = date
    webservice_entity.parent = repository_entity
    webservice_entity.save()
    return "ok"


def webservice_update(webservice_name, webservice_desc, webservice_html, is_active, webservice_id):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    webservice_entity = WebServiceEntity.objects.get(id=webservice_id)

    webservice_entity.webservice_name = webservice_name
    webservice_entity.webservice_desc = webservice_desc
    webservice_entity.webservice_html = webservice_html
    webservice_entity.is_active = is_active
    webservice_entity.update_date = date
    webservice_entity.save()
    return "ok"
