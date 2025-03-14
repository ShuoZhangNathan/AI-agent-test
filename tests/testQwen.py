import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

# 新增 messages 字段，包含用户输入
payload = {
    "model": "Qwen/QwQ-32B",
    "messages": [  # 👈 必须添加的对话内容
        {"role": "user", "content": "写一段关于AI的科普"}  # 用户输入的文本
    ],
    "stream": False,
    "max_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 51,
    "frequency_penalty": 0.5,
    "n": 1
}

headers = {
    "Authorization": "Bearer sk-tewxqnoaikjjzwqnvtesiaruggtohespjmgeidzqtawcnxoy",
    "Content-Type": "application/json"
}

# 发送请求并处理可能的错误
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # 检查HTTP状态码（如401、429等错误）
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except ValueError:
    print("响应内容解析失败")