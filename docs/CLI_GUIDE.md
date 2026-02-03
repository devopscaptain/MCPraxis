# Command Line Interface Guide

Complete guide for using the AWS Knowledge Query CLI tool.

## 🎯 Overview

The CLI tool (`ask_aws.py`) provides a fast, scriptable way to query AWS documentation from the command line. Perfect for:

- Quick documentation lookups
- Shell scripts and automation
- CI/CD pipelines
- Terminal-based workflows

## 🚀 Basic Usage

```bash
venv/bin/python cli/ask_aws.py "<question>" [topic] [limit]
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `question` | Yes | - | Your question (use quotes) |
| `topic` | No | `general` | Topic category |
| `limit` | No | `5` | Number of results (max 10) |

## 📚 Examples

### Basic Queries

```bash
# Simple question (uses default 'general' topic)
venv/bin/python cli/ask_aws.py "How to create a Lambda function"

# Get help
venv/bin/python cli/ask_aws.py --help
```

### With Topic Selection

```bash
# API documentation
venv/bin/python cli/ask_aws.py "boto3 S3 upload_file" reference_documentation

# Troubleshooting
venv/bin/python cli/ask_aws.py "Lambda timeout error" troubleshooting

# CDK examples
venv/bin/python cli/ask_aws.py "Lambda function CDK Python" cdk_constructs

# CloudFormation
venv/bin/python cli/ask_aws.py "DynamoDB table template" cloudformation
```

### With Result Limit

```bash
# Get only 3 results
venv/bin/python cli/ask_aws.py "S3 security" general 3

# Get maximum 10 results
venv/bin/python cli/ask_aws.py "Lambda best practices" general 10
```

## 📖 Available Topics

### general
Best practices, architecture patterns, and tutorials.

**Use for:**
- Architecture questions
- Best practices
- Service comparisons
- Getting started guides

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "Lambda best practices"
venv/bin/python cli/ask_aws.py "S3 security patterns"
venv/bin/python cli/ask_aws.py "DynamoDB vs RDS"
venv/bin/python cli/ask_aws.py "Serverless architecture"
```

### reference_documentation
API, SDK, and CLI documentation.

**Use for:**
- boto3 (Python SDK) documentation
- AWS CLI commands
- API references
- SDK method signatures

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "boto3 S3 upload_file" reference_documentation
venv/bin/python cli/ask_aws.py "aws lambda invoke CLI" reference_documentation
venv/bin/python cli/ask_aws.py "Lambda InvokeFunction API" reference_documentation
venv/bin/python cli/ask_aws.py "DynamoDB PutItem boto3" reference_documentation
```

### troubleshooting
Error messages and debugging guides.

**Use for:**
- Error messages
- Debugging issues
- Common problems
- Resolution steps

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "Lambda timeout error" troubleshooting
venv/bin/python cli/ask_aws.py "S3 access denied" troubleshooting
venv/bin/python cli/ask_aws.py "DynamoDB throttling" troubleshooting
venv/bin/python cli/ask_aws.py "API Gateway 403" troubleshooting
```

### cdk_docs
AWS CDK concepts and API reference.

**Use for:**
- CDK getting started
- CDK concepts
- CDK API reference
- CDK best practices

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "CDK stack construct" cdk_docs
venv/bin/python cli/ask_aws.py "CDK best practices" cdk_docs
venv/bin/python cli/ask_aws.py "CDK deployment" cdk_docs
```

### cdk_constructs
CDK code examples and patterns.

**Use for:**
- Working code examples
- CDK patterns
- Infrastructure as code
- Multi-language examples

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "Lambda function CDK Python" cdk_constructs
venv/bin/python cli/ask_aws.py "API Gateway Lambda CDK" cdk_constructs
venv/bin/python cli/ask_aws.py "DynamoDB table CDK TypeScript" cdk_constructs
venv/bin/python cli/ask_aws.py "S3 bucket CDK" cdk_constructs
```

### cloudformation
CloudFormation templates and examples.

**Use for:**
- CloudFormation templates
- SAM templates
- Resource definitions
- Template examples

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "Lambda CloudFormation template" cloudformation
venv/bin/python cli/ask_aws.py "DynamoDB CloudFormation" cloudformation
venv/bin/python cli/ask_aws.py "SAM template API Gateway" cloudformation
venv/bin/python cli/ask_aws.py "EventBridge rule CloudFormation" cloudformation
```

### current_awareness
New features and announcements.

**Use for:**
- Latest features
- What's new
- Service updates
- New capabilities

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "Lambda new features 2024" current_awareness
venv/bin/python cli/ask_aws.py "what's new in S3" current_awareness
venv/bin/python cli/ask_aws.py "ECS latest updates" current_awareness
venv/bin/python cli/ask_aws.py "RDS new capabilities" current_awareness
```

### amplify_docs
Amplify framework documentation.

**Use for:**
- Amplify web/mobile apps
- Amplify authentication
- Amplify APIs
- Framework-specific guides

**Examples:**
```bash
venv/bin/python cli/ask_aws.py "Amplify Auth React" amplify_docs
venv/bin/python cli/ask_aws.py "Amplify GraphQL API" amplify_docs
venv/bin/python cli/ask_aws.py "Amplify Storage Flutter" amplify_docs
```

