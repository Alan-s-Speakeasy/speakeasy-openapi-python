# coding: utf-8

"""
    Alan's Speakeasy

    Full API for Alan's Speakeasy, Version 0.1

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UserRole(str, Enum):
    """
    UserRole
    """

    """
    allowed enum values
    """
    HUMAN = 'HUMAN'
    BOT = 'BOT'
    ADMIN = 'ADMIN'
    EVALUATOR = 'EVALUATOR'
    ASSISTANT = 'ASSISTANT'
    TESTER = 'TESTER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserRole from a JSON string"""
        return cls(json.loads(json_str))


