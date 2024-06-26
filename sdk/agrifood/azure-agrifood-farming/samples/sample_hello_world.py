# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""
FILE: sample_hello_world.py

DESCRIPTION:
    This sample demonstrates the most basic operation that can be 
    performed - creation of a Party. Use this to understand how to 
    create the client object, how to authenticate it, and make sure 
    your client is set up correctly to call into your FarmBeats endpoint.

USAGE:
    ```python sample_hello_world.py```

    Set the environment variables with your own values before running the sample:
    - `AZURE_TENANT_ID`: The tenant ID of your active directory application.
    - `AZURE_CLIENT_ID`: The client ID of your active directory application.
    - `AZURE_CLIENT_SECRET`: The client secret of your active directory application.
    - `FARMBEATS_ENDPOINT`: The FarmBeats endpoint that you want to run these samples on.
"""

from azure.identity import DefaultAzureCredential
from azure.agrifood.farming import FarmBeatsClient
import os
from dotenv import load_dotenv
import random


def sample_hello_world():

    farmbeats_endpoint = os.environ['FARMBEATS_ENDPOINT']

    credential = DefaultAzureCredential()

    client = FarmBeatsClient(
        endpoint=farmbeats_endpoint,
        credential=credential
    )

    party_id = f"contoso-party-{random.randint(0,1000)}"
    party_name = "Contoso"
    party_description = "Contoso is hard working."

    print("Creating party, or updating if party already exists...", end=" ", flush=True)
    party = client.parties.create_or_update(
        party_id=party_id,
        party={
            "name": party_name,
            "description": party_description,
            "status": "Sample Status",
            "properties": {
                "foo": "bar",
                "numeric one": 1,
                1: "numeric key"
            }
        }
    )
    print("Done")
    
    print("Here are the details of the party:")
    print("\tID:", party["id"])
    print("\tName:", party["name"])
    print("\tDescription:", party["description"])
    print("\tCreated timestamp:", party["createdDateTime"])
    print("\tLast modified timestamp:", party["modifiedDateTime"])


if __name__ == "__main__":

    load_dotenv()

    sample_hello_world()
