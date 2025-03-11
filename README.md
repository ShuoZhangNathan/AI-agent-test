# AI Agent RAG System

基于 LangChain 的智能代理系统，支持文档处理、向量检索和工具调用。

## 项目特点

- 文档处理：支持 PDF、Word、Excel 格式
- 知识库：FAISS + SQLite 实现增量更新
- 模型集成：DeepSeek
- 工具集成：数据分析、代码生成
- 交互方式：Web 界面（Gradio）

## 项目结构
ai-agent-rag-system/
├── api/          # API 接口层
│   └── routers/  # 路由模块
├── core/         # 核心业务逻辑
│   ├── document_loader/  # 文档处理
│   ├── vector_store/    # 向量存储
│   ├── agents/         # AI代理
│   └── models/        # 模型集成
├── data/         # 数据存储
│   ├── docs/    # 原始文档
│   ├── vector_stores/  # FAISS索引
│   └── sqlite/  # SQLite数据库
├── tests/        # 测试用例
├── tools/        # 工具函数
└── web/          # Web界面


## 核心功能

1. **文档处理**
   - PDF、Word、Excel 解析
   - 文本分割和预处理
   - 增量更新支持

2. **向量检索**
   - FAISS 向量索引
   - SQLite 元数据存储
   - 高效检索算法

3. **AI 代理**
   - 任务规划
   - 工具调用
   - 上下文管理

4. **Web 界面**
   - 文档上传
   - 实时问答
   - 系统监控

## 快速开始

1. 安装依赖
```bash
pip install -r requirements.txt

2. 运行服务
python main.py

## API 接口
- POST /ingest：上传文档
- POST /query：文本问答
- GET /status：系统状态检查
## 开发计划
- 项目基础架构
- 文档处理模块
- 向量存储实现
- AI 代理集成
- Web 界面开发
- 测试用例编写
## 技术栈
- FastAPI：Web框架
- LangChain：AI框架
- FAISS：向量检索
- SQLite：数据存储
- Gradio：界面开发
- DeepSeek：大语言模型