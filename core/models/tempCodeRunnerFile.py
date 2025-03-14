# 使用新的导入方式
from langchain_ollama import Ollama
from langchain_ollama import ChatOllama

# 使用本地 Ollama 模型
model = ChatOllama(
    model="deepseek-r1:1.5b",
    base_url="http://localhost:11434"
)

# 测试模型
response = model.invoke("你好，请介绍一下你自己")
print(response)