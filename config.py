#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "e0a81fb2-460e-4871-9fca-50dad1466ce3")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "lcm_tst_bt1")
