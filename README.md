# AWS Knowledge MCP Server - Query Tools

> Query AWS documentation using AWS's public MCP server. No deployment, no AWS account, completely free!

## 🚀 Quick Start

```bash
# 1. Setup
python3 -m venv venv
venv/bin/pip install mcp httpx flask

# 2. Choose your interface:

# Web UI (Recommended)
./web/start_web_ui.sh
# → Open http://localhost:8080

# Command Line
venv/bin/python cli/ask_aws.py "How to create Lambda"

# Interactive Chat
venv/bin/python cli/interactive_aws.py
```

## 📁 Project Structure

```
mcp-project/
├── cli/                      # Command-line tools
│   ├── ask_aws.py           # Quick queries with arguments
│   └── interactive_aws.py   # Interactive chat mode
├── web/                      # Web interface
│   ├── web_ui.py            # Flask backend
│   ├── start_web_ui.sh      # Startup script
│   ├── templates/           # HTML templates
│   └── static/              # CSS & JavaScript
├── docs/                     # Documentation
│   ├── WEB_UI_GUIDE.md      # Web UI guide
│   └── USAGE.md             # Quick reference
├── venv/                     # Python environment
└── README.md                 # This file
```

## 🎯 Three Ways to Use

### 1. Web UI (Best for Exploration)
```bash
./web/start_web_ui.sh
```
- Beautiful interface
- Real-time search
- Quick examples
- Mobile-friendly

### 2. Command Line (Best for Automation)
```bash
venv/bin/python cli/ask_aws.py "your question" [topic] [limit]
```
- Fast queries
- Scriptable
- CI/CD friendly

### 3. Interactive Mode (Best for Learning)
```bash
venv/bin/python cli/interactive_aws.py
```
- Chat interface
- Topic switching
- Region viewer

## 📚 Available Topics

- `general` - Best practices, architecture
- `reference_documentation` - API/SDK/CLI docs
- `troubleshooting` - Errors and debugging
- `cdk_docs` - CDK concepts
- `cdk_constructs` - CDK code examples
- `cloudformation` - CloudFormation templates
- `current_awareness` - New features
- `amplify_docs` - Amplify framework

## 📖 Documentation

- [Web UI Guide](docs/WEB_UI_GUIDE.md) - Complete web interface documentation
- [Usage Guide](docs/USAGE.md) - Quick reference for all tools


## 💡 Examples

```bash
# Web UI
./web/start_web_ui.sh

# CLI - General question
venv/bin/python cli/ask_aws.py "Lambda best practices"

# CLI - API documentation
venv/bin/python cli/ask_aws.py "boto3 S3 upload" reference_documentation

# CLI - Troubleshooting
venv/bin/python cli/ask_aws.py "Lambda timeout" troubleshooting 3

# Interactive
venv/bin/python cli/interactive_aws.py
```

## 🔧 OpenSearch Encryption at Rest

**Question:** Can we enable encryption at rest in an existing OpenSearch cluster?

**Answer:** No, encryption at rest cannot be enabled on an existing OpenSearch domain. You must:

1. Create a new domain with encryption enabled
2. Migrate data from old to new domain
3. Update application endpoints

**Steps:**
```bash
# 1. Create new domain with encryption
aws opensearch create-domain \
  --domain-name my-new-domain \
  --encryption-at-rest-options Enabled=true,KmsKeyId=your-kms-key

# 2. Use snapshot/restore or reindex to migrate data
# 3. Update DNS/application configs
# 4. Delete old domain
```

**Alternative:** Use AWS DMS or custom scripts for data migration.

## ❓ FAQ

**Q: Do I need an AWS account?**  
A: No, for the Knowledge MCP server. 

**Q: Is this free?**  
A: Yes, the Knowledge MCP server is free. Other endpoints may incur AWS charges.

**Q: Can I use this in production?**  
A: For learning/development. For production, consider rate limits and caching.

## 📝 License

Educational and development use. See AWS's terms for the MCP servers.

---

**Made with ❤️ using AWS Knowledge MCP Server**
