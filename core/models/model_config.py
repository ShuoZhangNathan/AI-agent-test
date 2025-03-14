import os
import asyncio
import requests

from dotenv import load_dotenv
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

async def test_deepseek():
    try:
        model_client = OpenAIChatCompletionClient(
            model="deepseek-chat",
            base_url="https://api.siliconflow.cn/v1",
            api_key=os.getenv('DEEPSEEK_API_KEY'),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"
            },
            model_info={
                # 基础参数
                "model_type": "chat",  # 模型类型
                "vendor": "DeepSeek",  # 供应商
                "family": "deepseek-chat",  # 模型家族
                "context_length": 32768,  # 上下文长度
                "max_tokens": 4096,  # 最大输出token数
                "default_max_tokens": 2048,  # 默认输出token数
                
                # 功能支持参数
                "vision": False,  # 是否支持视觉
                "supports_vision": False,  # 是否支持视觉
                "function_calling": False,  # 是否支持函数调用
                "supports_function_calling": False,  # 是否支持函数调用
                "json_output": False,  # 是否支持JSON输出
                "supports_json_output": False,  # 是否支持JSON输出
                "supports_system_message": True,  # 是否支持系统消息
                "supports_files": False,  # 是否支持文件
                "supports_parallel_tool_calls": False,  # 是否支持并行工具调用
                
                # 运行时参数
                "timeout": 60,  # 超时时间
                "content_moderation": False  # 是否开启内容审核
            }
        )

        messages = [
            {"role": "user", "content": "法国的首都是哪里？"}  # 使用字典格式替代Message类
        ]
        response = await model_client.create(messages=messages)
        # 修改响应处理方式
        print("完整响应:", response)  # 先打印完整响应查看结构
        print("回答:", response['choices'][0]['message']['content'])  # 根据实际结构调整
        
    except Exception as e:
        print("错误:", str(e))

if __name__ == "__main__":
    asyncio.run(test_deepseek())