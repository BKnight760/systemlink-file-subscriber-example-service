# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated.
"""
Classes for SystemLink Message Bus usage.
"""
from __future__ import absolute_import

# Import python libs
import json
import sys
from datetime import datetime  # pylint: disable=unused-import

# Import local libs
# pylint: disable=import-error
from systemlink.messagebus.broadcast_message import BroadcastMessage  # pylint: disable=unused-import
from systemlink.messagebus.datetime import from_datetime, to_datetime  # pylint: disable=unused-import
from systemlink.messagebus.message_header import (  # pylint: disable=unused-import
    MessageHeader, JSON_MESSAGE_CONTENT_TYPE, BINARY_MESSAGE_CONTENT_TYPE)
from systemlink.messagebus.message_base import MessageBase
from systemlink.messagebus.request_message import RequestMessage  # pylint: disable=unused-import
from systemlink.messagebus.response_message import ResponseMessage  # pylint: disable=unused-import
from systemlink.messagebus.routed_message import RoutedMessage  # pylint: disable=unused-import
# pylint: enable=import-error

if sys.version_info[0] >= 3:
    long = int  # pylint: disable=redefined-builtin,invalid-name


_PASS_THROUGH_TYPES = {
    'bool',
    'bytearray',
    'float',
    'int',
    'long',
    'object',
    'str'
}

_PRIMITIVE_TYPES = {
    'bool': bool,
    'bytearray': bytearray,
    'datetime': datetime,
    'dict': dict,
    'float': float,
    'int': int,
    'list': list,
    'long': long,
    'object': object,
    'str': str
}


def _str_to_type(type_name):
    """
    Convert a type name to a type.

    :param type_name: The name of the type.
    :type type_name: str
    :return: The corresponding type.
    :rtype: type
    """
    type_ = _PRIMITIVE_TYPES.get(type_name)
    if type_ is not None:
        return type_
    return getattr(sys.modules[__name__], type_name)


def _deserialize(value, type_name):  # pylint: disable=too-many-return-statements,too-many-branches
    """
    Deserialize a value from a Python native type.

    :param value: The value to deserialize.
    :type value: object
    :param type_name: The name of the type of `value``.
    :type type_name: str
    :return: The deserialized object.
    :rtype: object
    """
    if value is None:
        return None
    if not type_name:
        return value
    if type_name.endswith(')'):
        sep_index = type_name.find('(')
        sub_type_name = type_name[sep_index+1:-1]
        type_name = type_name[:sep_index]
        if type_name == 'list':
            if sub_type_name in _PASS_THROUGH_TYPES:
                return value
            return [_deserialize(item, sub_type_name) for item in value]
        assert type_name == 'dict'
        sep_index = sub_type_name.find(',')
        key_type_name = sub_type_name[:sep_index]
        value_type_name = sub_type_name[sep_index+1:].strip()
        if key_type_name in _PASS_THROUGH_TYPES and value_type_name in _PASS_THROUGH_TYPES:
            return value
        new_dict = {}
        for dict_key, dict_value in value.items():
            new_dict[_deserialize(dict_key, key_type_name)] = _deserialize(
                dict_value, value_type_name
            )
        return new_dict
    if type_name in _PASS_THROUGH_TYPES:
        return value
    type_ = _str_to_type(type_name)
    if type_ == datetime:
        if not isinstance(value, datetime):
            return to_datetime(value)
        return value
    if hasattr(type_, 'from_dict'):
        return type_.from_dict(value)
    if hasattr(type_, 'from_string'):
        if isinstance(value, int):
            return type_(value)
        return type_.from_string(value)
    if hasattr(type_, 'from_list'):
        if isinstance(value, int):
            return type_(value)
        return type_.from_list(value)
    return value


def _serialize(value):  # pylint: disable=too-many-return-statements
    """
    Serialize a value to a Python native type.

    :param value: The value to serialize.
    :type value: object
    :return: The serialized object.
    :rtype: object
    """
    if value is None:
        return None
    if isinstance(value, list):
        return [_serialize(item) for item in value]
    if isinstance(value, dict):
        new_dict = {}
        for dict_key, dict_value in value.items():
            new_dict[_serialize(dict_key)] = _serialize(dict_value)
        return new_dict
    if isinstance(value, datetime):
        return from_datetime(value)
    if hasattr(value, 'to_dict'):
        return value.to_dict()
    if hasattr(value, 'to_string'):
        return value.to_string()
    if hasattr(value, 'to_list'):
        return value.to_list()
    return value


# pylint: disable=line-too-long,too-many-lines,too-many-instance-attributes,too-many-arguments,too-many-locals,useless-object-inheritance


#
# FileIngestion service
#


class QueryOperator(object):  # pylint: disable=too-few-public-methods
    """
    QueryOperator normal enum.
    """
    CONTAINS = 0
    NOT_CONTAINS = 1
    EQUAL = 2
    NOT_EQUAL = 3
    LESS_THAN = 4
    GREATER_THAN = 5
    LESS_THAN_OR_EQUAL = 6
    GREATER_THAN_OR_EQUAL = 7
    _INT_TO_STRING = {
        0: 'CONTAINS',
        1: 'NOT_CONTAINS',
        2: 'EQUAL',
        3: 'NOT_EQUAL',
        4: 'LESS_THAN',
        5: 'GREATER_THAN',
        6: 'LESS_THAN_OR_EQUAL',
        7: 'GREATER_THAN_OR_EQUAL'
    }
    _STRING_TO_INT = {
        'CONTAINS': 0,
        'NOT_CONTAINS': 1,
        'EQUAL': 2,
        'NOT_EQUAL': 3,
        'LESS_THAN': 4,
        'GREATER_THAN': 5,
        'LESS_THAN_OR_EQUAL': 6,
        'GREATER_THAN_OR_EQUAL': 7
    }

    def __init__(self, value):
        """
        :param value: The integer value of the enum.
        :type value: int
        """
        self._value = value

    @property
    def value(self):
        """
        Get integer value of the enum.

        :return: The integer value of the enum.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Set integer value of the enum.

        :param value: The integer value of the enum.
        :type value: int
        """
        self._value = value

    @classmethod
    def from_string(cls, value_string):
        """
        Create a new instance of :class:`QueryOperator` using a string.

        :param value_string: The string value of the enum.
        :type value_string: str
        :return: A new instance of :class:`QueryOperator`.
        :rtype: QueryOperator
        """
        if value_string is None:
            return None
        value = cls._STRING_TO_INT[value_string]
        return cls(value)

    def to_string(self):
        """
        Returns a string representing the enum.

        :return: A string representing the enum.
        :rtype: str
        """
        return self._INT_TO_STRING[self._value]

    def __str__(self):
        """
        Returns a string representing the enum.

        :return: A string representing the enum.
        :rtype: str
        """
        return self.to_string()


