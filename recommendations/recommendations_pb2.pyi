"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _BookCategory:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _BookCategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BookCategory.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MYSTERY: _BookCategory.ValueType  # 0
    SCIENCE_FICTION: _BookCategory.ValueType  # 1
    SELF_HELP: _BookCategory.ValueType  # 2

class BookCategory(_BookCategory, metaclass=_BookCategoryEnumTypeWrapper): ...

MYSTERY: BookCategory.ValueType  # 0
SCIENCE_FICTION: BookCategory.ValueType  # 1
SELF_HELP: BookCategory.ValueType  # 2
global___BookCategory = BookCategory

@typing.final
class RecommendationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    MAX_RESULTS_FIELD_NUMBER: builtins.int
    user_id: builtins.int
    category: global___BookCategory.ValueType
    max_results: builtins.int
    def __init__(
        self,
        *,
        user_id: builtins.int = ...,
        category: global___BookCategory.ValueType = ...,
        max_results: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["category", b"category", "max_results", b"max_results", "user_id", b"user_id"]) -> None: ...

global___RecommendationRequest = RecommendationRequest

@typing.final
class BookRecommendation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    id: builtins.int
    title: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        title: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "title", b"title"]) -> None: ...

global___BookRecommendation = BookRecommendation

@typing.final
class RecommendationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECOMMENDATIONS_FIELD_NUMBER: builtins.int
    @property
    def recommendations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BookRecommendation]: ...
    def __init__(
        self,
        *,
        recommendations: collections.abc.Iterable[global___BookRecommendation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["recommendations", b"recommendations"]) -> None: ...

global___RecommendationResponse = RecommendationResponse