## 💡 Tips for Better Results

### Be Specific

❌ Bad: `venv/bin/python cli/ask_aws.py "error"`  
✅ Good: `venv/bin/python cli/ask_aws.py "Lambda timeout error" troubleshooting`

### Include Service Names

❌ Bad: `venv/bin/python cli/ask_aws.py "upload file"`  
✅ Good: `venv/bin/python cli/ask_aws.py "boto3 S3 upload_file" reference_documentation`

### Use Exact Error Messages

❌ Bad: `venv/bin/python cli/ask_aws.py "access problem"`  
✅ Good: `venv/bin/python cli/ask_aws.py "AccessDenied S3" troubleshooting`

### Choose the Right Topic

❌ Bad: `venv/bin/python cli/ask_aws.py "boto3 S3" general`  
✅ Good: `venv/bin/python cli/ask_aws.py "boto3 S3" reference_documentation`

### Include Language/Framework

❌ Bad: `venv/bin/python cli/ask_aws.py "Lambda CDK" cdk_constructs`  
✅ Good: `venv/bin/python cli/ask_aws.py "Lambda CDK Python" cdk_constructs`

## 🔧 Advanced Usage

### Shell Aliases

Add to your `.bashrc` or `.zshrc`:

```bash
alias askaws='~/path/to/venv/bin/python ~/path/to/cli/ask_aws.py'
```

Then use:
```bash
askaws "Lambda best practices"
askaws "boto3 S3" reference_documentation
```

### In Shell Scripts

```bash
#!/bin/bash

# Query AWS docs in a script
VENV_PYTHON="/path/to/venv/bin/python"
CLI_SCRIPT="/path/to/cli/ask_aws.py"

# Get Lambda best practices
$VENV_PYTHON $CLI_SCRIPT "Lambda best practices" general 3

# Get boto3 documentation
$VENV_PYTHON $CLI_SCRIPT "boto3 S3 upload" reference_documentation 5
```

### Parsing Output

The CLI outputs formatted text. To parse programmatically, consider using the Python API instead (see [API Reference](API_REFERENCE.md)).

### Piping Output

```bash
# Save to file
venv/bin/python cli/ask_aws.py "Lambda best practices" > lambda_docs.txt

# Search in output
venv/bin/python cli/ask_aws.py "S3 security" | grep -i "encryption"

# Count results
venv/bin/python cli/ask_aws.py "Lambda" | grep -c "^[0-9]\\."
```

## 🐛 Troubleshooting

### Command Not Found

**Problem:** `python: command not found`

**Solution:**
```bash
# Try python3
python3 cli/ask_aws.py "your question"

# Or use full path
/usr/bin/python3 cli/ask_aws.py "your question"
```

### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'mcp'`

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install mcp httpx

# Run again
python cli/ask_aws.py "your question"
```

### Invalid Topic

**Problem:** `❌ Invalid topic: xyz`

**Solution:**
Use one of the valid topics:
- `general`
- `reference_documentation`
- `troubleshooting`
- `cdk_docs`
- `cdk_constructs`
- `cloudformation`
- `current_awareness`
- `amplify_docs`

### No Results Found

**Problem:** Search returns no results

**Solutions:**
1. Try a different topic
2. Rephrase your question
3. Be more specific
4. Use service names explicitly

### Connection Error

**Problem:** Cannot connect to MCP server

**Solutions:**
1. Check internet connection
2. Verify endpoint is accessible:
   ```bash
   curl https://knowledge-mcp.global.api.aws
   ```
3. Try again later

## 📊 Output Format

The CLI outputs results in this format:

```
🔍 Searching AWS Knowledge Base...
   Question: Your question
   Topic: general
   Max Results: 5

================================================================================
📚 RESULTS
================================================================================

1. Document Title
   🔗 https://docs.aws.amazon.com/...
   📝 Context snippet from the document...

2. Another Document
   🔗 https://docs.aws.amazon.com/...
   📝 More context...

================================================================================
✅ Search completed!
================================================================================
```

## 🎓 Learning Path

### Beginners

Start with general queries:
```bash
venv/bin/python cli/ask_aws.py "What is Lambda"
venv/bin/python cli/ask_aws.py "S3 getting started"
venv/bin/python cli/ask_aws.py "DynamoDB basics"
```

### Intermediate

Explore specific topics:
```bash
venv/bin/python cli/ask_aws.py "Lambda best practices" general
venv/bin/python cli/ask_aws.py "boto3 S3 examples" reference_documentation
venv/bin/python cli/ask_aws.py "Lambda CDK Python" cdk_constructs
```

### Advanced

Deep dive into specific areas:
```bash
venv/bin/python cli/ask_aws.py "Lambda performance optimization" general
venv/bin/python cli/ask_aws.py "S3 encryption options" general
venv/bin/python cli/ask_aws.py "DynamoDB GSI design" general
```

## 🔗 Related Guides

- [Interactive Mode Guide](INTERACTIVE_GUIDE.md) - Chat-style interface
- [Web UI Guide](WEB_UI_GUIDE.md) - Web interface
- [API Reference](API_REFERENCE.md) - Use in Python code
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues

---

**Happy querying! 🚀**
