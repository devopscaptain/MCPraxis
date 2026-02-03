# Troubleshooting Guide

Solutions to common issues with AWS Knowledge Query Tool.

## 🔍 Quick Diagnosis

### Check Your Setup

```bash
# 1. Check Python version (need 3.10+)
python3 --version

# 2. Check virtual environment
ls -la venv/

# 3. Check dependencies
venv/bin/pip list | grep -E "mcp|httpx|flask"

# 4. Test internet connection
curl https://knowledge-mcp.global.api.aws

# 5. Test CLI
venv/bin/python cli/ask_aws.py "test query"
```

## 🐛 Common Issues

### Installation Issues

#### Problem: Virtual Environment Not Found

**Error:**
```
bash: venv/bin/python: No such file or directory
```

**Solution:**
```bash
# Create virtual environment
python3 -m venv venv

# Verify it was created
ls -la venv/

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

#### Problem: Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'mcp'
```

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install mcp httpx flask

# Verify installation
pip list | grep -E "mcp|httpx|flask"

# Try again
python cli/ask_aws.py "test query"
```

#### Problem: Python Version Too Old

**Error:**
```
SyntaxError: invalid syntax
```

**Solution:**
```bash
# Check Python version
python3 --version

# Need Python 3.10 or higher
# Install newer Python version:
# - macOS: brew install python@3.11
# - Ubuntu: sudo apt install python3.11
# - Windows: Download from python.org

# Create venv with specific version
python3.11 -m venv venv
```

### Connection Issues

#### Problem: Cannot Connect to MCP Server

**Error:**
```
❌ Error: Cannot connect to MCP server
```

**Solutions:**

1. **Check internet connection:**
```bash
ping google.com
```

2. **Test MCP endpoint:**
```bash
curl https://knowledge-mcp.global.api.aws
```

3. **Check firewall/proxy:**
```bash
# If behind corporate firewall, may need proxy settings
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
```

4. **Try again later:**
The service may be temporarily unavailable.

#### Problem: Timeout Error

**Error:**
```
TimeoutError: Request timed out
```

**Solutions:**

1. **Check network speed:**
```bash
# Test download speed
curl -o /dev/null https://speed.cloudflare.com/__down?bytes=10000000
```

2. **Reduce result limit:**
```bash
# Instead of 10 results, try 3
venv/bin/python cli/ask_aws.py "query" general 3
```

3. **Try simpler query:**
```bash
# Simpler queries may be faster
venv/bin/python cli/ask_aws.py "Lambda" general 3
```

### Query Issues

#### Problem: No Results Found

**Error:**
```
❌ No results found. Try a different query or topic.
```

**Solutions:**

1. **Try different topic:**
```bash
# If general doesn't work, try reference_documentation
venv/bin/python cli/ask_aws.py "boto3 S3" reference_documentation
```

2. **Be more specific:**
```bash
# Instead of "error"
venv/bin/python cli/ask_aws.py "Lambda timeout error" troubleshooting
```

3. **Use service names:**
```bash
# Instead of "upload file"
venv/bin/python cli/ask_aws.py "S3 upload file" general
```

4. **Try different phrasing:**
```bash
# Try variations
venv/bin/python cli/ask_aws.py "Lambda function creation"
venv/bin/python cli/ask_aws.py "How to create Lambda"
venv/bin/python cli/ask_aws.py "Lambda getting started"
```

#### Problem: Invalid Topic

**Error:**
```
❌ Invalid topic: xyz
```

**Solution:**

Use one of these valid topics:
- `general`
- `reference_documentation`
- `troubleshooting`
- `cdk_docs`
- `cdk_constructs`
- `cloudformation`
- `current_awareness`
- `amplify_docs`

```bash
# Correct usage
venv/bin/python cli/ask_aws.py "Lambda" general
```

### Web UI Issues

#### Problem: Port Already in Use

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solutions:**

1. **Find process using port:**
```bash
# macOS/Linux
lsof -i :8080

# Windows
netstat -ano | findstr :8080
```

2. **Kill the process:**
```bash
# macOS/Linux
kill -9 <PID>

# Windows
taskkill /PID <PID> /F
```

3. **Use different port:**

Edit `web/web_ui.py`:
```python
app.run(debug=True, host='0.0.0.0', port=9000)  # Change to 9000
```

#### Problem: Web UI Not Loading

**Error:**
Browser shows "Cannot connect" or "Connection refused"

**Solutions:**

1. **Check if server is running:**
```bash
# Should see output like:
# * Running on http://0.0.0.0:8080
```

2. **Check correct URL:**
```
http://localhost:8080  ✅
http://127.0.0.1:8080  ✅
http://0.0.0.0:8080    ❌ (won't work in browser)
```

3. **Check firewall:**
```bash
# macOS
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /path/to/python

# Linux
sudo ufw allow 8080
```

4. **Try different browser:**
Sometimes browser cache causes issues. Try:
- Chrome/Chromium
- Firefox
- Safari
- Incognito/Private mode

#### Problem: Static Files Not Loading

**Error:**
Web UI loads but no styling/JavaScript

**Solutions:**

1. **Check file structure:**
```bash
ls -la web/static/css/
ls -la web/static/js/
ls -la web/templates/
```

2. **Verify Flask is finding files:**
```bash
# Should see these files:
web/
├── static/
│   ├── css/style.css
│   └── js/app.js
└── templates/
    └── index.html
