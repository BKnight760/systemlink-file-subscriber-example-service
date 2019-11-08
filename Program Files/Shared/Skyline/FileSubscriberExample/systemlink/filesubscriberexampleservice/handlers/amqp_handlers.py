# -*- coding: utf-8 -*-
"""
Message handlers for the File Subscriber Example Service's AMQP messages.
"""
from __future__ import absolute_import, print_function

# Import python libs
import atexit
import json
import logging
import os.path
from typing import List, Optional

import requests

# Import local libs
from systemlink.messagebus.error import Error
from systemlink.messagebus.exceptions import SystemLinkException
from systemlink.messagebus.managed_service_base import ManagedServiceBase
from systemlink.messagebus.mixins.serialization import SerializationMixin
from systemlink.fileingestionclient import messages as fileingestion_messages
from systemlink.messagebus.generic_message import GenericMessage

# Set up logging
LOGGER = logging.getLogger(__name__)

AMQP_HANDLER = None

BUFFER_SIZE = 32768
REMOTE_USER = 'REMOTE_USER'
REQUEST_METHOD = 'REQUEST_METHOD'
VERSION_INT = 1
VERSION_STR = 'v' + str(VERSION_INT)


def register(managed_service: ManagedServiceBase):
    """
    Register one or more handlers.

    :param managed_service: An instance of the managed service.
    :type managed_service:
        systemlink.filesubscriberexampleservice.managed_service.FileSubscriberExampleService
    """
    global AMQP_HANDLER  # pylint: disable=global-statement

    AMQP_HANDLER = AmqpHandler(managed_service)
    atexit.register(_unregister)


def _unregister():
    """
    Unregister handlers.
    """
    global AMQP_HANDLER  # pylint: disable=global-statement

    if AMQP_HANDLER is not None:
        AMQP_HANDLER.close()
        AMQP_HANDLER = None


class AmqpHandler():
    """
    The AMQP handler.
    """
    def __init__(
            self,
            managed_service: ManagedServiceBase):
        """
        :param managed_service: An instance of the managed service.
        :type managed_service:
            systemlink.filesubscriberexampleservice.managed_service.FileSubscriberExampleService
        """
        self._managed_service = managed_service
        self._managed_service.register_work_subscriber_callback(
            fileingestion_messages.FileAvailableBroadcast,  # pylint: disable=invalid-name
            self.file_available_broadcast, message_name=None)
        LOGGER.error('Registered for File Available broadcast!')

    def __del__(self):
        self.close()

    def close(self):
        """
        Close all associated resources.
        """
        pass


    def file_available_broadcast(
            self,
            generic_message: GenericMessage,
        ):
        """
        :param generic_message: An object representing the AMQP message.
        """
        try:
            broadcast = fileingestion_messages.FileAvailableBroadcast.from_message(generic_message)
            LOGGER.error('Received File Available broadcaast: {}'.format(broadcast.to_body_bytes()))
            LOGGER.error('File Name: {}'.format(broadcast.metadata.properties['Name']))
            if 'Foo' in broadcast.metadata.properties:
                pass
                # TODO: Customize the code here to perform your task
        except Exception as e:
            LOGGER.error('FileSubscriberExample threw an exception: {}'.format(str(e)))
            pass
