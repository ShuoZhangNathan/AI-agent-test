# AI Agent RAG System

An intelligent agent system based on LangChain, supporting document processing, vector retrieval, and tool invocation.

## Project Features

- ​**Document Processing**: Supports PDF, Word, and Excel formats.
- ​**Knowledge Base**: FAISS + SQLite for incremental updates.
- ​**Model Integration**: DeepSeek.
- ​**Tool Integration**: Data analysis, code generation.
- ​**Interaction**: Web interface (Gradio).

## Project Structure
ai-agent-rag-system/
├── api/          # API Layer
│   └── routers/  # Routing Modules
├── core/         # Core Business Logic
│   ├── document_loader/  # Document Processing
│   ├── vector_store/    # Vector Storage
│   ├── agents/         # AI Agents
│   └── models/        # Model Integration
├── data/         # Data Storage
│   ├── docs/    # Raw Documents
│   ├── vector_stores/  # FAISS Indexes
│   └── sqlite/  # SQLite Database
├── tests/        # Test Cases
├── tools/        # Utility Functions
└── web/          # Web Interface


## Core Features

1. ​**Document Processing**
   - PDF, Word, Excel parsing.
   - Text segmentation and preprocessing.
   - Support for incremental updates.

2. ​**Vector Retrieval**
   - FAISS vector indexing.
   - SQLite metadata storage.
   - Efficient retrieval algorithms.

3. ​**AI Agent**
   - Task planning.
   - Tool invocation.
   - Context management.

4. ​**Web Interface**
   - Document upload.
   - Real-time Q&A.
   - System monitoring.

## Quick Start

1. **Install dependencies:**

pip install -r requirements.txt

2. **Run the application:**

python main.py


API Endpoints
​POST /ingest: Upload documents.
​POST /query: Text-based Q&A.
​GET /status: System status check.
Development Plan
Project infrastructure setup.
Document processing module.
Vector storage implementation.
AI agent integration.
Web interface development.
Test case writing.
Tech Stack
​FastAPI: Web framework.
​LangChain: AI framework.
​FAISS: Vector retrieval.
​SQLite: Data storage.
​Gradio: Interface development.
​DeepSeek: Large language model.