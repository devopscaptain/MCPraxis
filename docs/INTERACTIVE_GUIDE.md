# Interactive Mode Guide

Complete guide for using the AWS Knowledge Query interactive chat interface.

## 🎯 Overview

The interactive mode (`interactive_aws.py`) provides a chat-style interface for exploring AWS documentation. Perfect for:

- Learning and exploration
- Trying different queries quickly
- Switching between topics easily
- Viewing AWS regions and availability

## 🚀 Starting Interactive Mode

```bash
venv/bin/python cli/interactive_aws.py
```

You'll see:
```
🔗 Connecting to AWS Knowledge MCP Server...
✅ Connected!

================================================================================
🤖 AWS Knowledge Assistant - Interactive Mode
================================================================================

Commands:
  ask <question>              - Ask about AWS services
  topic <name>                - Change topic (current: general)
  regions                     - List all AWS regions
  available <service>         - Check service availability
  topics                      - Show available topics
  help                        - Show this help
  quit / exit                 - Exit the assistant

================================================================================

💬 You: 
```

## 📖 Commands

### Asking Questions

You can ask questions in two ways:

**1. Direct (no command needed):**
```
💬 You: How to create a Lambda function
```

**2. Using the `ask` command:**
```
💬 You: ask Lambda best practices
```

Both work the same way. The assistant will search using the current topic.

### Changing Topics

```
💬 You: topic reference_documentation
✅ Topic changed to: reference_documentation

💬 You: boto3 S3 upload
```

To see current topic:
```
💬 You: topic
📌 Current topic: general
```

### Listing Topics

```
💬 You: topics

📚 Available Topics:
  • general                  - Best practices, architecture
  • reference_documentation  - API/SDK/CLI docs
  • troubleshooting         - Error messages, debugging
  • cdk_docs                - CDK concepts
  • cdk_constructs          - CDK code examples
  • cloudformation          - CloudFormation templates
  • current_awareness       - New features
  • amplify_docs            - Amplify framework
```

### Viewing AWS Regions

```
💬 You: regions

🌍 Fetching AWS regions...

📍 AWS Regions:
   • us-east-1              - US East (N. Virginia)
   • us-east-2              - US East (Ohio)
   • us-west-1              - US West (N. California)
   • us-west-2              - US West (Oregon)
   • eu-west-1              - Europe (Ireland)
   • eu-central-1           - Europe (Frankfurt)
   • ap-southeast-1         - Asia Pacific (Singapore)
   • ap-northeast-1         - Asia Pacific (Tokyo)
   • ap-south-1             - Asia Pacific (Mumbai)
   • sa-east-1              - South America (São Paulo)
   ... and 23 more regions
```

### Checking Service Availability

```
💬 You: available AWS Lambda

🔍 Checking availability for: AWS Lambda
✅ Found availability data:
   [availability information]
```

### Getting Help

```
💬 You: help

Commands:
  ask <question>              - Ask about AWS services
  topic <name>                - Change topic
  regions                     - List all AWS regions
  available <service>         - Check service availability
  topics                      - Show available topics
  quit / exit                 - Exit
```

### Exiting

```
💬 You: quit
👋 Goodbye!
```

Or use: `exit`, `q`, or press `Ctrl+C`

## 💡 Example Sessions

### Session 1: Learning Lambda

```
💬 You: What is Lambda

🔍 Searching for: What is Lambda
   Topic: general

================================================================================
📚 RESULTS
================================================================================

1. AWS Lambda - Overview
   🔗 https://docs.aws.amazon.com/lambda/...
   📝 AWS Lambda is a serverless compute service...

2. Getting Started with Lambda
   🔗 https://docs.aws.amazon.com/lambda/...
   📝 Create your first Lambda function...

================================================================================

💬 You: Lambda best practices

🔍 Searching for: Lambda best practices
   Topic: general

[Results displayed...]

💬 You: topic reference_documentation
✅ Topic changed to: reference_documentation

💬 You: boto3 Lambda invoke

🔍 Searching for: boto3 Lambda invoke
   Topic: reference_documentation

[Results displayed...]

💬 You: quit
👋 Goodbye!
```

### Session 2: Troubleshooting

```
💬 You: topic troubleshooting
✅ Topic changed to: troubleshooting

💬 You: Lambda timeout error

🔍 Searching for: Lambda timeout error
   Topic: troubleshooting

================================================================================
📚 RESULTS
================================================================================

1. Troubleshooting Lambda Timeouts
   🔗 https://docs.aws.amazon.com/lambda/...
   📝 Lambda functions have a maximum execution time...

[More results...]

💬 You: S3 access denied

🔍 Searching for: S3 access denied
   Topic: troubleshooting

[Results displayed...]
```

### Session 3: CDK Development

```
💬 You: topic cdk_constructs
✅ Topic changed to: cdk_constructs

💬 You: Lambda function CDK Python

🔍 Searching for: Lambda function CDK Python
   Topic: cdk_constructs

================================================================================
📚 RESULTS
================================================================================

1. Lambda Function Construct - Python
   🔗 https://docs.aws.amazon.com/cdk/...
   📝 from aws_cdk import aws_lambda as lambda_...

[Code examples displayed...]

💬 You: API Gateway Lambda CDK

[Results displayed...]

💬 You: regions

🌍 Fetching AWS regions...
[Regions displayed...]
```

