# AWS Knowledge Query Tool - Documentation

Complete documentation for the AWS Knowledge Query Tool.

## 📚 Documentation Index

### Getting Started
- [Main README](../README.md) - Quick start and overview
- [Installation Guide](#installation) - Detailed setup instructions

### User Guides
- [CLI Guide](CLI_GUIDE.md) - Command-line interface reference
- [Interactive Mode Guide](INTERACTIVE_GUIDE.md) - Chat-style interface guide
- [Web UI Guide](WEB_UI_GUIDE.md) - Web interface documentation

### Developer Resources
- [API Reference](API_REFERENCE.md) - Python API documentation
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions

## 🎯 What is This Tool?

The AWS Knowledge Query Tool provides three interfaces to query AWS's official documentation through the **AWS Knowledge MCP Server**:

1. **Web UI** - Beautiful web interface with real-time search
2. **CLI** - Fast command-line queries for automation
3. **Interactive** - Chat-style interface for exploration

**Key Features:**
- ✅ No AWS account required
- ✅ No authentication needed
- ✅ Completely free to use
- ✅ Access to all AWS documentation
- ✅ 8 specialized topic categories
- ✅ Regional availability information

## 🚀 Quick Start

### 1. Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install mcp httpx flask
```

### 2. Choose Your Interface

**Web UI (Recommended for beginners):**
```bash
cd web
../venv/bin/python web_ui.py
# Open http://localhost:8080
```

**CLI (Best for automation):**
```bash
venv/bin/python cli/ask_aws.py "How to create Lambda function"
```

**Interactive (Best for learning):**
```bash
venv/bin/python cli/interactive_aws.py
```

## 📖 Documentation Guides

### [CLI Guide](CLI_GUIDE.md)

Complete reference for the command-line interface.

**Topics covered:**
- Basic usage and syntax
- All 8 topic categories explained
- Examples for each topic
- Tips for better results
- Shell scripting integration
- Advanced usage patterns

**Quick example:**
```bash
venv/bin/python cli/ask_aws.py "Lambda best practices" general 5
```

### [Interactive Mode Guide](INTERACTIVE_GUIDE.md)

Guide for the chat-style interactive interface.

**Topics covered:**
- All available commands
- Example sessions
- Workflow tips
- Topic switching
- Viewing regions
- Learning paths

**Quick example:**
```bash
venv/bin/python cli/interactive_aws.py
💬 You: Lambda best practices
💬 You: topic cdk_constructs
💬 You: Lambda CDK Python
```

### [Web UI Guide](WEB_UI_GUIDE.md)

Complete guide for the web interface.

**Topics covered:**
- Starting the web server
- Using the search interface
- Topic filtering
- Quick examples
- API endpoints
- Customization
- Production deployment

**Quick example:**
```bash
cd web
../venv/bin/python web_ui.py
# Open http://localhost:8080
```

### [API Reference](API_REFERENCE.md)

Python API documentation for developers.

**Topics covered:**
- AWSAssistant class reference
- All methods and parameters
- Complete code examples
- Error handling
- Flask integration
- Custom applications

**Quick example:**
```python
from cli.interactive_aws import AWSAssistant

assistant = AWSAssistant()
await assistant.connect()
results = await assistant.ask("Lambda best practices")
await assistant.disconnect()
```

### [Troubleshooting](TROUBLESHOOTING.md)

Solutions to common issues.

**Topics covered:**
- Installation issues
- Connection problems
- Query issues
- Web UI problems
- Interactive mode issues
- Script/automation issues
- Advanced debugging

**Quick diagnosis:**
```bash
# Check setup
python3 --version
ls -la venv/
venv/bin/pip list | grep -E "mcp|httpx|flask"
curl https://knowledge-mcp.global.api.aws
```

## 📚 Topic Categories

The tool provides 8 specialized topic categories for better search results:

| Topic | Description | Best For |
|-------|-------------|----------|
| **general** | Best practices, architecture, tutorials | Learning, architecture design |
| **reference_documentation** | API/SDK/CLI documentation | Code implementation, API usage |
| **troubleshooting** | Error messages, debugging | Fixing errors, debugging |
| **cdk_docs** | CDK concepts, API reference | Learning CDK, understanding concepts |
| **cdk_constructs** | CDK code examples, patterns | Writing CDK code, IaC |
| **cloudformation** | CloudFormation templates | Writing CloudFormation, SAM |
| **current_awareness** | New features, announcements | Staying updated, new features |
| **amplify_docs** | Amplify framework | Web/mobile app development |

## 💡 Common Use Cases

### Learning AWS Services

**Goal:** Understand a new AWS service

**Approach:**
1. Start with Web UI or Interactive mode
2. Use `general` topic
3. Ask "What is [service]"
4. Ask about best practices
5. Look for getting started guides

**Example:**
```bash
venv/bin/python cli/interactive_aws.py
💬 You: What is Lambda
💬 You: Lambda best practices
💬 You: Lambda getting started
```

### Finding API Documentation

**Goal:** Find boto3 or AWS CLI documentation

**Approach:**
1. Use CLI or Interactive mode
2. Use `reference_documentation` topic
3. Include SDK/CLI name in query
4. Be specific about the operation

**Example:**
```bash
venv/bin/python cli/ask_aws.py "boto3 S3 upload_file" reference_documentation
venv/bin/python cli/ask_aws.py "aws lambda invoke CLI" reference_documentation
```

### Troubleshooting Errors

**Goal:** Fix an error or issue

**Approach:**
1. Use any interface
2. Use `troubleshooting` topic
3. Include exact error message
4. Include service name

**Example:**
```bash
venv/bin/python cli/ask_aws.py "Lambda timeout error" troubleshooting
venv/bin/python cli/ask_aws.py "S3 AccessDenied" troubleshooting
```

### Writing CDK Code

**Goal:** Write infrastructure as code with CDK

**Approach:**
1. Use Web UI or Interactive mode
2. Start with `cdk_docs` for concepts
3. Switch to `cdk_constructs` for examples
4. Include language (Python, TypeScript, etc.)

**Example:**
```bash
venv/bin/python cli/interactive_aws.py
💬 You: topic cdk_docs
💬 You: CDK stack construct
💬 You: topic cdk_constructs
💬 You: Lambda function CDK Python
```

### Staying Updated

**Goal:** Learn about new AWS features

**Approach:**
1. Use any interface
2. Use `current_awareness` topic
3. Ask about specific service updates
4. Ask "what's new"

**Example:**
```bash
venv/bin/python cli/ask_aws.py "Lambda new features 2024" current_awareness
venv/bin/python cli/ask_aws.py "what's new in S3" current_awareness
```

## 🔧 Installation

### Prerequisites

- **Python 3.10 or higher**
- **Internet connection**
- **pip** (Python package manager)

### Step-by-Step Installation

#### 1. Check Python Version

```bash
python3 --version
# Should show 3.10 or higher
```

If you need to install Python:
- **macOS:** `brew install python@3.11`
- **Ubuntu:** `sudo apt install python3.11`
- **Windows:** Download from [python.org](https://python.org)

#### 2. Create Virtual Environment

```bash
# Navigate to project directory
cd aws-knowledge-query

# Create virtual environment
python3 -m venv venv

# Verify it was created
ls -la venv/
```

#### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` in your prompt.

#### 4. Install Dependencies

```bash
pip install mcp httpx flask
```

#### 5. Verify Installation

```bash
# Check installed packages
pip list | grep -E "mcp|httpx|flask"

# Test CLI
venv/bin/python cli/ask_aws.py --help

# Test connection
venv/bin/python cli/ask_aws.py "test query"
```

### Troubleshooting Installation

See [Troubleshooting Guide](TROUBLESHOOTING.md) for detailed solutions.

**Common issues:**
- Python version too old → Install Python 3.10+
- Module not found → Activate venv and install dependencies
- Permission denied → Use `sudo` or check file permissions

## 🌐 Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Your Application                      │
│  ┌──────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  Web UI  │  │     CLI      │  │   Interactive    │  │
│  │ (Flask)  │  │ (ask_aws.py) │  │ (interactive.py) │  │
│  └────┬─────┘  └──────┬───────┘  └────────┬─────────┘  │
│       │               │                    │             │
│       └───────────────┴────────────────────┘             │
│                       │                                  │
└───────────────────────┼──────────────────────────────────┘
                        │
                        │ HTTPS
                        ▼
        ┌───────────────────────────────────┐
        │  AWS Knowledge MCP Server         │
        │  knowledge-mcp.global.api.aws     │
        │                                   │
        │  - Search documentation           │
        │  - List regions                   │
        │  - Check availability             │
        └───────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  AWS Documentation Database       │
        │  - All service docs               │
        │  - API references                 │
        │  - Best practices                 │
        │  - Code examples                  │
        └───────────────────────────────────┘
```

### MCP Tools Available

The AWS Knowledge MCP Server provides these tools:

1. **aws___search_documentation** - Search AWS docs by topic
2. **aws___read_documentation** - Fetch specific doc pages
3. **aws___recommend** - Get related documentation
4. **aws___list_regions** - List all AWS regions
5. **aws___get_regional_availability** - Check service availability

## 📊 Project Structure

```
aws-knowledge-query/
├── cli/
│   ├── ask_aws.py              # CLI tool
│   └── interactive_aws.py      # Interactive mode
├── web/
│   ├── web_ui.py               # Flask server
│   ├── start_web_ui.sh         # Startup script
│   ├── templates/
│   │   └── index.html          # HTML template
│   └── static/
│       ├── css/
│       │   └── style.css       # Styles
│       └── js/
│           └── app.js          # Frontend logic
├── docs/
│   ├── README.md               # This file
│   ├── CLI_GUIDE.md            # CLI documentation
│   ├── INTERACTIVE_GUIDE.md    # Interactive mode docs
│   ├── WEB_UI_GUIDE.md         # Web UI documentation
│   ├── API_REFERENCE.md        # Python API reference
│   └── TROUBLESHOOTING.md      # Troubleshooting guide
├── venv/                        # Virtual environment
└── README.md                    # Main README
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional examples
- Better error handling
- Performance optimizations
- New features
- Documentation improvements
- Bug fixes

## 📄 License

Educational and development use. See AWS's terms for the MCP server.

## 🔗 External Resources

- [AWS MCP Documentation](https://awslabs.github.io/mcp/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server)
- [AWS Documentation](https://docs.aws.amazon.com/)

## ❓ FAQ

**Q: Do I need an AWS account?**  
A: No! The AWS Knowledge MCP Server is completely public and free.

**Q: Is this free to use?**  
A: Yes, completely free. The service is rate-limited, so use responsibly.

**Q: Can I use this in production?**  
A: This is designed for development and learning. For production, implement caching and rate limiting.

**Q: How current is the information?**  
A: The AWS Knowledge MCP Server is continuously updated by AWS.

**Q: Can I contribute?**  
A: Yes! Contributions are welcome.

**Q: Where can I get help?**  
A: Check the [Troubleshooting Guide](TROUBLESHOOTING.md) or review the relevant user guide.

---

**Made with ❤️ using AWS Knowledge MCP Server**

*Last Updated: February 2026*
