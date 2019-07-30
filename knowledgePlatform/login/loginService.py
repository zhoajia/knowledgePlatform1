import hashlib
from knowledgePlatform.User.models import UserEntity


def login(user_name, pass_word):
    passwordMD5 = hashlib.md5(pass_word.encode("utf8")).hexdigest()  # 密码MD5加密
    user = UserEntity.objects.filter(user_name=user_name)
    if len(user) == 0:
        return 0
    if user[0].pass_word == passwordMD5:
        return 1
    else:
        return 0
