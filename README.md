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

## 🌐 AWS MCP Server Endpoints

This project uses AWS's public MCP servers. Here are the official endpoints:

### 1. AWS Knowledge MCP Server (No Auth Required) ✅ Default
```
https://knowledge-mcp.global.api.aws
```
**Features:**
- Documentation search across all AWS services
- Regional availability information
- Best practices and tutorials
- Code examples

**Authentication:** None required  
**Cost:** Free  
**Documentation:** [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server)

---

### 2. AWS MCP Server (Requires AWS Credentials)
```
https://mcp.{region}.api.aws
```
**Features:**
- Full AWS API access (15,000+ APIs)
- Execute AWS CLI commands
- Multi-step workflows (Agent SOPs)
- IAM-based authentication
- CloudTrail audit logging

**Authentication:** AWS IAM credentials required  
**Cost:** Pay for AWS resources used  
**Documentation:** [AWS MCP Server User Guide](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html)

**Example Regions:**
- `https://mcp.us-east-1.api.aws`
- `https://mcp.us-west-2.api.aws`
- `https://mcp.eu-west-1.api.aws`

---

### 3. AWS EKS MCP Server (Requires AWS Credentials)
```
https://eks-mcp.{region}.api.aws/mcp
```
**Features:**
- Kubernetes cluster management
- EKS-specific operations
- kubectl command execution
- Read-only mode available

**Authentication:** AWS IAM credentials required  
**IAM Permissions:** `eks-mcp:InvokeMcp`, `eks-mcp:CallReadOnlyTool`  
**Documentation:** [Amazon EKS MCP Server](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html)

**Example:**
```json
{
  "mcpServers": {
    "eks-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://eks-mcp.us-west-2.api.aws/mcp",
        "--service", "eks-mcp",
        "--region", "us-east-1",
        "--read-only"
      ]
    }
  }
}
```

---

### 4. AWS ECS MCP Server (Requires AWS Credentials)
```
https://ecs-mcp.{region}.api.aws/mcp
```
**Features:**
- Container orchestration
- ECS task and service management
- Application deployment

**Authentication:** AWS IAM credentials required  
**Documentation:** [Amazon ECS MCP Server](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-mcp-tool-configurations.html)

---

## 📚 Where to Find These URLs

**Official AWS Documentation:**
1. [AWS MCP Servers Overview](https://awslabs.github.io/mcp/)
2. [AWS MCP Server User Guide](https://docs.aws.amazon.com/aws-mcp/latest/userguide/)
3. [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server)
4. [Amazon EKS MCP Configuration](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html)
5. [Amazon ECS MCP Configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-mcp-tool-configurations.html)

**GitHub Repository:**
- [awslabs/mcp](https://github.com/awslabs/mcp) - Official AWS MCP Servers source code

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
A: No, for the Knowledge MCP server. Yes, for AWS MCP (Core) and EKS MCP.

**Q: Is this free?**  
A: Yes, the Knowledge MCP server is free. Other endpoints may incur AWS charges.

**Q: Can I use this in production?**  
A: For learning/development. For production, consider rate limits and caching.

## 📝 License

Educational and development use. See AWS's terms for the MCP servers.

---

**Made with ❤️ using AWS Knowledge MCP Server**
