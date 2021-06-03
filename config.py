#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    #APP_ID = os.environ.get("MicrosoftAppId", "e0a81fb2-460e-4871-9fca-50dad1466ce3")
    #APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "lcm_tst_bt1")
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "51720ee9-893d-41a6-8cca-78d5245623ea")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "2a8acc03-74b1-4f4b-b25c-27e2c69ef4d9")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://lcm-qna-service.azurewebsites.net/qnamaker")
    WELCOME_WORD = "### 欢迎来到黑客松大赛问答中心:\n\r**高频问题列表**\n\r* [学习路径](https://www.baidu.com)\n\r* [赛事主页](https://www.microsoft.com/china/azure/hackathon/index.html?trackcode=osccommu)"
