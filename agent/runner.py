import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from agent.tool_schemas import TOOLS
from agent.tools import add

# 初始化Deepseek APIkey
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("未找到 DEEPSEEK_API_KEY，请检查项目根目录下的 .env 文件")

client = OpenAI(
    api_key = api_key,
    base_url = "https://api.deepseek.com"
)


def run_agent_once(question:str):
    """
    执行一次 Agent 请求。

    当前支持：
    1. LLM 直接回答；
    2. LLM 调用 add 工具后再生成最终回答。

    Args:
        question (str):
            用户问题。

    Returns:
        str:
            Agent 最终回答。
    """

    messages = [
    {
    "role":"user",
    "content": question
        }
    ]

    response = client.chat.completions.create(
        model = "deepseek-v4-flash",
        messages = messages,
        tools = TOOLS,
        extra_body={
            "thinking":{
                "type":"disabled"
            }
        }
    )

    message = response.choices[0].message

    # 情况 1：LLM 请求调用工具
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        arguments = json.loads(tool_call.function.arguments)

        if tool_call.function.name == "add":
            result = add(
                arguments["a"],
                arguments["b"]
            )
        else:
            raise ValueError(
                f"未知工具: {tool_call.function.name}"
            )

        #  保存模型第一次的 Tool Call
        messages.append(message)

        # 保存真正的 Tool Result
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )

        # 第二次调用 LLM
        final_response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=messages,
            tools=TOOLS,
            extra_body={
                "thinking": {
                    "type": "disabled"
                }
            }
        )

        final_message = final_response.choices[0].message

        return final_message.content

    # 情况 2：LLM 不需要调用工具
    return message.content or ""

# 测试
if __name__ == "__main__":
    answer = run_agent_once(
        "请使用加法工具计算 17.5 + 24.5"
    )
    print(answer)