```

3. **Clear browser cache:**
- Chrome: Ctrl+Shift+Delete
- Firefox: Ctrl+Shift+Delete
- Safari: Cmd+Option+E

#### Problem: API Errors in Web UI

**Error:**
"Error: [error message]" in web UI

**Solutions:**

1. **Check browser console:**
- Press F12
- Go to Console tab
- Look for error messages

2. **Check network tab:**
- Press F12
- Go to Network tab
- Look for failed requests

3. **Check server logs:**
Look at terminal where web server is running for error messages.

### Interactive Mode Issues

#### Problem: Cannot Exit Interactive Mode

**Error:**
Stuck in interactive mode

**Solutions:**

1. **Use quit command:**
```
💬 You: quit
```

2. **Use exit command:**
```
💬 You: exit
```

3. **Use Ctrl+C:**
Press `Ctrl+C` on keyboard

4. **Use Ctrl+D:**
Press `Ctrl+D` on keyboard (EOF)

5. **Force kill:**
```bash
# In another terminal
ps aux | grep interactive_aws.py
kill -9 <PID>
```

#### Problem: Command Not Recognized

**Error:**
Command doesn't work in interactive mode

**Solution:**

Valid commands:
- `<question>` - Just type your question
- `ask <question>` - Explicitly ask
- `topic <name>` - Change topic
- `topics` - List topics
- `regions` - List regions
- `available <service>` - Check availability
- `help` - Show help
- `quit` / `exit` - Exit

```
💬 You: help
```

### Script/Automation Issues

#### Problem: Script Hangs

**Error:**
Script runs but never completes

**Solutions:**

1. **Add timeout:**
```python
import asyncio

# Add timeout to async operations
try:
    await asyncio.wait_for(assistant.ask("query"), timeout=30)
except asyncio.TimeoutError:
    print("Query timed out")
```

2. **Check for infinite loops:**
Review your code for loops that might not exit.

3. **Add debug output:**
```python
print("Starting query...")
results = await assistant.ask("query")
print(f"Got {len(results)} results")
```

#### Problem: Import Errors in Scripts

**Error:**
```
ModuleNotFoundError: No module named 'cli'
```

**Solution:**

1. **Use correct import path:**
```python
# If running from project root
from cli.interactive_aws import AWSAssistant

# If running from cli directory
from interactive_aws import AWSAssistant
```

2. **Add to Python path:**
```python
import sys
sys.path.append('/path/to/project')
from cli.interactive_aws import AWSAssistant
```

3. **Use absolute imports:**
```python
import os
import sys

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from cli.interactive_aws import AWSAssistant
```

## 🔧 Advanced Troubleshooting

### Enable Debug Logging

Add to your script:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

### Check MCP Communication

```python
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
from datetime import timedelta

async def test_mcp():
    mcp_url = "https://knowledge-mcp.global.api.aws"
    
    try:
        print("Connecting...")
        async with streamablehttp_client(
            mcp_url, 
            headers={}, 
            timeout=timedelta(seconds=60)
        ) as (read_stream, write_stream, _):
            print("Connected!")
            
            async with ClientSession(read_stream, write_stream) as session:
                print("Initializing session...")
                await session.initialize()
                print("Session initialized!")
                
                print("Calling tool...")
                result = await session.call_tool(
                    "aws___search_documentation",
                    arguments={
                        "search_phrase": "Lambda",
                        "topics": ["general"],
                        "limit": 1
                    }
                )
                print(f"Got result: {result}")
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

asyncio.run(test_mcp())
```

### Verify Dependencies

```bash
# Check installed versions
venv/bin/pip list

# Should see:
# mcp              (version)
# httpx            (version)
# flask            (version)

# If versions are old, upgrade:
venv/bin/pip install --upgrade mcp httpx flask
```

### Test Network Connectivity

```bash
# Test DNS resolution
nslookup knowledge-mcp.global.api.aws

# Test HTTPS connection
openssl s_client -connect knowledge-mcp.global.api.aws:443

# Test with curl
curl -v https://knowledge-mcp.global.api.aws
```

## 📞 Getting Help

If you're still stuck:

1. **Check error messages carefully** - They often contain the solution
2. **Search for the error** - Google the exact error message
3. **Check AWS MCP documentation** - https://awslabs.github.io/mcp/
4. **Review the code** - Look at the source files for clues
5. **Try a minimal example** - Simplify your code to isolate the issue

## 🔗 Related Guides

- [CLI Guide](CLI_GUIDE.md) - Command-line usage
- [Interactive Guide](INTERACTIVE_GUIDE.md) - Interactive mode
- [Web UI Guide](WEB_UI_GUIDE.md) - Web interface
- [API Reference](API_REFERENCE.md) - Python API

---

**Still having issues? Double-check the basics: Python version, dependencies, internet connection.** 🔍