class FileIngestionMetadata(object):
    """
    FileIngestionMetadata custom data type.
    """
    def __init__(self,
                 id_=None,
                 size_=None,
                 created_=None,
                 service_group_=None,
                 workspace_=None,
                 properties_=None,
                 size64_=None,
                 meta_data_revision_=None):
        """
        :param id_: id
        :type id_: str
        :param size_: size
        :type size_: int
        :param created_: created
        :type created_: datetime
        :param service_group_: service_group
        :type service_group_: str
        :param workspace_: workspace
        :type workspace_: str
        :param properties_: properties
        :type properties_: dict(str,str)
        :param size64_: size64
        :type size64_: long
        :param meta_data_revision_: meta_data_revision
        :type meta_data_revision_: int
        """
        self.id = id_  # pylint: disable=invalid-name
        self.size = size_
        self.created = created_
        self.service_group = service_group_
        self.workspace = workspace_
        self.properties = properties_
        self.size64 = size64_
        self.meta_data_revision = meta_data_revision_

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileIngestionMetadata` using a dictionary.

        :param body_dict: A dictionary representing the body.
        :type body_dict: dict
        :return: A new instance of :class:`FileIngestionMetadata`.
        :rtype: FileIngestionMetadata
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        size_ = _deserialize(body_dict.get('size'), 'int')
        created_ = _deserialize(body_dict.get('created'), 'datetime')
        service_group_ = _deserialize(body_dict.get('serviceGroup'), 'str')
        workspace_ = _deserialize(body_dict.get('workspace'), 'str')
        properties_ = _deserialize(body_dict.get('properties'), 'dict(str,str)')
        size64_ = _deserialize(body_dict.get('size64'), 'long')
        meta_data_revision_ = _deserialize(body_dict.get('metaDataRevision'), 'int')
        return cls(
            id_=id_,
            size_=size_,
            created_=created_,
            service_group_=service_group_,
            workspace_=workspace_,
            properties_=properties_,
            size64_=size64_,
            meta_data_revision_=meta_data_revision_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileIngestionMetadata` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileIngestionMetadata`.
        :rtype: FileIngestionMetadata
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileIngestionMetadata` using a body
        of type :class:`bytes` or :class:`bytearray`.

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileIngestionMetadata`.
        :rtype: FileIngestionMetadata
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        size_ = _serialize(self.size)
        created_ = _serialize(self.created)
        service_group_ = _serialize(self.service_group)
        workspace_ = _serialize(self.workspace)
        properties_ = _serialize(self.properties)
        size64_ = _serialize(self.size64)
        meta_data_revision_ = _serialize(self.meta_data_revision)
        return {
            'id': id_,
            'size': size_,
            'created': created_,
            'serviceGroup': service_group_,
            'workspace': workspace_,
            'properties': properties_,
            'size64': size64_,
            'metaDataRevision': meta_data_revision_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')


class StringQueryEntry(object):
    """
    StringQueryEntry custom data type.
    """
    def __init__(self,
                 key_=None,
                 value_=None,
                 operation_=None):
        """
        :param key_: key
        :type key_: str
        :param value_: value
        :type value_: str
        :param operation_: operation
        :type operation_: QueryOperator
        """
        self.key = key_
        self.value = value_
        self.operation = operation_

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`StringQueryEntry` using a dictionary.

        :param body_dict: A dictionary representing the body.
        :type body_dict: dict
        :return: A new instance of :class:`StringQueryEntry`.
        :rtype: StringQueryEntry
        """
        key_ = _deserialize(body_dict.get('key'), 'str')
        value_ = _deserialize(body_dict.get('value'), 'str')
        operation_ = _deserialize(body_dict.get('operation'), 'QueryOperator')
        return cls(
            key_=key_,
            value_=value_,
            operation_=operation_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`StringQueryEntry` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`StringQueryEntry`.
        :rtype: StringQueryEntry
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`StringQueryEntry` using a body
        of type :class:`bytes` or :class:`bytearray`.

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`StringQueryEntry`.
        :rtype: StringQueryEntry
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        key_ = _serialize(self.key)
        value_ = _serialize(self.value)
        operation_ = _serialize(self.operation)
        return {
            'key': key_,
            'value': value_,
            'operation': operation_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')


class IntQueryEntry(object):
    """
    IntQueryEntry custom data type.
    """
    def __init__(self,
                 key_=None,
                 value_=None,
                 operation_=None,
                 value64_=None):
        """
        :param key_: key
        :type key_: str
        :param value_: value
        :type value_: int
        :param operation_: operation
        :type operation_: QueryOperator
        :param value64_: value64
        :type value64_: long
        """
        self.key = key_
        self.value = value_
        self.operation = operation_
        self.value64 = value64_

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`IntQueryEntry` using a dictionary.

        :param body_dict: A dictionary representing the body.
        :type body_dict: dict
        :return: A new instance of :class:`IntQueryEntry`.
        :rtype: IntQueryEntry
        """
        key_ = _deserialize(body_dict.get('key'), 'str')
        value_ = _deserialize(body_dict.get('value'), 'int')
        operation_ = _deserialize(body_dict.get('operation'), 'QueryOperator')
        value64_ = _deserialize(body_dict.get('value64'), 'long')
        return cls(
            key_=key_,
            value_=value_,
            operation_=operation_,
            value64_=value64_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`IntQueryEntry` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`IntQueryEntry`.
        :rtype: IntQueryEntry
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`IntQueryEntry` using a body
        of type :class:`bytes` or :class:`bytearray`.

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`IntQueryEntry`.
        :rtype: IntQueryEntry
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        key_ = _serialize(self.key)
        value_ = _serialize(self.value)
        operation_ = _serialize(self.operation)
        value64_ = _serialize(self.value64)
        return {
            'key': key_,
            'value': value_,
            'operation': operation_,
            'value64': value64_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')


class DateQueryEntry(object):
    """
    DateQueryEntry custom data type.
    """
    def __init__(self,
                 key_=None,
                 value_=None,
                 operation_=None):
        """
        :param key_: key
        :type key_: str
        :param value_: value
        :type value_: datetime
        :param operation_: operation
        :type operation_: QueryOperator
        """
        self.key = key_
        self.value = value_
        self.operation = operation_

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`DateQueryEntry` using a dictionary.

        :param body_dict: A dictionary representing the body.
        :type body_dict: dict
        :return: A new instance of :class:`DateQueryEntry`.
        :rtype: DateQueryEntry
        """
        key_ = _deserialize(body_dict.get('key'), 'str')
        value_ = _deserialize(body_dict.get('value'), 'datetime')
        operation_ = _deserialize(body_dict.get('operation'), 'QueryOperator')
        return cls(
            key_=key_,
            value_=value_,
            operation_=operation_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`DateQueryEntry` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`DateQueryEntry`.
        :rtype: DateQueryEntry
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`DateQueryEntry` using a body
        of type :class:`bytes` or :class:`bytearray`.

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`DateQueryEntry`.
        :rtype: DateQueryEntry
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        key_ = _serialize(self.key)
        value_ = _serialize(self.value)
        operation_ = _serialize(self.operation)
        return {
            'key': key_,
            'value': value_,
            'operation': operation_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')


class Entity(object):
    """
    Entity custom data type.
    """
    def __init__(self,
                 name_=None,
                 id_=None):
        """
        :param name_: name
        :type name_: str
        :param id_: id
        :type id_: str
        """
        self.name = name_
        self.id = id_  # pylint: disable=invalid-name

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`Entity` using a dictionary.

        :param body_dict: A dictionary representing the body.
        :type body_dict: dict
        :return: A new instance of :class:`Entity`.
        :rtype: Entity
        """
        name_ = _deserialize(body_dict.get('name'), 'str')
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        return cls(
            name_=name_,
            id_=id_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`Entity` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`Entity`.
        :rtype: Entity
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`Entity` using a body
        of type :class:`bytes` or :class:`bytearray`.

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`Entity`.
        :rtype: Entity
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        name_ = _serialize(self.name)
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        return {
            'name': name_,
            'id': id_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')


class FileSendRequest(RequestMessage):
    """
    FileSendRequest JSON request message.
    """
    MESSAGE_NAME = 'FileSendRequest'

    def __init__(self,
                 properties_=None,
                 notify_complete_=None,
                 id_=None):
        """
        :param properties_: properties
        :type properties_: dict(str,str)
        :param notify_complete_: notify_complete
        :type notify_complete_: bool
        :param id_: id
        :type id_: str
        """
        self.properties = properties_
        self.notify_complete = notify_complete_
        self.id = id_  # pylint: disable=invalid-name
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileSendRequest, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileSendRequest` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileSendRequest`.
        :rtype: FileSendRequest
        """
        properties_ = _deserialize(body_dict.get('properties'), 'dict(str,str)')
        notify_complete_ = _deserialize(body_dict.get('notifyComplete'), 'bool')
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        return cls(
            properties_=properties_,
            notify_complete_=notify_complete_,
            id_=id_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileSendRequest` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileSendRequest`.
        :rtype: FileSendRequest
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileSendRequest` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileSendRequest`.
        :rtype: FileSendRequest
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileSendRequest` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileSendRequest`.
        :rtype: FileSendRequest
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        properties_ = _serialize(self.properties)
        notify_complete_ = _serialize(self.notify_complete)
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        return {
            'properties': properties_,
            'notifyComplete': notify_complete_,
            'id': id_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileSendResponse(ResponseMessage):
    """
    FileSendResponse JSON response message.
    """
    MESSAGE_NAME = 'FileSendResponse'

    def __init__(self,
                 request_message,
                 id_=None):
        """
        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param id_: id
        :type id_: str
        """
        self.id = id_  # pylint: disable=invalid-name
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        # If request_message is None, routing key needs to be set outside this constructor.
        if request_message:
            header.correlation_id = request_message.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_message.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        super(FileSendResponse, self).__init__(header, None)

    @classmethod
    def from_dict(cls, request_message, body_dict):
        """
        Create a new instance of :class:`FileSendResponse` using a dictionary.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileSendResponse`.
        :rtype: FileSendResponse
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        return cls(
            request_message,
            id_=id_
        )

    @classmethod
    def from_json(cls, request_message, body_json):
        """
        Create a new instance of :class:`FileSendResponse` using a JSON string.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileSendResponse`.
        :rtype: FileSendResponse
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(request_message, body_dict)

    @classmethod
    def from_body_bytes(cls, request_message, body_bytes):
        """
        Create a new instance of :class:`FileSendResponse` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileSendResponse`.
        :rtype: FileSendResponse
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(request_message, body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileSendResponse` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileSendResponse`.
        :rtype: FileSendResponse
        """
        instance = cls.from_body_bytes(message, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        routing_key = MessageHeader.generate_routing_key(message.reply_to, cls.MESSAGE_NAME)
        instance.routing_key = routing_key
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        return {
            'id': id_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_header.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileUpdateMetadataPropertiesRequest(RequestMessage):
    """
    FileUpdateMetadataPropertiesRequest JSON request message.
    """
    MESSAGE_NAME = 'FileUpdateMetadataPropertiesRequest'

    def __init__(self,
                 id_=None,
                 replace_existing_=None,
                 properties_=None,
                 expected_revision_=None,
                 workspace_=None):
        """
        :param id_: id
        :type id_: str
        :param replace_existing_: replace_existing
        :type replace_existing_: bool
        :param properties_: properties
        :type properties_: dict(str,str)
        :param expected_revision_: expected_revision
        :type expected_revision_: int
        :param workspace_: workspace
        :type workspace_: str
        """
        self.id = id_  # pylint: disable=invalid-name
        self.replace_existing = replace_existing_
        self.properties = properties_
        self.expected_revision = expected_revision_
        self.workspace = workspace_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileUpdateMetadataPropertiesRequest, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileUpdateMetadataPropertiesRequest` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileUpdateMetadataPropertiesRequest`.
        :rtype: FileUpdateMetadataPropertiesRequest
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        replace_existing_ = _deserialize(body_dict.get('replaceExisting'), 'bool')
        properties_ = _deserialize(body_dict.get('properties'), 'dict(str,str)')
        expected_revision_ = _deserialize(body_dict.get('expectedRevision'), 'int')
        workspace_ = _deserialize(body_dict.get('workspace'), 'str')
        return cls(
            id_=id_,
            replace_existing_=replace_existing_,
            properties_=properties_,
            expected_revision_=expected_revision_,
            workspace_=workspace_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileUpdateMetadataPropertiesRequest` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileUpdateMetadataPropertiesRequest`.
        :rtype: FileUpdateMetadataPropertiesRequest
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileUpdateMetadataPropertiesRequest` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileUpdateMetadataPropertiesRequest`.
        :rtype: FileUpdateMetadataPropertiesRequest
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileUpdateMetadataPropertiesRequest` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileUpdateMetadataPropertiesRequest`.
        :rtype: FileUpdateMetadataPropertiesRequest
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        replace_existing_ = _serialize(self.replace_existing)
        properties_ = _serialize(self.properties)
        expected_revision_ = _serialize(self.expected_revision)
        workspace_ = _serialize(self.workspace)
        return {
            'id': id_,
            'replaceExisting': replace_existing_,
            'properties': properties_,
            'expectedRevision': expected_revision_,
            'workspace': workspace_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileUpdateMetadataPropertiesResponse(ResponseMessage):
    """
    FileUpdateMetadataPropertiesResponse JSON response message.
    """
    MESSAGE_NAME = 'FileUpdateMetadataPropertiesResponse'

    def __init__(self,
                 request_message,
                 metadata_=None):
        """
        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param metadata_: metadata
        :type metadata_: FileIngestionMetadata
        """
        self.metadata = metadata_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        # If request_message is None, routing key needs to be set outside this constructor.
        if request_message:
            header.correlation_id = request_message.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_message.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        super(FileUpdateMetadataPropertiesResponse, self).__init__(header, None)

    @classmethod
    def from_dict(cls, request_message, body_dict):
        """
        Create a new instance of :class:`FileUpdateMetadataPropertiesResponse` using a dictionary.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileUpdateMetadataPropertiesResponse`.
        :rtype: FileUpdateMetadataPropertiesResponse
        """
        metadata_ = _deserialize(body_dict.get('metadata'), 'FileIngestionMetadata')
        return cls(
            request_message,
            metadata_=metadata_
        )

    @classmethod
    def from_json(cls, request_message, body_json):
        """
        Create a new instance of :class:`FileUpdateMetadataPropertiesResponse` using a JSON string.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileUpdateMetadataPropertiesResponse`.
        :rtype: FileUpdateMetadataPropertiesResponse
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(request_message, body_dict)

    @classmethod
    def from_body_bytes(cls, request_message, body_bytes):
        """
        Create a new instance of :class:`FileUpdateMetadataPropertiesResponse` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileUpdateMetadataPropertiesResponse`.
        :rtype: FileUpdateMetadataPropertiesResponse
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(request_message, body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileUpdateMetadataPropertiesResponse` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileUpdateMetadataPropertiesResponse`.
        :rtype: FileUpdateMetadataPropertiesResponse
        """
        instance = cls.from_body_bytes(message, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        routing_key = MessageHeader.generate_routing_key(message.reply_to, cls.MESSAGE_NAME)
        instance.routing_key = routing_key
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        metadata_ = _serialize(self.metadata)
        return {
            'metadata': metadata_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_header.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileReceiveRoutedMessage(RoutedMessage):
    """
    FileReceiveRoutedMessage JSON routed message.
    """
    MESSAGE_NAME = 'FileReceiveRoutedMessage'

    def __init__(self,
                 id_=None,
                 max_packet_size_=None):
        """
        :param id_: id
        :type id_: str
        :param max_packet_size_: max_packet_size
        :type max_packet_size_: int
        """
        self.id = id_  # pylint: disable=invalid-name
        self.max_packet_size = max_packet_size_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileReceiveRoutedMessage, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileReceiveRoutedMessage` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileReceiveRoutedMessage`.
        :rtype: FileReceiveRoutedMessage
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        max_packet_size_ = _deserialize(body_dict.get('maxPacketSize'), 'int')
        return cls(
            id_=id_,
            max_packet_size_=max_packet_size_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileReceiveRoutedMessage` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileReceiveRoutedMessage`.
        :rtype: FileReceiveRoutedMessage
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileReceiveRoutedMessage` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileReceiveRoutedMessage`.
        :rtype: FileReceiveRoutedMessage
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileReceiveRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileReceiveRoutedMessage`.
        :rtype: FileReceiveRoutedMessage
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        max_packet_size_ = _serialize(self.max_packet_size)
        return {
            'id': id_,
            'maxPacketSize': max_packet_size_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileReceiveRequest(RequestMessage):
    """
    FileReceiveRequest JSON request message.
    """
    MESSAGE_NAME = 'FileReceiveRequest'

    def __init__(self,
                 id_=None,
                 max_packet_size_=None):
        """
        :param id_: id
        :type id_: str
        :param max_packet_size_: max_packet_size
        :type max_packet_size_: int
        """
        self.id = id_  # pylint: disable=invalid-name
        self.max_packet_size = max_packet_size_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileReceiveRequest, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileReceiveRequest` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileReceiveRequest`.
        :rtype: FileReceiveRequest
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        max_packet_size_ = _deserialize(body_dict.get('maxPacketSize'), 'int')
        return cls(
            id_=id_,
            max_packet_size_=max_packet_size_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileReceiveRequest` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileReceiveRequest`.
        :rtype: FileReceiveRequest
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileReceiveRequest` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileReceiveRequest`.
        :rtype: FileReceiveRequest
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileReceiveRequest` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileReceiveRequest`.
        :rtype: FileReceiveRequest
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        max_packet_size_ = _serialize(self.max_packet_size)
        return {
            'id': id_,
            'maxPacketSize': max_packet_size_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileReceiveResponse(ResponseMessage):
    """
    FileReceiveResponse JSON response message.
    """
    MESSAGE_NAME = 'FileReceiveResponse'

    def __init__(self,
                 request_message,
                 receive_id_=None,
                 metadata_=None):
        """
        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param receive_id_: receive_id
        :type receive_id_: str
        :param metadata_: metadata
        :type metadata_: FileIngestionMetadata
        """
        self.receive_id = receive_id_
        self.metadata = metadata_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        # If request_message is None, routing key needs to be set outside this constructor.
        if request_message:
            header.correlation_id = request_message.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_message.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        super(FileReceiveResponse, self).__init__(header, None)

    @classmethod
    def from_dict(cls, request_message, body_dict):
        """
        Create a new instance of :class:`FileReceiveResponse` using a dictionary.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileReceiveResponse`.
        :rtype: FileReceiveResponse
        """
        receive_id_ = _deserialize(body_dict.get('receiveId'), 'str')
        metadata_ = _deserialize(body_dict.get('metadata'), 'FileIngestionMetadata')
        return cls(
            request_message,
            receive_id_=receive_id_,
            metadata_=metadata_
        )

    @classmethod
    def from_json(cls, request_message, body_json):
        """
        Create a new instance of :class:`FileReceiveResponse` using a JSON string.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileReceiveResponse`.
        :rtype: FileReceiveResponse
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(request_message, body_dict)

    @classmethod
    def from_body_bytes(cls, request_message, body_bytes):
        """
        Create a new instance of :class:`FileReceiveResponse` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileReceiveResponse`.
        :rtype: FileReceiveResponse
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(request_message, body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileReceiveResponse` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileReceiveResponse`.
        :rtype: FileReceiveResponse
        """
        instance = cls.from_body_bytes(message, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        routing_key = MessageHeader.generate_routing_key(message.reply_to, cls.MESSAGE_NAME)
        instance.routing_key = routing_key
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        receive_id_ = _serialize(self.receive_id)
        metadata_ = _serialize(self.metadata)
        return {
            'receiveId': receive_id_,
            'metadata': metadata_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_header.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FilePacketRoutedMessage(RoutedMessage):
    """
    FilePacketRoutedMessage binary routed message.
    """
    MESSAGE_NAME = 'FilePacketRoutedMessage'

    def __init__(self,
                 routing_source,
                 id_=None,
                 packet_number_=None,
                 is_last_packet_=None,
                 body=None):
        """
        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param id_: id
        :type id_: str
        :param packet_number_: packet_number
        :type packet_number_: int
        :param is_last_packet_: is_last_packet
        :type is_last_packet_: bool
        :param body: The binary message body
        :type body: bytes or bytearray
        """
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = BINARY_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
        header.routing_key = routing_key
        header.set_property('Id', id_)
        header.set_property('PacketNumber', packet_number_)
        header.set_property('IsLastPacket', is_last_packet_)
        super(FilePacketRoutedMessage, self).__init__(header, body)

    @classmethod
    def from_message(cls, routing_source, message):
        """
        Create a new instance of :class`FilePacketRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FilePacketRoutedMessage`.
        :rtype: FilePacketRoutedMessage
        """
        source_header = message.header
        id_ = source_header.get_property('Id')
        packet_number_ = source_header.get_int_property('PacketNumber')
        is_last_packet_ = source_header.get_bool_property('IsLastPacket')
        source_body = message.body_bytes
        instance = cls(
            routing_source,
            id_,
            packet_number_,
            is_last_packet_,
            source_body
        )
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_message(self, routing_source, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.body_bytes
        return MessageBase(header, body_bytes)


class FileReceivePacketRoutedMessage(RoutedMessage):
    """
    FileReceivePacketRoutedMessage binary routed message.
    """
    MESSAGE_NAME = 'FileReceivePacketRoutedMessage'

    def __init__(self,
                 routing_source,
                 receive_id_=None,
                 id_=None,
                 packet_number_=None,
                 is_last_packet_=None,
                 send_acknowledgment_=None,
                 body=None):
        """
        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param receive_id_: receive_id
        :type receive_id_: str
        :param id_: id
        :type id_: str
        :param packet_number_: packet_number
        :type packet_number_: int
        :param is_last_packet_: is_last_packet
        :type is_last_packet_: bool
        :param send_acknowledgment_: send_acknowledgment
        :type send_acknowledgment_: bool
        :param body: The binary message body
        :type body: bytes or bytearray
        """
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = BINARY_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
        header.routing_key = routing_key
        header.set_property('ReceiveId', receive_id_)
        header.set_property('Id', id_)
        header.set_property('PacketNumber', packet_number_)
        header.set_property('IsLastPacket', is_last_packet_)
        header.set_property('SendAcknowledgment', send_acknowledgment_)
        super(FileReceivePacketRoutedMessage, self).__init__(header, body)

    @classmethod
    def from_message(cls, routing_source, message):
        """
        Create a new instance of :class`FileReceivePacketRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileReceivePacketRoutedMessage`.
        :rtype: FileReceivePacketRoutedMessage
        """
        source_header = message.header
        receive_id_ = source_header.get_property('ReceiveId')
        id_ = source_header.get_property('Id')
        packet_number_ = source_header.get_int_property('PacketNumber')
        is_last_packet_ = source_header.get_bool_property('IsLastPacket')
        send_acknowledgment_ = source_header.get_bool_property('SendAcknowledgment')
        source_body = message.body_bytes
        instance = cls(
            routing_source,
            receive_id_,
            id_,
            packet_number_,
            is_last_packet_,
            send_acknowledgment_,
            source_body
        )
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_message(self, routing_source, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.body_bytes
        return MessageBase(header, body_bytes)


class FileReceivePacketAcknowledgmentRoutedMessage(RoutedMessage):
    """
    FileReceivePacketAcknowledgmentRoutedMessage JSON routed message.
    """
    MESSAGE_NAME = 'FileReceivePacketAcknowledgmentRoutedMessage'

    def __init__(self,
                 routing_source,
                 receive_id_=None,
                 stop_sending_packets_=None):
        """
        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param receive_id_: receive_id
        :type receive_id_: str
        :param stop_sending_packets_: stop_sending_packets
        :type stop_sending_packets_: bool
        """
        self.receive_id = receive_id_
        self.stop_sending_packets = stop_sending_packets_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileReceivePacketAcknowledgmentRoutedMessage, self).__init__(header, None)

    @classmethod
    def from_dict(cls, routing_source, body_dict):
        """
        Create a new instance of :class:`FileReceivePacketAcknowledgmentRoutedMessage` using a dictionary.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileReceivePacketAcknowledgmentRoutedMessage`.
        :rtype: FileReceivePacketAcknowledgmentRoutedMessage
        """
        receive_id_ = _deserialize(body_dict.get('receiveId'), 'str')
        stop_sending_packets_ = _deserialize(body_dict.get('stopSendingPackets'), 'bool')
        return cls(
            routing_source,
            receive_id_=receive_id_,
            stop_sending_packets_=stop_sending_packets_
        )

    @classmethod
    def from_json(cls, routing_source, body_json):
        """
        Create a new instance of :class:`FileReceivePacketAcknowledgmentRoutedMessage` using a JSON string.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileReceivePacketAcknowledgmentRoutedMessage`.
        :rtype: FileReceivePacketAcknowledgmentRoutedMessage
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(routing_source, body_dict)

    @classmethod
    def from_body_bytes(cls, routing_source, body_bytes):
        """
        Create a new instance of :class:`FileReceivePacketAcknowledgmentRoutedMessage` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileReceivePacketAcknowledgmentRoutedMessage`.
        :rtype: FileReceivePacketAcknowledgmentRoutedMessage
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(routing_source, body_json)

    @classmethod
    def from_message(cls, routing_source, message):
        """
        Create a new instance of :class`FileReceivePacketAcknowledgmentRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileReceivePacketAcknowledgmentRoutedMessage`.
        :rtype: FileReceivePacketAcknowledgmentRoutedMessage
        """
        instance = cls.from_body_bytes(routing_source, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        receive_id_ = _serialize(self.receive_id)
        stop_sending_packets_ = _serialize(self.stop_sending_packets)
        return {
            'receiveId': receive_id_,
            'stopSendingPackets': stop_sending_packets_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, routing_source, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileCompleteRoutedMessage(RoutedMessage):
    """
    FileCompleteRoutedMessage JSON routed message.
    """
    MESSAGE_NAME = 'FileCompleteRoutedMessage'

    def __init__(self,
                 routing_source,
                 id_=None,
                 metadata_=None,
                 packet_number_=None):
        """
        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param id_: id
        :type id_: str
        :param metadata_: metadata
        :type metadata_: FileIngestionMetadata
        :param packet_number_: packet_number
        :type packet_number_: int
        """
        self.id = id_  # pylint: disable=invalid-name
        self.metadata = metadata_
        self.packet_number = packet_number_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileCompleteRoutedMessage, self).__init__(header, None)

    @classmethod
    def from_dict(cls, routing_source, body_dict):
        """
        Create a new instance of :class:`FileCompleteRoutedMessage` using a dictionary.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileCompleteRoutedMessage`.
        :rtype: FileCompleteRoutedMessage
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        metadata_ = _deserialize(body_dict.get('metadata'), 'FileIngestionMetadata')
        packet_number_ = _deserialize(body_dict.get('packetNumber'), 'int')
        return cls(
            routing_source,
            id_=id_,
            metadata_=metadata_,
            packet_number_=packet_number_
        )

    @classmethod
    def from_json(cls, routing_source, body_json):
        """
        Create a new instance of :class:`FileCompleteRoutedMessage` using a JSON string.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileCompleteRoutedMessage`.
        :rtype: FileCompleteRoutedMessage
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(routing_source, body_dict)

    @classmethod
    def from_body_bytes(cls, routing_source, body_bytes):
        """
        Create a new instance of :class:`FileCompleteRoutedMessage` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileCompleteRoutedMessage`.
        :rtype: FileCompleteRoutedMessage
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(routing_source, body_json)

    @classmethod
    def from_message(cls, routing_source, message):
        """
        Create a new instance of :class`FileCompleteRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileCompleteRoutedMessage`.
        :rtype: FileCompleteRoutedMessage
        """
        instance = cls.from_body_bytes(routing_source, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        metadata_ = _serialize(self.metadata)
        packet_number_ = _serialize(self.packet_number)
        return {
            'id': id_,
            'metadata': metadata_,
            'packetNumber': packet_number_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, routing_source, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileReceiveCompleteRoutedMessage(RoutedMessage):
    """
    FileReceiveCompleteRoutedMessage JSON routed message.
    """
    MESSAGE_NAME = 'FileReceiveCompleteRoutedMessage'

    def __init__(self,
                 routing_source,
                 receive_id_=None,
                 id_=None,
                 packet_number_=None):
        """
        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param receive_id_: receive_id
        :type receive_id_: str
        :param id_: id
        :type id_: str
        :param packet_number_: packet_number
        :type packet_number_: int
        """
        self.receive_id = receive_id_
        self.id = id_  # pylint: disable=invalid-name
        self.packet_number = packet_number_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileReceiveCompleteRoutedMessage, self).__init__(header, None)

    @classmethod
    def from_dict(cls, routing_source, body_dict):
        """
        Create a new instance of :class:`FileReceiveCompleteRoutedMessage` using a dictionary.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileReceiveCompleteRoutedMessage`.
        :rtype: FileReceiveCompleteRoutedMessage
        """
        receive_id_ = _deserialize(body_dict.get('receiveId'), 'str')
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        packet_number_ = _deserialize(body_dict.get('packetNumber'), 'int')
        return cls(
            routing_source,
            receive_id_=receive_id_,
            id_=id_,
            packet_number_=packet_number_
        )

    @classmethod
    def from_json(cls, routing_source, body_json):
        """
        Create a new instance of :class:`FileReceiveCompleteRoutedMessage` using a JSON string.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileReceiveCompleteRoutedMessage`.
        :rtype: FileReceiveCompleteRoutedMessage
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(routing_source, body_dict)

    @classmethod
    def from_body_bytes(cls, routing_source, body_bytes):
        """
        Create a new instance of :class:`FileReceiveCompleteRoutedMessage` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileReceiveCompleteRoutedMessage`.
        :rtype: FileReceiveCompleteRoutedMessage
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(routing_source, body_json)

    @classmethod
    def from_message(cls, routing_source, message):
        """
        Create a new instance of :class`FileReceiveCompleteRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileReceiveCompleteRoutedMessage`.
        :rtype: FileReceiveCompleteRoutedMessage
        """
        instance = cls.from_body_bytes(routing_source, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        receive_id_ = _serialize(self.receive_id)
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        packet_number_ = _serialize(self.packet_number)
        return {
            'receiveId': receive_id_,
            'id': id_,
            'packetNumber': packet_number_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, routing_source, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileCancelRoutedMessage(RoutedMessage):
    """
    FileCancelRoutedMessage JSON routed message.
    """
    MESSAGE_NAME = 'FileCancelRoutedMessage'

    def __init__(self,
                 routing_source,
                 id_=None):
        """
        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param id_: id
        :type id_: str
        """
        self.id = id_  # pylint: disable=invalid-name
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileCancelRoutedMessage, self).__init__(header, None)

    @classmethod
    def from_dict(cls, routing_source, body_dict):
        """
        Create a new instance of :class:`FileCancelRoutedMessage` using a dictionary.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileCancelRoutedMessage`.
        :rtype: FileCancelRoutedMessage
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        return cls(
            routing_source,
            id_=id_
        )

    @classmethod
    def from_json(cls, routing_source, body_json):
        """
        Create a new instance of :class:`FileCancelRoutedMessage` using a JSON string.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileCancelRoutedMessage`.
        :rtype: FileCancelRoutedMessage
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(routing_source, body_dict)

    @classmethod
    def from_body_bytes(cls, routing_source, body_bytes):
        """
        Create a new instance of :class:`FileCancelRoutedMessage` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileCancelRoutedMessage`.
        :rtype: FileCancelRoutedMessage
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(routing_source, body_json)

    @classmethod
    def from_message(cls, routing_source, message):
        """
        Create a new instance of :class`FileCancelRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileCancelRoutedMessage`.
        :rtype: FileCancelRoutedMessage
        """
        instance = cls.from_body_bytes(routing_source, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        return {
            'id': id_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, routing_source, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param routing_source: The message to use its reply-to field as a routing parameter.
        :type routing_source: systemlink.messagebus.message_base.MessageBase
        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(routing_source.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileListAvailableFilesRequest(RequestMessage):
    """
    FileListAvailableFilesRequest JSON request message.
    """
    MESSAGE_NAME = 'FileListAvailableFilesRequest'

    def __init__(self,
                 ids_=None,
                 order_by_=None,
                 order_by_descending_=None,
                 skip_=None,
                 take_=None):
        """
        :param ids_: ids
        :type ids_: list(str)
        :param order_by_: order_by
        :type order_by_: str
        :param order_by_descending_: order_by_descending
        :type order_by_descending_: bool
        :param skip_: skip
        :type skip_: int
        :param take_: take
        :type take_: int
        """
        self.ids = ids_
        self.order_by = order_by_
        self.order_by_descending = order_by_descending_
        self.skip = skip_
        self.take = take_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileListAvailableFilesRequest, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileListAvailableFilesRequest` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileListAvailableFilesRequest`.
        :rtype: FileListAvailableFilesRequest
        """
        ids_ = _deserialize(body_dict.get('ids'), 'list(str)')
        order_by_ = _deserialize(body_dict.get('orderBy'), 'str')
        order_by_descending_ = _deserialize(body_dict.get('orderByDescending'), 'bool')
        skip_ = _deserialize(body_dict.get('skip'), 'int')
        take_ = _deserialize(body_dict.get('take'), 'int')
        return cls(
            ids_=ids_,
            order_by_=order_by_,
            order_by_descending_=order_by_descending_,
            skip_=skip_,
            take_=take_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileListAvailableFilesRequest` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileListAvailableFilesRequest`.
        :rtype: FileListAvailableFilesRequest
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileListAvailableFilesRequest` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileListAvailableFilesRequest`.
        :rtype: FileListAvailableFilesRequest
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileListAvailableFilesRequest` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileListAvailableFilesRequest`.
        :rtype: FileListAvailableFilesRequest
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        ids_ = _serialize(self.ids)
        order_by_ = _serialize(self.order_by)
        order_by_descending_ = _serialize(self.order_by_descending)
        skip_ = _serialize(self.skip)
        take_ = _serialize(self.take)
        return {
            'ids': ids_,
            'orderBy': order_by_,
            'orderByDescending': order_by_descending_,
            'skip': skip_,
            'take': take_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileListAvailableFilesResponse(ResponseMessage):
    """
    FileListAvailableFilesResponse JSON response message.
    """
    MESSAGE_NAME = 'FileListAvailableFilesResponse'

    def __init__(self,
                 request_message,
                 available_files_=None,
                 total_count_=None):
        """
        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param available_files_: available_files
        :type available_files_: list(FileIngestionMetadata)
        :param total_count_: total_count
        :type total_count_: int
        """
        self.available_files = available_files_
        self.total_count = total_count_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        # If request_message is None, routing key needs to be set outside this constructor.
        if request_message:
            header.correlation_id = request_message.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_message.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        super(FileListAvailableFilesResponse, self).__init__(header, None)

    @classmethod
    def from_dict(cls, request_message, body_dict):
        """
        Create a new instance of :class:`FileListAvailableFilesResponse` using a dictionary.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileListAvailableFilesResponse`.
        :rtype: FileListAvailableFilesResponse
        """
        available_files_ = _deserialize(body_dict.get('availableFiles'), 'list(FileIngestionMetadata)')
        total_count_ = _deserialize(body_dict.get('totalCount'), 'int')
        return cls(
            request_message,
            available_files_=available_files_,
            total_count_=total_count_
        )

    @classmethod
    def from_json(cls, request_message, body_json):
        """
        Create a new instance of :class:`FileListAvailableFilesResponse` using a JSON string.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileListAvailableFilesResponse`.
        :rtype: FileListAvailableFilesResponse
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(request_message, body_dict)

    @classmethod
    def from_body_bytes(cls, request_message, body_bytes):
        """
        Create a new instance of :class:`FileListAvailableFilesResponse` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileListAvailableFilesResponse`.
        :rtype: FileListAvailableFilesResponse
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(request_message, body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileListAvailableFilesResponse` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileListAvailableFilesResponse`.
        :rtype: FileListAvailableFilesResponse
        """
        instance = cls.from_body_bytes(message, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        routing_key = MessageHeader.generate_routing_key(message.reply_to, cls.MESSAGE_NAME)
        instance.routing_key = routing_key
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        available_files_ = _serialize(self.available_files)
        total_count_ = _serialize(self.total_count)
        return {
            'availableFiles': available_files_,
            'totalCount': total_count_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_header.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileGetServerPathRequest(RequestMessage):
    """
    FileGetServerPathRequest JSON request message.
    """
    MESSAGE_NAME = 'FileGetServerPathRequest'

    def __init__(self,
                 id_=None):
        """
        :param id_: id
        :type id_: str
        """
        self.id = id_  # pylint: disable=invalid-name
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileGetServerPathRequest, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileGetServerPathRequest` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileGetServerPathRequest`.
        :rtype: FileGetServerPathRequest
        """
        id_ = _deserialize(body_dict.get('id'), 'str')  # pylint: disable=invalid-name
        return cls(
            id_=id_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileGetServerPathRequest` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileGetServerPathRequest`.
        :rtype: FileGetServerPathRequest
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileGetServerPathRequest` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileGetServerPathRequest`.
        :rtype: FileGetServerPathRequest
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileGetServerPathRequest` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileGetServerPathRequest`.
        :rtype: FileGetServerPathRequest
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_ = _serialize(self.id)  # pylint: disable=invalid-name
        return {
            'id': id_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileGetServerPathResponse(ResponseMessage):
    """
    FileGetServerPathResponse JSON response message.
    """
    MESSAGE_NAME = 'FileGetServerPathResponse'

    def __init__(self,
                 request_message,
                 path_=None):
        """
        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param path_: path
        :type path_: str
        """
        self.path = path_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        # If request_message is None, routing key needs to be set outside this constructor.
        if request_message:
            header.correlation_id = request_message.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_message.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        super(FileGetServerPathResponse, self).__init__(header, None)

    @classmethod
    def from_dict(cls, request_message, body_dict):
        """
        Create a new instance of :class:`FileGetServerPathResponse` using a dictionary.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileGetServerPathResponse`.
        :rtype: FileGetServerPathResponse
        """
        path_ = _deserialize(body_dict.get('path'), 'str')
        return cls(
            request_message,
            path_=path_
        )

    @classmethod
    def from_json(cls, request_message, body_json):
        """
        Create a new instance of :class:`FileGetServerPathResponse` using a JSON string.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileGetServerPathResponse`.
        :rtype: FileGetServerPathResponse
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(request_message, body_dict)

    @classmethod
    def from_body_bytes(cls, request_message, body_bytes):
        """
        Create a new instance of :class:`FileGetServerPathResponse` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileGetServerPathResponse`.
        :rtype: FileGetServerPathResponse
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(request_message, body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileGetServerPathResponse` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileGetServerPathResponse`.
        :rtype: FileGetServerPathResponse
        """
        instance = cls.from_body_bytes(message, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        routing_key = MessageHeader.generate_routing_key(message.reply_to, cls.MESSAGE_NAME)
        instance.routing_key = routing_key
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        path_ = _serialize(self.path)
        return {
            'path': path_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_header.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileQueryAvailableFilesRequest(RequestMessage):
    """
    FileQueryAvailableFilesRequest JSON request message.
    """
    MESSAGE_NAME = 'FileQueryAvailableFilesRequest'

    def __init__(self,
                 id_query_=None,
                 path_query_=None,
                 extension_query_=None,
                 size_max_query_=None,
                 size_min_query_=None,
                 created_query_=None,
                 properties_query_=None,
                 skip_=None,
                 take_=None):
        """
        :param id_query_: id_query
        :type id_query_: StringQueryEntry
        :param path_query_: path_query
        :type path_query_: StringQueryEntry
        :param extension_query_: extension_query
        :type extension_query_: StringQueryEntry
        :param size_max_query_: size_max_query
        :type size_max_query_: IntQueryEntry
        :param size_min_query_: size_min_query
        :type size_min_query_: IntQueryEntry
        :param created_query_: created_query
        :type created_query_: DateQueryEntry
        :param properties_query_: properties_query
        :type properties_query_: list(StringQueryEntry)
        :param skip_: skip
        :type skip_: int
        :param take_: take
        :type take_: int
        """
        self.id_query = id_query_
        self.path_query = path_query_
        self.extension_query = extension_query_
        self.size_max_query = size_max_query_
        self.size_min_query = size_min_query_
        self.created_query = created_query_
        self.properties_query = properties_query_
        self.skip = skip_
        self.take = take_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileQueryAvailableFilesRequest, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileQueryAvailableFilesRequest` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileQueryAvailableFilesRequest`.
        :rtype: FileQueryAvailableFilesRequest
        """
        id_query_ = _deserialize(body_dict.get('idQuery'), 'StringQueryEntry')
        path_query_ = _deserialize(body_dict.get('pathQuery'), 'StringQueryEntry')
        extension_query_ = _deserialize(body_dict.get('extensionQuery'), 'StringQueryEntry')
        size_max_query_ = _deserialize(body_dict.get('sizeMaxQuery'), 'IntQueryEntry')
        size_min_query_ = _deserialize(body_dict.get('sizeMinQuery'), 'IntQueryEntry')
        created_query_ = _deserialize(body_dict.get('createdQuery'), 'DateQueryEntry')
        properties_query_ = _deserialize(body_dict.get('propertiesQuery'), 'list(StringQueryEntry)')
        skip_ = _deserialize(body_dict.get('skip'), 'int')
        take_ = _deserialize(body_dict.get('take'), 'int')
        return cls(
            id_query_=id_query_,
            path_query_=path_query_,
            extension_query_=extension_query_,
            size_max_query_=size_max_query_,
            size_min_query_=size_min_query_,
            created_query_=created_query_,
            properties_query_=properties_query_,
            skip_=skip_,
            take_=take_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileQueryAvailableFilesRequest` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileQueryAvailableFilesRequest`.
        :rtype: FileQueryAvailableFilesRequest
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileQueryAvailableFilesRequest` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileQueryAvailableFilesRequest`.
        :rtype: FileQueryAvailableFilesRequest
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileQueryAvailableFilesRequest` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileQueryAvailableFilesRequest`.
        :rtype: FileQueryAvailableFilesRequest
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        id_query_ = _serialize(self.id_query)
        path_query_ = _serialize(self.path_query)
        extension_query_ = _serialize(self.extension_query)
        size_max_query_ = _serialize(self.size_max_query)
        size_min_query_ = _serialize(self.size_min_query)
        created_query_ = _serialize(self.created_query)
        properties_query_ = _serialize(self.properties_query)
        skip_ = _serialize(self.skip)
        take_ = _serialize(self.take)
        return {
            'idQuery': id_query_,
            'pathQuery': path_query_,
            'extensionQuery': extension_query_,
            'sizeMaxQuery': size_max_query_,
            'sizeMinQuery': size_min_query_,
            'createdQuery': created_query_,
            'propertiesQuery': properties_query_,
            'skip': skip_,
            'take': take_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileQueryAvailableFilesResponse(ResponseMessage):
    """
    FileQueryAvailableFilesResponse JSON response message.
    """
    MESSAGE_NAME = 'FileQueryAvailableFilesResponse'

    def __init__(self,
                 request_message,
                 available_files_=None,
                 total_count_=None):
        """
        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param available_files_: available_files
        :type available_files_: list(FileIngestionMetadata)
        :param total_count_: total_count
        :type total_count_: int
        """
        self.available_files = available_files_
        self.total_count = total_count_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        # If request_message is None, routing key needs to be set outside this constructor.
        if request_message:
            header.correlation_id = request_message.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_message.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        super(FileQueryAvailableFilesResponse, self).__init__(header, None)

    @classmethod
    def from_dict(cls, request_message, body_dict):
        """
        Create a new instance of :class:`FileQueryAvailableFilesResponse` using a dictionary.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileQueryAvailableFilesResponse`.
        :rtype: FileQueryAvailableFilesResponse
        """
        available_files_ = _deserialize(body_dict.get('availableFiles'), 'list(FileIngestionMetadata)')
        total_count_ = _deserialize(body_dict.get('totalCount'), 'int')
        return cls(
            request_message,
            available_files_=available_files_,
            total_count_=total_count_
        )

    @classmethod
    def from_json(cls, request_message, body_json):
        """
        Create a new instance of :class:`FileQueryAvailableFilesResponse` using a JSON string.

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileQueryAvailableFilesResponse`.
        :rtype: FileQueryAvailableFilesResponse
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(request_message, body_dict)

    @classmethod
    def from_body_bytes(cls, request_message, body_bytes):
        """
        Create a new instance of :class:`FileQueryAvailableFilesResponse` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param request_message: The request_message to use for reply information. May be None.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileQueryAvailableFilesResponse`.
        :rtype: FileQueryAvailableFilesResponse
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(request_message, body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileQueryAvailableFilesResponse` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileQueryAvailableFilesResponse`.
        :rtype: FileQueryAvailableFilesResponse
        """
        instance = cls.from_body_bytes(message, message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        routing_key = MessageHeader.generate_routing_key(message.reply_to, cls.MESSAGE_NAME)
        instance.routing_key = routing_key
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        available_files_ = _serialize(self.available_files)
        total_count_ = _serialize(self.total_count)
        return {
            'availableFiles': available_files_,
            'totalCount': total_count_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
            routing_key = MessageHeader.generate_routing_key(request_header.reply_to, self.MESSAGE_NAME)
            header.routing_key = routing_key
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileDeleteRoutedMessage(RoutedMessage):
    """
    FileDeleteRoutedMessage JSON routed message.
    """
    MESSAGE_NAME = 'FileDeleteRoutedMessage'

    def __init__(self,
                 ids_=None):
        """
        :param ids_: ids
        :type ids_: list(str)
        """
        self.ids = ids_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key('FileIngestion', self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileDeleteRoutedMessage, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileDeleteRoutedMessage` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileDeleteRoutedMessage`.
        :rtype: FileDeleteRoutedMessage
        """
        ids_ = _deserialize(body_dict.get('ids'), 'list(str)')
        return cls(
            ids_=ids_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileDeleteRoutedMessage` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileDeleteRoutedMessage`.
        :rtype: FileDeleteRoutedMessage
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileDeleteRoutedMessage` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileDeleteRoutedMessage`.
        :rtype: FileDeleteRoutedMessage
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileDeleteRoutedMessage` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileDeleteRoutedMessage`.
        :rtype: FileDeleteRoutedMessage
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        ids_ = _serialize(self.ids)
        return {
            'ids': ids_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileAvailableBroadcast(BroadcastMessage):
    """
    FileAvailableBroadcast JSON broadcast message.
    """
    MESSAGE_NAME = 'FileAvailableBroadcast'

    def __init__(self,
                 entity_=None,
                 metadata_=None):
        """
        :param entity_: entity
        :type entity_: Entity
        :param metadata_: metadata
        :type metadata_: FileIngestionMetadata
        """
        self.entity = entity_
        self.metadata = metadata_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(None, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileAvailableBroadcast, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileAvailableBroadcast` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileAvailableBroadcast`.
        :rtype: FileAvailableBroadcast
        """
        entity_ = _deserialize(body_dict.get('entity'), 'Entity')
        metadata_ = _deserialize(body_dict.get('metadata'), 'FileIngestionMetadata')
        return cls(
            entity_=entity_,
            metadata_=metadata_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileAvailableBroadcast` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileAvailableBroadcast`.
        :rtype: FileAvailableBroadcast
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileAvailableBroadcast` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileAvailableBroadcast`.
        :rtype: FileAvailableBroadcast
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileAvailableBroadcast` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileAvailableBroadcast`.
        :rtype: FileAvailableBroadcast
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        entity_ = _serialize(self.entity)
        metadata_ = _serialize(self.metadata)
        return {
            'entity': entity_,
            'metadata': metadata_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileUpdatedBroadcast(BroadcastMessage):
    """
    FileUpdatedBroadcast JSON broadcast message.
    """
    MESSAGE_NAME = 'FileUpdatedBroadcast'

    def __init__(self,
                 entity_=None,
                 metadata_=None):
        """
        :param entity_: entity
        :type entity_: Entity
        :param metadata_: metadata
        :type metadata_: FileIngestionMetadata
        """
        self.entity = entity_
        self.metadata = metadata_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(None, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileUpdatedBroadcast, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileUpdatedBroadcast` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileUpdatedBroadcast`.
        :rtype: FileUpdatedBroadcast
        """
        entity_ = _deserialize(body_dict.get('entity'), 'Entity')
        metadata_ = _deserialize(body_dict.get('metadata'), 'FileIngestionMetadata')
        return cls(
            entity_=entity_,
            metadata_=metadata_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileUpdatedBroadcast` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileUpdatedBroadcast`.
        :rtype: FileUpdatedBroadcast
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileUpdatedBroadcast` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileUpdatedBroadcast`.
        :rtype: FileUpdatedBroadcast
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileUpdatedBroadcast` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileUpdatedBroadcast`.
        :rtype: FileUpdatedBroadcast
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        entity_ = _serialize(self.entity)
        metadata_ = _serialize(self.metadata)
        return {
            'entity': entity_,
            'metadata': metadata_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body


class FileDeletedBroadcast(BroadcastMessage):
    """
    FileDeletedBroadcast JSON broadcast message.
    """
    MESSAGE_NAME = 'FileDeletedBroadcast'

    def __init__(self,
                 entity_=None,
                 metadata_=None):
        """
        :param entity_: entity
        :type entity_: Entity
        :param metadata_: metadata
        :type metadata_: FileIngestionMetadata
        """
        self.entity = entity_
        self.metadata = metadata_
        header = MessageHeader()
        header.message_name = self.MESSAGE_NAME
        header.content_type = JSON_MESSAGE_CONTENT_TYPE
        routing_key = MessageHeader.generate_routing_key(None, self.MESSAGE_NAME)
        header.routing_key = routing_key
        super(FileDeletedBroadcast, self).__init__(header, None)

    @classmethod
    def from_dict(cls, body_dict):
        """
        Create a new instance of :class:`FileDeletedBroadcast` using a dictionary.

        :param body_dict: The body as a dictionary.
        :type body_dict: dict
        :return: A new instance of :class:`FileDeletedBroadcast`.
        :rtype: FileDeletedBroadcast
        """
        entity_ = _deserialize(body_dict.get('entity'), 'Entity')
        metadata_ = _deserialize(body_dict.get('metadata'), 'FileIngestionMetadata')
        return cls(
            entity_=entity_,
            metadata_=metadata_
        )

    @classmethod
    def from_json(cls, body_json):
        """
        Create a new instance of :class:`FileDeletedBroadcast` using a JSON string.

        :param body_json: A string in JSON format representing the body.
        :type body_json: str
        :return: A new instance of :class:`FileDeletedBroadcast`.
        :rtype: FileDeletedBroadcast
        """
        body_dict = json.loads(body_json)
        return cls.from_dict(body_dict)

    @classmethod
    def from_body_bytes(cls, body_bytes):
        """
        Create a new instance of :class:`FileDeletedBroadcast` using a body
        of type :class:`bytes` or :class:`bytearray`,

        :param body_bytes: The body to use.
        :type body_bytes: bytes or bytearray
        :return: A new instance of :class:`FileDeletedBroadcast`.
        :rtype: FileDeletedBroadcast
        """
        body_json = str(body_bytes, 'utf-8')
        return cls.from_json(body_json)

    @classmethod
    def from_message(cls, message):
        """
        Create a new instance of :class`FileDeletedBroadcast` using a
        :class:`systemlink.messagebus.message_base.MessageBase` derived message.

        :param message: The message to use as the basis for this class instance.
        :type message: systemlink.messagebus.message_base.MessageBase
        :return: A new instance of :class`FileDeletedBroadcast`.
        :rtype: FileDeletedBroadcast
        """
        instance = cls.from_body_bytes(message.body_bytes)
        instance.correlation_id = message.correlation_id
        instance.reply_to = message.reply_to
        return instance

    def to_dict(self):
        """
        Returns a dictionary representing the data in this object.

        :return: A dictionary representing the data in this object.
        :rtype: dict
        """
        entity_ = _serialize(self.entity)
        metadata_ = _serialize(self.metadata)
        return {
            'entity': entity_,
            'metadata': metadata_
        }

    def to_json(self):
        """
        Returns a JSON string representing the data in this object.

        :return: A JSON string representing the data in this object.
        :rtype: str
        """
        body_dict = self.to_dict()
        return json.dumps(body_dict, separators=(',', ':'))

    def to_body_bytes(self):
        """
        Returns a :class:`bytearray` body representing the data in this object.

        :return: A :class:`bytearray` body representing the data in this object.
        :rtype: bytearray
        """
        body_json = self.to_json()
        return bytearray(body_json, 'utf-8')

    def to_message(self, request_message=None):
        """
        Returns a :class:`systemlink.messagebus.message_base.MessageBase`
        object representing the data in this object.

        :param request_message: Request message if this is a response.
        :type request_message: systemlink.messagebus.message_base.MessageBase or None
        :return: A :class:`systemlink.messagebus.message_base.MessageBase`
            object representing the data in this object.
        :rtype: systemlink.messagebus.message_base.MessageBase
        """
        header = self.header
        if request_message:
            request_header = request_message.header
            header.correlation_id = request_header.correlation_id
        body_bytes = self.to_body_bytes()
        return MessageBase(header, body_bytes)

    @property
    def body_bytes(self):
        """
        Returns a :class:`bytes` body representing the data in this object.

        :return: A :class:`bytes` body representing the data in this object.
        :rtype: bytes
        """
        self._body = self.to_body_bytes()  # pylint: disable=attribute-defined-outside-init
        return self._body
