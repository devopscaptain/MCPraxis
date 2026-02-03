# API Reference

Complete reference for using AWS Knowledge Query in your Python code.

## 🎯 Overview

You can integrate AWS Knowledge Query functionality into your own Python applications using the provided classes and functions.

## 📦 Installation

```bash
pip install mcp httpx
```

## 🚀 Quick Start

### Simple Query Function

```python
import asyncio
from cli.ask_aws import ask_aws

# Ask a question
asyncio.run(ask_aws("How to create Lambda function", "general", 5))
```

### Using the Assistant Class

```python
import asyncio
from cli.interactive_aws import AWSAssistant

async def main():
    assistant = AWSAssistant()
    await assistant.connect()
    
    results = await assistant.ask("Lambda best practices", "general", 5)
    
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
    
    await assistant.disconnect()

asyncio.run(main())
```

## 📚 API Reference

### AWSAssistant Class

The main class for interacting with the AWS Knowledge MCP Server.

#### Constructor

```python
from cli.interactive_aws import AWSAssistant

assistant = AWSAssistant()
```

**Parameters:** None

**Attributes:**
- `mcp_url` (str): The MCP server endpoint
- `session` (ClientSession): The MCP client session

#### Methods

##### connect()

Connect to the AWS Knowledge MCP Server.

```python
await assistant.connect()
```

**Returns:** None

**Raises:** Exception if connection fails

**Example:**
```python
assistant = AWSAssistant()
await assistant.connect()
```

##### disconnect()

Disconnect from the server and clean up resources.

```python
await assistant.disconnect()
```

**Returns:** None

**Example:**
```python
await assistant.disconnect()
```

##### ask(question, topic="general", limit=3)

Search AWS documentation.

```python
results = await assistant.ask(
    question="Lambda best practices",
    topic="general",
    limit=5
)
```

**Parameters:**
- `question` (str, required): Your question about AWS
- `topic` (str, optional): Topic category (default: "general")
- `limit` (int, optional): Number of results (default: 3, max: 10)

**Returns:** List of dictionaries with keys:
- `title` (str): Document title
- `url` (str): Documentation URL
- `context` (str): Context snippet

**Example:**
```python
results = await assistant.ask("boto3 S3 upload", "reference_documentation", 5)

for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Context: {result['context'][:200]}...")
```

##### list_regions()

Get all AWS regions.

```python
regions = await assistant.list_regions()
```

**Returns:** List of dictionaries with keys:
- `region_id` (str): Region identifier (e.g., "us-east-1")
- `region_long_name` (str): Full region name (e.g., "US East (N. Virginia)")

**Example:**
```python
regions = await assistant.list_regions()

for region in regions:
    print(f"{region['region_id']}: {region['region_long_name']}")
```

##### check_availability(service, resource_type="product")

Check service availability across regions.

```python
availability = await assistant.check_availability(
    service="AWS Lambda",
    resource_type="product"
)
```

**Parameters:**
- `service` (str, required): Service name
- `resource_type` (str, optional): Resource type (default: "product")

**Returns:** List of availability data

**Example:**
```python
availability = await assistant.check_availability("AWS Lambda")
print(f"Found {len(availability)} availability records")
```

### ask_aws Function

Simple function for one-off queries.

```python
from cli.ask_aws import ask_aws

await ask_aws(question, topic="general", limit=5)
```

**Parameters:**
- `question` (str, required): Your question
- `topic` (str, optional): Topic category (default: "general")
- `limit` (int, optional): Number of results (default: 5)

**Returns:** None (prints results to stdout)

**Example:**
```python
import asyncio
from cli.ask_aws import ask_aws

asyncio.run(ask_aws("Lambda timeout error", "troubleshooting", 3))
```

## 🎯 Complete Examples

### Example 1: Simple Search

```python
import asyncio
from cli.interactive_aws import AWSAssistant

async def search_aws_docs():
    assistant = AWSAssistant()
    
    try:
        await assistant.connect()
        
        results = await assistant.ask("Lambda best practices", "general", 5)
        
        print(f"Found {len(results)} results:\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Context: {result.get('context', 'N/A')[:150]}...\n")
    
    finally:
        await assistant.disconnect()

asyncio.run(search_aws_docs())
```

### Example 2: Multiple Queries

```python
import asyncio
from cli.interactive_aws import AWSAssistant

async def multiple_searches():
    assistant = AWSAssistant()
    await assistant.connect()
    
    try:
        # Search different topics
        queries = [
            ("Lambda best practices", "general"),
            ("boto3 S3 upload", "reference_documentation"),
            ("Lambda timeout error", "troubleshooting"),
        ]
        
        for question, topic in queries:
            print(f"\n{'='*60}")
            print(f"Query: {question} (Topic: {topic})")
            print('='*60)
            
            results = await assistant.ask(question, topic, 3)
            
            for result in results:
                print(f"- {result['title']}")
                print(f"  {result['url']}\n")
    
    finally:
        await assistant.disconnect()

asyncio.run(multiple_searches())
```

### Example 3: Region Information

```python
import asyncio
from cli.interactive_aws import AWSAssistant

async def get_regions():
    assistant = AWSAssistant()
    await assistant.connect()
    
    try:
        regions = await assistant.list_regions()
        
        print(f"Total AWS Regions: {len(regions)}\n")
        
        # Group by continent
        us_regions = [r for r in regions if r['region_id'].startswith('us-')]
        eu_regions = [r for r in regions if r['region_id'].startswith('eu-')]
        ap_regions = [r for r in regions if r['region_id'].startswith('ap-')]
        
        print("US Regions:")
        for region in us_regions:
            print(f"  {region['region_id']}: {region['region_long_name']}")
        
        print("\nEU Regions:")
        for region in eu_regions:
            print(f"  {region['region_id']}: {region['region_long_name']}")
        
        print("\nAP Regions:")
        for region in ap_regions:
            print(f"  {region['region_id']}: {region['region_long_name']}")
    
    finally:
        await assistant.disconnect()

asyncio.run(get_regions())
```

