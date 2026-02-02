# AWS Knowledge MCP Server - Query Tools

> Query AWS documentation and services using AWS's public MCP server endpoint. No deployment, no AWS account, completely free!

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Command Line Tool](#command-line-tool)
  - [Interactive Mode](#interactive-mode)
  - [Use in Your Code](#use-in-your-code)
- [Available Topics](#available-topics)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## 🎯 Overview

This project provides three ways to query AWS's official documentation and services through the **AWS Knowledge MCP Server** - a free, public endpoint managed by AWS.

**What is MCP?**  
Model Context Protocol (MCP) is an open standard that enables AI systems to communicate with external data sources. AWS provides a public MCP server with access to:
- AWS documentation across all services
- Regional availability information
- Service features and APIs
- Best practices and tutorials

**Endpoint:** `https://knowledge-mcp.global.api.aws`

---

## ✨ Features

### 🔍 Search AWS Documentation
- Search across 8 specialized topic categories
- Get official AWS documentation instantly
- Filter by service, API, troubleshooting, CDK, CloudFormation, etc.

### 🌍 Regional Information
- List all AWS regions
- Check service availability by region
- Verify CloudFormation resource support

### 💻 Three Interfaces
- **Web UI** - Beautiful web interface with modern design ⭐ NEW!
- **CLI Tool** - Quick command-line queries with arguments
- **Interactive Mode** - Chat-style interface for exploration

### 🚀 No Setup Required
- ✅ No AWS account needed
- ✅ No authentication required
- ✅ No deployment necessary
- ✅ Completely free to use

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- Internet connection

### Setup Steps

```bash
# 1. Clone or download this project
cd mcp-project

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# 4. Install dependencies
pip install mcp httpx

# 5. Verify installation
python ask_aws.py --help
```

**That's it!** You're ready to query AWS documentation.

---

## 🚀 Quick Start

### Option 1: Web UI (Recommended for Beginners)

```bash
# Start the web interface
./start_web_ui.sh

# Open your browser to: http://localhost:8080
```

**Features:** Beautiful UI, real-time search, mobile-friendly, quick examples

📖 See [WEB_UI_GUIDE.md](WEB_UI_GUIDE.md) for complete web UI documentation.

### Option 2: Command Line

```bash
# Ask a question
python ask_aws.py "How to create a Lambda function"
```

### Option 3: Interactive Mode

```bash
# Start interactive chat
python interactive_aws.py
```

---

## 📘 Usage

### Web UI

**Start the server:**
```bash
./start_web_ui.sh
```

Then open `http://localhost:8080` in your browser.

**Features:**
- Search with topic filtering
- Quick example buttons
- View AWS regions
- Mobile-responsive design
- Real-time results

### Try Your First Query

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Ask a question
python ask_aws.py "How to create a Lambda function"
```

You should see results from AWS documentation instantly!

---

## 📘 Usage

### Command Line Tool

**Syntax:**
```bash
python ask_aws.py "<question>" [topic] [limit]
```

**Arguments:**
- `question` (required) - Your question in quotes
- `topic` (optional) - Topic category (default: `general`)
- `limit` (optional) - Number of results (default: 5, max: 10)

**Examples:**

```bash
# Basic question (uses default 'general' topic)
python ask_aws.py "How to create a Lambda function"

# Specify topic for better results
python ask_aws.py "boto3 S3 upload file" reference_documentation

# Limit number of results
python ask_aws.py "Lambda timeout error" troubleshooting 3

# CDK code examples
python ask_aws.py "Lambda function CDK Python" cdk_constructs

# Check new features
python ask_aws.py "Lambda new features 2024" current_awareness
```

**Get Help:**
```bash
python ask_aws.py --help
```

---

### Interactive Mode

Start an interactive chat session:

```bash
python interactive_aws.py
```

**Available Commands:**

| Command | Description | Example |
|---------|-------------|---------|
| `<question>` | Ask directly (no command needed) | `How to use Lambda?` |
| `ask <question>` | Ask explicitly | `ask Lambda pricing` |
| `topic <name>` | Change current topic | `topic cdk_docs` |
| `topics` | List all available topics | `topics` |
| `regions` | List all AWS regions | `regions` |
| `available <service>` | Check service availability | `available AWS Lambda` |
| `help` | Show help message | `help` |
| `quit` or `exit` | Exit the assistant | `quit` |

**Example Session:**

```
💬 You: How to create a Lambda function
[Results displayed...]

💬 You: topic cdk_constructs
✅ Topic changed to: cdk_constructs

💬 You: Lambda function CDK Python
[CDK examples displayed...]

💬 You: regions
[AWS regions listed...]

💬 You: quit
👋 Goodbye!
```

---

### Use in Your Code

Import and use the tools in your Python scripts:

#### Option 1: Simple Query Function

```python
import asyncio
from ask_aws import ask_aws

# Ask a question
asyncio.run(ask_aws("How to create Lambda", "general", 5))
```

#### Option 2: Assistant Class (More Control)

```python
import asyncio
from interactive_aws import AWSAssistant

async def main():
    # Create assistant
    assistant = AWSAssistant()
    
    # Connect to AWS MCP server
    await assistant.connect()
    
    # Search documentation
    results = await assistant.ask("Lambda best practices", "general", 5)
    
    # Process results
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Context: {result.get('context', 'N/A')[:200]}...")
        print()
    
    # List regions
    regions = await assistant.list_regions()
    print(f"Total AWS Regions: {len(regions)}")
    
    # Check availability
    availability = await assistant.check_availability("AWS Lambda")
    print(f"Lambda availability data: {len(availability)} items")
    
    # Disconnect
    await assistant.disconnect()

# Run
asyncio.run(main())
```

---

## 📚 Available Topics

Choose the right topic for better, more relevant results:

| Topic | Use For | Example Queries |
|-------|---------|-----------------|
| **general** | Best practices, architecture, tutorials | "Lambda best practices"<br>"S3 security patterns" |
| **reference_documentation** | API/SDK/CLI documentation | "boto3 S3 upload_file"<br>"Lambda InvokeFunction API" |
| **troubleshooting** | Error messages, debugging | "Lambda timeout error"<br>"AccessDenied S3" |
| **cdk_docs** | CDK concepts, API reference | "CDK stack construct"<br>"cdk deploy command" |
| **cdk_constructs** | CDK code examples, patterns | "Lambda function CDK Python"<br>"API Gateway CDK" |
| **cloudformation** | CloudFormation templates | "DynamoDB CloudFormation"<br>"SAM template" |
| **current_awareness** | New features, announcements | "Lambda new features 2024"<br>"what's new in S3" |
| **amplify_docs** | Amplify framework (web/mobile) | "Amplify Auth React"<br>"Amplify Storage Flutter" |

**💡 Tip:** When in doubt, use `general` - it works for most questions!

---

## 📖 Examples

### General AWS Questions

```bash
# Architecture and best practices
python ask_aws.py "Lambda best practices"
python ask_aws.py "S3 security best practices"
python ask_aws.py "DynamoDB vs RDS comparison"
python ask_aws.py "Serverless architecture patterns"
```

### API/SDK Documentation

```bash
# Python boto3
python ask_aws.py "boto3 S3 upload_file parameters" reference_documentation
python ask_aws.py "boto3 Lambda invoke" reference_documentation

# AWS CLI
python ask_aws.py "aws s3 cp command syntax" reference_documentation
python ask_aws.py "aws lambda invoke CLI" reference_documentation
```

### Troubleshooting Errors

```bash
# Common errors
python ask_aws.py "Lambda timeout error" troubleshooting
python ask_aws.py "S3 access denied error" troubleshooting
python ask_aws.py "DynamoDB throttling" troubleshooting
python ask_aws.py "API Gateway 403 error" troubleshooting
```

### CDK Development

```bash
# CDK concepts
python ask_aws.py "CDK stack construct TypeScript" cdk_docs
python ask_aws.py "CDK best practices Python" cdk_docs

# CDK code examples
python ask_aws.py "Lambda function CDK Python example" cdk_constructs
python ask_aws.py "API Gateway Lambda CDK TypeScript" cdk_constructs
python ask_aws.py "DynamoDB table CDK" cdk_constructs
```

### CloudFormation Templates

```bash
python ask_aws.py "Lambda function CloudFormation template" cloudformation
python ask_aws.py "DynamoDB table CloudFormation" cloudformation
python ask_aws.py "SAM template API Gateway" cloudformation
```

### New Features & Updates

```bash
python ask_aws.py "Lambda new features 2024" current_awareness
python ask_aws.py "S3 latest updates" current_awareness
python ask_aws.py "what's new in ECS" current_awareness
```

### Amplify Framework

```bash
python ask_aws.py "Amplify authentication React" amplify_docs
python ask_aws.py "Amplify GraphQL API Next.js" amplify_docs
python ask_aws.py "Amplify Storage Flutter" amplify_docs
```

---

## 🔧 Troubleshooting

### No Results Found

**Problem:** Query returns no results

**Solutions:**
1. Try a different topic category
2. Rephrase your question to be more specific
3. Use service names explicitly (e.g., "Lambda" instead of "function")
4. Try the `general` topic for broad questions

### Connection Errors

**Problem:** Cannot connect to MCP server

**Solutions:**
1. Check your internet connection
2. Verify the endpoint is accessible: `curl https://knowledge-mcp.global.api.aws`
3. Check if you're behind a firewall/proxy
4. Try again later (service may be temporarily unavailable)

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'mcp'`

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install mcp httpx
```

### Rate Limiting

**Problem:** Getting rate limited

**Solution:**
- The service is free but rate-limited
- Wait a few minutes between large batches of queries
- Use responsibly

---

## ❓ FAQ

### Do I need an AWS account?
**No!** The AWS Knowledge MCP Server is completely public and free. No AWS account or credentials required.

### Is this free to use?
**Yes!** The service is provided by AWS at no cost. However, it is rate-limited, so use responsibly.

### Can I use this in production?
This is designed for development and learning. For production use cases, consider:
- Deploying your own MCP server
- Using AWS's official SDKs and APIs
- Implementing proper caching and rate limiting

### What data sources does it use?
The AWS Knowledge MCP Server indexes:
- AWS official documentation
- AWS blog posts
- What's New announcements
- Getting Started guides
- Code examples and samples
- CloudFormation/CDK documentation

### Can I search multiple topics at once?
Via CLI: One topic at a time  
Via code: Yes, pass a list of topics to the `ask()` function

### How current is the information?
The AWS Knowledge MCP Server is continuously updated by AWS with the latest documentation and announcements.

### Is my query data stored?
Refer to AWS's privacy policy for the Knowledge MCP Server. Generally, queries may be logged for service improvement.

---

## 🌐 Technical Details

### Architecture

```
┌─────────────────────┐
│   Your Script       │
│  (ask_aws.py or     │
│  interactive_aws.py)│
└──────────┬──────────┘
           │ HTTPS
           ▼
┌─────────────────────────────────────┐
│  https://knowledge-mcp.global.api.aws│
│  (AWS Managed MCP Server)           │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────┐
│  AWS Documentation  │
│  AWS Services Data  │
│  Regional Info      │
└─────────────────────┘
```

### MCP Tools Available

The AWS Knowledge MCP Server provides 5 tools:

1. **aws___search_documentation** - Search AWS docs by topic
2. **aws___read_documentation** - Fetch specific doc pages
3. **aws___recommend** - Get related documentation
4. **aws___list_regions** - List all AWS regions
5. **aws___get_regional_availability** - Check service availability

### Dependencies

- **mcp** - Model Context Protocol client library
- **httpx** - HTTP client for async requests
- **Python 3.10+** - Required for async/await support

---

## 📁 Project Structure

```
mcp-project/
├── ask_aws.py           # CLI tool for quick queries
├── interactive_aws.py   # Interactive chat interface
├── README.md            # This file
├── USAGE.md             # Quick reference guide
└── venv/                # Python virtual environment
```

---

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Fork and modify for your needs
- Add new features
- Improve error handling
- Add more examples

---

## 📄 License

This project is provided as-is for educational and development purposes. The AWS Knowledge MCP Server is provided by AWS - refer to AWS's terms of service.

---

## 🔗 Resources

- [AWS MCP Documentation](https://awslabs.github.io/mcp/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server)

---

**Made with ❤️ using AWS Knowledge MCP Server**

*Last Updated: February 2026*
