# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class BuiltInInfoType(_serialization.Model):
    """Pre-configured sensitive information type.

    :ivar name: Display name of the info type.
    :vartype name: str
    :ivar id: Id of the info type.
    :vartype id: str
    :ivar type: Category of the built-in info type.
    :vartype type: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        type: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: Display name of the info type.
        :paramtype name: str
        :keyword id: Id of the info type.
        :paramtype id: str
        :keyword type: Category of the built-in info type.
        :paramtype type: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.type = type


class CloudErrorBody(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.security.v2023_02_15_preview.models.CloudErrorBody]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.security.v2023_02_15_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class GetSensitivitySettingsListResponse(_serialization.Model):
    """A list with a single sensitivity settings resource.

    :ivar value:
    :vartype value:
     list[~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponse]
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[GetSensitivitySettingsResponse]"},
    }

    def __init__(
        self, *, value: Optional[List["_models.GetSensitivitySettingsResponse"]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value:
        :paramtype value:
         list[~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponse]
        """
        super().__init__(**kwargs)
        self.value = value


class GetSensitivitySettingsResponse(_serialization.Model):
    """Data sensitivity settings for sensitive data discovery.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the sensitivity settings.
    :vartype id: str
    :ivar type: The type of the sensitivity settings.
    :vartype type: str
    :ivar name: The name of the sensitivity settings.
    :vartype name: str
    :ivar properties: The sensitivity settings properties.
    :vartype properties:
     ~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponseProperties
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
        "name": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "properties": {"key": "properties", "type": "GetSensitivitySettingsResponseProperties"},
    }

    def __init__(
        self, *, properties: Optional["_models.GetSensitivitySettingsResponseProperties"] = None, **kwargs: Any
    ) -> None:
        """
        :keyword properties: The sensitivity settings properties.
        :paramtype properties:
         ~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponseProperties
        """
        super().__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = properties


class GetSensitivitySettingsResponseProperties(_serialization.Model):
    """The sensitivity settings properties.

    :ivar sensitive_info_types_ids: List of selected sensitive info types' IDs.
    :vartype sensitive_info_types_ids: list[str]
    :ivar sensitivity_threshold_label_order: The order of the sensitivity threshold label. Any
     label at or above this order will be considered sensitive. If set to -1, sensitivity by labels
     is turned off.
    :vartype sensitivity_threshold_label_order: float
    :ivar sensitivity_threshold_label_id: The id of the sensitivity threshold label. Any label at
     or above this rank will be considered sensitive.
    :vartype sensitivity_threshold_label_id: str
    :ivar mip_information: Microsoft information protection built-in and custom information types,
     labels, and integration status.
    :vartype mip_information:
     ~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponsePropertiesMipInformation
    """

    _attribute_map = {
        "sensitive_info_types_ids": {"key": "sensitiveInfoTypesIds", "type": "[str]"},
        "sensitivity_threshold_label_order": {"key": "sensitivityThresholdLabelOrder", "type": "float"},
        "sensitivity_threshold_label_id": {"key": "sensitivityThresholdLabelId", "type": "str"},
        "mip_information": {"key": "mipInformation", "type": "GetSensitivitySettingsResponsePropertiesMipInformation"},
    }

    def __init__(
        self,
        *,
        sensitive_info_types_ids: Optional[List[str]] = None,
        sensitivity_threshold_label_order: Optional[float] = None,
        sensitivity_threshold_label_id: Optional[str] = None,
        mip_information: Optional["_models.GetSensitivitySettingsResponsePropertiesMipInformation"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword sensitive_info_types_ids: List of selected sensitive info types' IDs.
        :paramtype sensitive_info_types_ids: list[str]
        :keyword sensitivity_threshold_label_order: The order of the sensitivity threshold label. Any
         label at or above this order will be considered sensitive. If set to -1, sensitivity by labels
         is turned off.
        :paramtype sensitivity_threshold_label_order: float
        :keyword sensitivity_threshold_label_id: The id of the sensitivity threshold label. Any label
         at or above this rank will be considered sensitive.
        :paramtype sensitivity_threshold_label_id: str
        :keyword mip_information: Microsoft information protection built-in and custom information
         types, labels, and integration status.
        :paramtype mip_information:
         ~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponsePropertiesMipInformation
        """
        super().__init__(**kwargs)
        self.sensitive_info_types_ids = sensitive_info_types_ids
        self.sensitivity_threshold_label_order = sensitivity_threshold_label_order
        self.sensitivity_threshold_label_id = sensitivity_threshold_label_id
        self.mip_information = mip_information


class GetSensitivitySettingsResponsePropertiesMipInformation(_serialization.Model):  # pylint: disable=name-too-long
    """Microsoft information protection built-in and custom information types, labels, and integration
    status.

    :ivar mip_integration_status: Microsoft information protection integration status. Known values
     are: "Ok", "noConsent", "noAutoLabelingRules", and "noMipLabels".
    :vartype mip_integration_status: str or
     ~azure.mgmt.security.v2023_02_15_preview.models.MipIntegrationStatus
    :ivar labels: List of Microsoft information protection sensitivity labels.
    :vartype labels: list[~azure.mgmt.security.v2023_02_15_preview.models.Label]
    :ivar custom_info_types: List of custom user-defined information types.
    :vartype custom_info_types: list[~azure.mgmt.security.v2023_02_15_preview.models.InfoType]
    :ivar built_in_info_types: List of pre-configured sensitive information types.
    :vartype built_in_info_types:
     list[~azure.mgmt.security.v2023_02_15_preview.models.BuiltInInfoType]
    """

    _attribute_map = {
        "mip_integration_status": {"key": "mipIntegrationStatus", "type": "str"},
        "labels": {"key": "labels", "type": "[Label]"},
        "custom_info_types": {"key": "customInfoTypes", "type": "[InfoType]"},
        "built_in_info_types": {"key": "builtInInfoTypes", "type": "[BuiltInInfoType]"},
    }

    def __init__(
        self,
        *,
        mip_integration_status: Optional[Union[str, "_models.MipIntegrationStatus"]] = None,
        labels: Optional[List["_models.Label"]] = None,
        custom_info_types: Optional[List["_models.InfoType"]] = None,
        built_in_info_types: Optional[List["_models.BuiltInInfoType"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword mip_integration_status: Microsoft information protection integration status. Known
         values are: "Ok", "noConsent", "noAutoLabelingRules", and "noMipLabels".
        :paramtype mip_integration_status: str or
         ~azure.mgmt.security.v2023_02_15_preview.models.MipIntegrationStatus
        :keyword labels: List of Microsoft information protection sensitivity labels.
        :paramtype labels: list[~azure.mgmt.security.v2023_02_15_preview.models.Label]
        :keyword custom_info_types: List of custom user-defined information types.
        :paramtype custom_info_types: list[~azure.mgmt.security.v2023_02_15_preview.models.InfoType]
        :keyword built_in_info_types: List of pre-configured sensitive information types.
        :paramtype built_in_info_types:
         list[~azure.mgmt.security.v2023_02_15_preview.models.BuiltInInfoType]
        """
        super().__init__(**kwargs)
        self.mip_integration_status = mip_integration_status
        self.labels = labels
        self.custom_info_types = custom_info_types
        self.built_in_info_types = built_in_info_types


class InfoType(_serialization.Model):
    """Custom user-defined information type.

    :ivar name: Display name of the info type.
    :vartype name: str
    :ivar id: Id of the info type.
    :vartype id: str
    :ivar description: Description of the info type.
    :vartype description: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        description: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: Display name of the info type.
        :paramtype name: str
        :keyword id: Id of the info type.
        :paramtype id: str
        :keyword description: Description of the info type.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.description = description


class Label(_serialization.Model):
    """Microsoft information protection sensitivity label.

    :ivar name: The display name of the label.
    :vartype name: str
    :ivar id: The ID of the label.
    :vartype id: str
    :ivar order: Labels are ordered by sensitivity level. The higher the order of the label, the
     more sensitive it is.
    :vartype order: float
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "order": {"key": "order", "type": "float"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        order: Optional[float] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: The display name of the label.
        :paramtype name: str
        :keyword id: The ID of the label.
        :paramtype id: str
        :keyword order: Labels are ordered by sensitivity level. The higher the order of the label, the
         more sensitive it is.
        :paramtype order: float
        """
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.order = order


class UpdateSensitivitySettingsRequest(_serialization.Model):
    """Request to update data sensitivity settings for sensitive data discovery.

    All required parameters must be populated in order to send to server.

    :ivar sensitive_info_types_ids: List of selected sensitive info types' IDs. Required.
    :vartype sensitive_info_types_ids: list[str]
    :ivar sensitivity_threshold_label_order: The order of the sensitivity threshold label. Any
     label at or above this order will be considered sensitive. If set to -1, sensitivity by labels
     is turned off.
    :vartype sensitivity_threshold_label_order: float
    :ivar sensitivity_threshold_label_id: The id of the sensitivity threshold label. Any label at
     or above this rank will be considered sensitive.
    :vartype sensitivity_threshold_label_id: str
    """

    _validation = {
        "sensitive_info_types_ids": {"required": True},
    }

    _attribute_map = {
        "sensitive_info_types_ids": {"key": "sensitiveInfoTypesIds", "type": "[str]"},
        "sensitivity_threshold_label_order": {"key": "sensitivityThresholdLabelOrder", "type": "float"},
        "sensitivity_threshold_label_id": {"key": "sensitivityThresholdLabelId", "type": "str"},
    }

    def __init__(
        self,
        *,
        sensitive_info_types_ids: List[str],
        sensitivity_threshold_label_order: Optional[float] = None,
        sensitivity_threshold_label_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword sensitive_info_types_ids: List of selected sensitive info types' IDs. Required.
        :paramtype sensitive_info_types_ids: list[str]
        :keyword sensitivity_threshold_label_order: The order of the sensitivity threshold label. Any
         label at or above this order will be considered sensitive. If set to -1, sensitivity by labels
         is turned off.
        :paramtype sensitivity_threshold_label_order: float
        :keyword sensitivity_threshold_label_id: The id of the sensitivity threshold label. Any label
         at or above this rank will be considered sensitive.
        :paramtype sensitivity_threshold_label_id: str
        """
        super().__init__(**kwargs)
        self.sensitive_info_types_ids = sensitive_info_types_ids
        self.sensitivity_threshold_label_order = sensitivity_threshold_label_order
        self.sensitivity_threshold_label_id = sensitivity_threshold_label_id
