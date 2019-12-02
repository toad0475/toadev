#!/usr/bin/env python3

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        # NOTE: client will automatically disconnect at the end of the scope
        # == Simple RPC without argument

        # print("Getting Wwise instance information:")
        # result = client.call("ak.wwise.core.getInfo")
        # pprint(result)
        
        # == RPC with arguments
        print("Query the Default Work Unit information:")
        object_get_args = {
            "from": {
                "id": ["{4064325C-264E-4362-8132-F07ACA6D3E3F}"]
            },
            "options": {
                "return": ["@ConeAttenuation",
                           "@ConeInnerAngle",
                           "@ConeOuterAngle",
                           "@ConeUse",
                           "@RadiusMax"]
            }
        }
        result = client.call("ak.wwise.core.object.get", object_get_args)
        pprint(result)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