## 🎯 Workflow Tips

### Exploring a New Service

1. Start with general topic
2. Ask "What is [service]"
3. Ask about best practices
4. Switch to reference_documentation for API details
5. Switch to cdk_constructs for code examples

Example:
```
💬 You: What is DynamoDB
💬 You: DynamoDB best practices
💬 You: topic reference_documentation
💬 You: boto3 DynamoDB PutItem
💬 You: topic cdk_constructs
💬 You: DynamoDB table CDK Python
```

### Debugging an Issue

1. Switch to troubleshooting topic
2. Paste the error message
3. Ask follow-up questions
4. Switch to reference_documentation for API details

Example:
```
💬 You: topic troubleshooting
💬 You: Lambda timeout error
💬 You: How to increase Lambda timeout
💬 You: topic reference_documentation
💬 You: Lambda timeout configuration
```

### Learning CDK

1. Start with cdk_docs for concepts
2. Switch to cdk_constructs for examples
3. Ask about specific constructs

Example:
```
💬 You: topic cdk_docs
💬 You: CDK getting started
💬 You: CDK stack construct
💬 You: topic cdk_constructs
💬 You: Lambda function CDK Python
💬 You: S3 bucket CDK TypeScript
```

## 🔧 Advanced Features

### Quick Topic Switching

You can switch topics and ask in one session:

```
💬 You: topic troubleshooting
💬 You: Lambda timeout
💬 You: topic reference_documentation
💬 You: boto3 Lambda configuration
💬 You: topic cdk_constructs
💬 You: Lambda CDK example
```

### Combining Commands

While you can't combine commands in one line, you can quickly execute them in sequence:

```
💬 You: topics
💬 You: topic cdk_constructs
💬 You: Lambda CDK Python
```

### Using with Shell History

Use your shell's history (↑ arrow) to repeat or modify previous queries:

```
💬 You: Lambda best practices
[Results...]

💬 You: ↑ (edit to) S3 best practices
[Results...]
```

## 🐛 Troubleshooting

### Connection Issues

**Problem:** Cannot connect to MCP server

**Solution:**
- Check internet connection
- Verify endpoint accessibility
- Try again later

### No Results

**Problem:** Search returns no results

**Solutions:**
- Try a different topic
- Rephrase your question
- Be more specific
- Use service names explicitly

### Keyboard Interrupt

**Problem:** Accidentally pressed Ctrl+C

**Solution:**
The assistant will exit gracefully. Just restart:
```bash
venv/bin/python cli/interactive_aws.py
```

### Command Not Recognized

**Problem:** Command not working

**Solution:**
Check available commands with:
```
💬 You: help
```

Valid commands:
- `ask <question>` (or just type the question)
- `topic <name>`
- `topics`
- `regions`
- `available <service>`
- `help`
- `quit` / `exit`

## 💡 Tips & Best Practices

### For Best Results

1. **Start broad, then narrow** - Begin with general questions, then get specific
2. **Use the right topic** - Switch topics based on what you need
3. **Be specific** - Include service names and specific terms
4. **Try different phrasings** - If no results, rephrase your question
5. **Use regions command** - Check which regions support your service

### Keyboard Shortcuts

- **↑/↓ arrows** - Navigate command history
- **Ctrl+C** - Exit (gracefully)
- **Ctrl+D** - Exit (EOF)
- **Tab** - (depends on your shell's autocomplete)

### Efficient Exploration

1. Use `topics` to see all categories
2. Switch topics frequently as you explore
3. Use `regions` to understand AWS global infrastructure
4. Keep questions concise but specific

## 📊 Output Format

Results are displayed in this format:

```
🔍 Searching for: Your question
   Topic: current_topic

================================================================================
📚 RESULTS
================================================================================

1. Document Title
   🔗 https://docs.aws.amazon.com/...
   📝 Context snippet (first 250 characters)...

2. Another Document
   🔗 https://docs.aws.amazon.com/...
   📝 More context...

3. Third Document
   🔗 https://docs.aws.amazon.com/...
   📝 Additional context...

================================================================================
```

## 🎓 Learning Paths

### Beginner Path

```
💬 You: What is AWS Lambda
💬 You: Lambda getting started
💬 You: How to create Lambda function
💬 You: Lambda pricing
```

### Intermediate Path

```
💬 You: Lambda best practices
💬 You: topic reference_documentation
💬 You: boto3 Lambda invoke
💬 You: topic cdk_constructs
💬 You: Lambda CDK Python
```

### Advanced Path

```
💬 You: Lambda performance optimization
💬 You: Lambda cold start reduction
💬 You: Lambda VPC configuration
💬 You: Lambda layers best practices
```

## 🔗 Related Guides

- [CLI Guide](CLI_GUIDE.md) - Command-line tool
- [Web UI Guide](WEB_UI_GUIDE.md) - Web interface
- [API Reference](API_REFERENCE.md) - Use in Python code
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues

---

**Happy exploring! 🚀**
