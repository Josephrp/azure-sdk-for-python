# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.media import AzureMediaServices

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-media
# USAGE
    python streamingendpointcreate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureMediaServices(
        credential=DefaultAzureCredential(),
        subscription_id="0a6ec948-5a62-437d-b9df-934dc7c1b722",
    )

    response = client.streaming_endpoints.begin_create(
        resource_group_name="mediaresources",
        account_name="slitestmedia10",
        streaming_endpoint_name="myStreamingEndpoint1",
        parameters={
            "location": "West US",
            "properties": {
                "accessControl": {
                    "akamai": {
                        "akamaiSignatureHeaderAuthenticationKeyList": [
                            {
                                "base64Key": "dGVzdGlkMQ==",
                                "expiration": "2029-12-31T16:00:00-08:00",
                                "identifier": "id1",
                            },
                            {
                                "base64Key": "dGVzdGlkMQ==",
                                "expiration": "2030-12-31T16:00:00-08:00",
                                "identifier": "id2",
                            },
                        ]
                    },
                    "ip": {"allow": [{"address": "192.168.1.1", "name": "AllowedIp"}]},
                },
                "availabilitySetName": "availableset",
                "cdnEnabled": False,
                "description": "test event 1",
                "scaleUnits": 1,
            },
            "tags": {"tag1": "value1", "tag2": "value2"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mediaservices/resource-manager/Microsoft.Media/Streaming/stable/2022-08-01/examples/streamingendpoint-create.json
if __name__ == "__main__":
    main()