### Example 4: Error Handling

```python
import asyncio
from cli.interactive_aws import AWSAssistant

async def search_with_error_handling():
    assistant = AWSAssistant()
    
    try:
        await assistant.connect()
        print("✅ Connected to AWS Knowledge MCP Server")
        
        results = await assistant.ask("Lambda best practices", "general", 5)
        
        if not results:
            print("⚠️ No results found")
        else:
            print(f"✅ Found {len(results)} results")
            for result in results:
                print(f"- {result['title']}")
    
    except ConnectionError as e:
        print(f"❌ Connection error: {e}")
    except TimeoutError as e:
        print(f"❌ Timeout error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    finally:
        try:
            await assistant.disconnect()
            print("✅ Disconnected")
        except:
            pass

asyncio.run(search_with_error_handling())
```

### Example 5: Custom Application

```python
import asyncio
from cli.interactive_aws import AWSAssistant

class AWSDocsHelper:
    def __init__(self):
        self.assistant = AWSAssistant()
        self.connected = False
    
    async def __aenter__(self):
        await self.assistant.connect()
        self.connected = True
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.connected:
            await self.assistant.disconnect()
    
    async def search(self, question, topic="general", limit=5):
        """Search AWS documentation"""
        return await self.assistant.ask(question, topic, limit)
    
    async def get_regions(self):
        """Get all AWS regions"""
        return await self.assistant.list_regions()
    
    async def troubleshoot(self, error_message, limit=3):
        """Search troubleshooting docs"""
        return await self.assistant.ask(error_message, "troubleshooting", limit)
    
    async def get_api_docs(self, query, limit=5):
        """Search API documentation"""
        return await self.assistant.ask(query, "reference_documentation", limit)
    
    async def get_cdk_examples(self, query, limit=5):
        """Search CDK examples"""
        return await self.assistant.ask(query, "cdk_constructs", limit)

# Usage
async def main():
    async with AWSDocsHelper() as helper:
        # Search general docs
        results = await helper.search("Lambda best practices")
        print(f"General: {len(results)} results")
        
        # Troubleshoot an error
        results = await helper.troubleshoot("Lambda timeout error")
        print(f"Troubleshooting: {len(results)} results")
        
        # Get API docs
        results = await helper.get_api_docs("boto3 S3 upload")
        print(f"API docs: {len(results)} results")
        
        # Get CDK examples
        results = await helper.get_cdk_examples("Lambda CDK Python")
        print(f"CDK examples: {len(results)} results")
        
        # Get regions
        regions = await helper.get_regions()
        print(f"Regions: {len(regions)} total")

asyncio.run(main())
```

### Example 6: Flask Integration

```python
from flask import Flask, request, jsonify
import asyncio
from cli.interactive_aws import AWSAssistant

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    question = data.get('question')
    topic = data.get('topic', 'general')
    limit = data.get('limit', 5)
    
    if not question:
        return jsonify({"error": "Question required"}), 400
    
    # Run async function in sync context
    results = asyncio.run(search_aws(question, topic, limit))
    return jsonify({"results": results})

async def search_aws(question, topic, limit):
    assistant = AWSAssistant()
    await assistant.connect()
    try:
        return await assistant.ask(question, topic, limit)
    finally:
        await assistant.disconnect()

if __name__ == '__main__':
    app.run(port=5000)
```

## 📖 Topics Reference

Valid topic values:

| Topic | Description |
|-------|-------------|
| `general` | Best practices, architecture, tutorials |
| `reference_documentation` | API/SDK/CLI documentation |
| `troubleshooting` | Error messages and debugging |
| `cdk_docs` | CDK concepts and API reference |
| `cdk_constructs` | CDK code examples |
| `cloudformation` | CloudFormation templates |
| `current_awareness` | New features and announcements |
| `amplify_docs` | Amplify framework documentation |

## 🔧 Configuration

### MCP Server Endpoint

The default endpoint is:
```python
mcp_url = "https://knowledge-mcp.global.api.aws"
```

To use a different endpoint:
```python
assistant = AWSAssistant()
assistant.mcp_url = "https://your-custom-endpoint.com"
await assistant.connect()
```

### Timeout Configuration

The default timeout is 60 seconds. To change it, modify the `streamablehttp_client` call in the source code.

## 🐛 Error Handling

### Common Exceptions

```python
try:
    await assistant.connect()
    results = await assistant.ask("Lambda", "general", 5)
except ConnectionError:
    print("Cannot connect to MCP server")
except TimeoutError:
    print("Request timed out")
except json.JSONDecodeError:
    print("Invalid response from server")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Best Practices

1. **Always use try/finally** to ensure disconnection:
```python
try:
    await assistant.connect()
    # Your code
finally:
    await assistant.disconnect()
```

2. **Use context managers** for automatic cleanup:
```python
async with AWSDocsHelper() as helper:
    results = await helper.search("Lambda")
```

3. **Handle empty results**:
```python
results = await assistant.ask("query", "general", 5)
if not results:
    print("No results found")
```

## 🔗 Related Guides

- [CLI Guide](CLI_GUIDE.md) - Command-line usage
- [Interactive Guide](INTERACTIVE_GUIDE.md) - Interactive mode
- [Web UI Guide](WEB_UI_GUIDE.md) - Web interface
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues

---

**Happy coding! 🚀**
