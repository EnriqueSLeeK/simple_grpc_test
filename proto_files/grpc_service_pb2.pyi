from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class doubleData(_message.Message):
    __slots__ = ["double_data"]
    DOUBLE_DATA_FIELD_NUMBER: _ClassVar[int]
    double_data: float
    def __init__(self, double_data: _Optional[float] = ...) -> None: ...

class int32Data(_message.Message):
    __slots__ = ["int32_data"]
    INT32_DATA_FIELD_NUMBER: _ClassVar[int]
    int32_data: int
    def __init__(self, int32_data: _Optional[int] = ...) -> None: ...

class int32MultiSend(_message.Message):
    __slots__ = ["int32_d_0", "int32_d_1", "int32_d_2", "int32_d_3", "int32_d_4", "int32_d_5", "int32_d_6", "int32_d_7"]
    INT32_D_0_FIELD_NUMBER: _ClassVar[int]
    INT32_D_1_FIELD_NUMBER: _ClassVar[int]
    INT32_D_2_FIELD_NUMBER: _ClassVar[int]
    INT32_D_3_FIELD_NUMBER: _ClassVar[int]
    INT32_D_4_FIELD_NUMBER: _ClassVar[int]
    INT32_D_5_FIELD_NUMBER: _ClassVar[int]
    INT32_D_6_FIELD_NUMBER: _ClassVar[int]
    INT32_D_7_FIELD_NUMBER: _ClassVar[int]
    int32_d_0: int
    int32_d_1: int
    int32_d_2: int
    int32_d_3: int
    int32_d_4: int
    int32_d_5: int
    int32_d_6: int
    int32_d_7: int
    def __init__(self, int32_d_0: _Optional[int] = ..., int32_d_1: _Optional[int] = ..., int32_d_2: _Optional[int] = ..., int32_d_3: _Optional[int] = ..., int32_d_4: _Optional[int] = ..., int32_d_5: _Optional[int] = ..., int32_d_6: _Optional[int] = ..., int32_d_7: _Optional[int] = ...) -> None: ...

class stringData(_message.Message):
    __slots__ = ["string_data"]
    STRING_DATA_FIELD_NUMBER: _ClassVar[int]
    string_data: str
    def __init__(self, string_data: _Optional[str] = ...) -> None: ...
