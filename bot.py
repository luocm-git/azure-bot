# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import heapq
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions
from flask import Config
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
class QusCnter:
    def __init__(self, name: str, base: int):
        self.name = name
        self.cnt = base
g_top_questions = [QusCnter('大赛介绍',3),
                   QusCnter('大赛规则',2),
                   QusCnter('奖项设置',4),
                   QusCnter('课程',1)]
# 增加问题被访问的次数
def inc_ques_cnt(name):
    for ques in g_top_questions:
        if (ques.name == name):
            ques.cnt += 1
            return
    g_top_questions.append(QusCnter(name,1))

# 获取访问频率最高的前n个问题名称列表
def get_top_ques(n: int):
    res_lst = sorted(g_top_questions, key=lambda que: que.cnt, reverse=True)
    cnt = min(len(res_lst), n)
    return [res_lst[i].name for i in range(cnt)]

class MyBot(ActivityHandler):
    def __init__(self, config: Config):
        self.config = config
        self.qna_maker = QnAMaker(
                QnAMakerEndpoint(
                    knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                    endpoint_key=config.QNA_ENDPOINT_KEY,
                    host=config.QNA_ENDPOINT_HOST,
               )
        )

    async def on_message_activity(self, turn_context: TurnContext):
        # 从QnA 服务中获取答案
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            inc_ques_cnt(response[0].questions[0])
            reply = MessageFactory.text(response[0].answer)
            # 展示建议操作
            prompts = [prompt.display_text for prompt in response[0].context.prompts]
            if (len(prompts) > 0):
                await self._construt_suggested_actions(reply, prompts)
            await turn_context.send_activity(reply)
        else:
            await turn_context.send_activity("No QnA Maker answers were found.")

    async def _construt_suggested_actions(self, reply, prompts):
        """
        Creates and sends an activity with suggested actions to the user. When the user
        clicks one of the buttons the text value from the "CardAction" will be displayed
        in the channel just as if the user entered the text. There are multiple
        "ActionTypes" that may be used for different situations.
        """
        cardActions = [CardAction(title=prompt,
                                  type=ActionTypes.im_back,
                                  value=prompt) for prompt in prompts]
        reply.suggested_actions = SuggestedActions( actions=cardActions)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):

        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                reply = MessageFactory.text("### 高频问题：")
                top_ques = get_top_ques(3)
                await self._construt_suggested_actions(reply, top_ques)
                await turn_context.send_activity(reply)
