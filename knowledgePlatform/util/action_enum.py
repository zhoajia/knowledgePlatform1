from enum import Enum
from enum import IntEnum, unique


@unique
class ActionEnum(Enum):
    ADD = "添加"
    UPDATE = "更新"
    DELETE = "删除"
    EXECUTE = "执行"
    CANCEL = "取消"
