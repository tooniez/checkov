from __future__ import annotations

from typing import Any

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.arm.base_resource_value_check import BaseResourceValueCheck


class EventHubNamespaceMinTLS12(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure Event Hub Namespace uses at least TLS 1.2"
        id = "CKV_AZURE_223"
        supported_resources = ["Microsoft.EventHub/namespaces", ]
        categories = [CheckCategories.ENCRYPTION, ]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources,
                         missing_block_result=CheckResult.PASSED)

    def get_inspected_key(self) -> str:
        return "properties/minimumTlsVersion"

    def get_expected_value(self) -> Any:
        return "1.2"


check = EventHubNamespaceMinTLS12()
