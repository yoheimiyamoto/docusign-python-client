# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DisplayApplianceSignerAttachment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attachment_description=None, attachment_tab_id=None, document_id=None, envelope_id=None, page_count=None, page_id=None, recipient_id=None):
        """
        DisplayApplianceSignerAttachment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attachment_description': 'str',
            'attachment_tab_id': 'str',
            'document_id': 'str',
            'envelope_id': 'str',
            'page_count': 'int',
            'page_id': 'str',
            'recipient_id': 'str'
        }

        self.attribute_map = {
            'attachment_description': 'attachmentDescription',
            'attachment_tab_id': 'attachmentTabId',
            'document_id': 'documentId',
            'envelope_id': 'envelopeId',
            'page_count': 'pageCount',
            'page_id': 'pageId',
            'recipient_id': 'recipientId'
        }

        self._attachment_description = attachment_description
        self._attachment_tab_id = attachment_tab_id
        self._document_id = document_id
        self._envelope_id = envelope_id
        self._page_count = page_count
        self._page_id = page_id
        self._recipient_id = recipient_id

    @property
    def attachment_description(self):
        """
        Gets the attachment_description of this DisplayApplianceSignerAttachment.
        

        :return: The attachment_description of this DisplayApplianceSignerAttachment.
        :rtype: str
        """
        return self._attachment_description

    @attachment_description.setter
    def attachment_description(self, attachment_description):
        """
        Sets the attachment_description of this DisplayApplianceSignerAttachment.
        

        :param attachment_description: The attachment_description of this DisplayApplianceSignerAttachment.
        :type: str
        """

        self._attachment_description = attachment_description

    @property
    def attachment_tab_id(self):
        """
        Gets the attachment_tab_id of this DisplayApplianceSignerAttachment.
        

        :return: The attachment_tab_id of this DisplayApplianceSignerAttachment.
        :rtype: str
        """
        return self._attachment_tab_id

    @attachment_tab_id.setter
    def attachment_tab_id(self, attachment_tab_id):
        """
        Sets the attachment_tab_id of this DisplayApplianceSignerAttachment.
        

        :param attachment_tab_id: The attachment_tab_id of this DisplayApplianceSignerAttachment.
        :type: str
        """

        self._attachment_tab_id = attachment_tab_id

    @property
    def document_id(self):
        """
        Gets the document_id of this DisplayApplianceSignerAttachment.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :return: The document_id of this DisplayApplianceSignerAttachment.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this DisplayApplianceSignerAttachment.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :param document_id: The document_id of this DisplayApplianceSignerAttachment.
        :type: str
        """

        self._document_id = document_id

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this DisplayApplianceSignerAttachment.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this DisplayApplianceSignerAttachment.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this DisplayApplianceSignerAttachment.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this DisplayApplianceSignerAttachment.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def page_count(self):
        """
        Gets the page_count of this DisplayApplianceSignerAttachment.
        

        :return: The page_count of this DisplayApplianceSignerAttachment.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this DisplayApplianceSignerAttachment.
        

        :param page_count: The page_count of this DisplayApplianceSignerAttachment.
        :type: int
        """

        self._page_count = page_count

    @property
    def page_id(self):
        """
        Gets the page_id of this DisplayApplianceSignerAttachment.
        

        :return: The page_id of this DisplayApplianceSignerAttachment.
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """
        Sets the page_id of this DisplayApplianceSignerAttachment.
        

        :param page_id: The page_id of this DisplayApplianceSignerAttachment.
        :type: str
        """

        self._page_id = page_id

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this DisplayApplianceSignerAttachment.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this DisplayApplianceSignerAttachment.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this DisplayApplianceSignerAttachment.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this DisplayApplianceSignerAttachment.
        :type: str
        """

        self._recipient_id = recipient_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
