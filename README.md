# AWS Knowledge Query Tool

> Query AWS documentation using the AWS Knowledge MCP Server. No AWS account required, completely free!

## 🚀 Quick Start

```bash
# 1. Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install mcp httpx flask

# 3. Choose your interface:

# Web UI (Recommended)
cd web
../venv/bin/python web_ui.py
# Open http://localhost:8080

# Command Line
venv/bin/python cli/ask_aws.py "How to create Lambda function"

# Interactive Chat
venv/bin/python cli/interactive_aws.py
```

## 📖 What is This?

This tool provides three ways to query AWS's official documentation through the **AWS Knowledge MCP Server** - a free, public endpoint that provides access to:

- AWS documentation across all services
- Regional availability information
- Service features and APIs
- Best practices and troubleshooting guides
- CDK and CloudFormation examples

**No AWS account needed. No authentication required. Completely free.**

## 📁 Project Structure

```
.
├── cli/
│   ├── ask_aws.py           # Quick CLI queries
│   └── interactive_aws.py   # Interactive chat mode
├── web/
│   ├── web_ui.py            # Flask web server
│   ├── start_web_ui.sh      # Startup script
│   ├── templates/
│   │   └── index.html       # Web UI template
│   └── static/
│       ├── css/style.css    # Styles
│       └── js/app.js        # Frontend logic
├── docs/                     # Documentation
├── venv/                     # Python virtual environment
└── README.md                 # This file
```

## 🎯 Three Ways to Use

### 1. Web UI - Best for Exploration

Beautiful web interface with real-time search, topic filtering, and quick examples.

```bash
cd web
../venv/bin/python web_ui.py
```

Then open `http://localhost:8080` in your browser.

**Features:**
- Modern, responsive design
- Topic filtering (8 categories)
- Quick example queries
- AWS regions viewer
- Mobile-friendly

📖 See [Web UI Guide](docs/WEB_UI_GUIDE.md) for details.

### 2. Command Line - Best for Automation

Fast queries perfect for scripts and CI/CD pipelines.

```bash
venv/bin/python cli/ask_aws.py "<question>" [topic] [limit]
```

**Examples:**
```bash
# Basic query
venv/bin/python cli/ask_aws.py "Lambda best practices"

# With topic
venv/bin/python cli/ask_aws.py "boto3 S3 upload" reference_documentation

# With limit
venv/bin/python cli/ask_aws.py "Lambda timeout" troubleshooting 3
```

📖 See [CLI Guide](docs/CLI_GUIDE.md) for details.

### 3. Interactive Mode - Best for Learning

Chat-style interface for exploring AWS documentation.

```bash
venv/bin/python cli/interactive_aws.py
```

**Commands:**
- `<question>` - Ask directly
- `topic <name>` - Change topic
- `regions` - List AWS regions
- `help` - Show help
- `quit` - Exit

📖 See [Interactive Guide](docs/INTERACTIVE_GUIDE.md) for details.

## 📚 Available Topics

| Topic | Use For | Example |
|-------|---------|---------|
| `general` | Best practices, architecture | "Lambda best practices" |
| `reference_documentation` | API/SDK/CLI docs | "boto3 S3 upload_file" |
| `troubleshooting` | Error messages, debugging | "Lambda timeout error" |
| `cdk_docs` | CDK concepts | "CDK stack construct" |
| `cdk_constructs` | CDK code examples | "Lambda CDK Python" |
| `cloudformation` | CloudFormation templates | "DynamoDB CloudFormation" |
| `current_awareness` | New features | "Lambda new features 2024" |
| `amplify_docs` | Amplify framework | "Amplify Auth React" |

## 💡 Examples

```bash
# General questions
venv/bin/python cli/ask_aws.py "S3 security best practices"

# API documentation
venv/bin/python cli/ask_aws.py "boto3 Lambda invoke" reference_documentation

# Troubleshooting
venv/bin/python cli/ask_aws.py "S3 access denied" troubleshooting

# CDK examples
venv/bin/python cli/ask_aws.py "API Gateway Lambda CDK" cdk_constructs

# New features
venv/bin/python cli/ask_aws.py "what's new in Lambda" current_awareness
```

## 🔧 Installation

### Prerequisites
- Python 3.10 or higher
- Internet connection

### Setup

```bash
# 1. Clone or download this project
cd aws-knowledge-query

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install mcp httpx flask

# 5. Verify installation
venv/bin/python cli/ask_aws.py --help
```

## 📖 Documentation

- [Web UI Guide](docs/WEB_UI_GUIDE.md) - Complete web interface guide
- [CLI Guide](docs/CLI_GUIDE.md) - Command-line tool reference
- [Interactive Guide](docs/INTERACTIVE_GUIDE.md) - Interactive mode guide
- [API Reference](docs/API_REFERENCE.md) - Using in your code
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions

## ❓ FAQ

**Q: Do I need an AWS account?**  
A: No! The AWS Knowledge MCP Server is completely public and free.

**Q: Is this free to use?**  
A: Yes, completely free. The service is rate-limited, so use responsibly.

**Q: Can I use this in production?**  
A: This is designed for development and learning. For production, consider implementing caching and rate limiting.

**Q: How current is the information?**  
A: The AWS Knowledge MCP Server is continuously updated by AWS with the latest documentation.

**Q: What's the endpoint?**  
A: `https://knowledge-mcp.global.api.aws` (public, no auth required)

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

Educational and development use. See AWS's terms for the MCP server.

## 🔗 Resources

- [AWS MCP Documentation](https://awslabs.github.io/mcp/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server)

---

**Made with ❤️ using AWS Knowledge MCP Server**
