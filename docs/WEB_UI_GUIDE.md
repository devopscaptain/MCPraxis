# Web UI Guide

Complete guide for the AWS Knowledge Query web interface.

## 🎨 Overview

The web UI provides a beautiful, modern interface for querying AWS documentation. It features:

- **Real-time search** with instant results
- **Topic filtering** across 8 AWS documentation categories
- **Quick examples** for common queries
- **AWS regions viewer** to see all available regions
- **Responsive design** that works on all devices
- **Modern UI** with AWS branding and smooth animations

## 🚀 Getting Started

### Starting the Web Server

**Option 1: Using Python directly**
```bash
cd web
../venv/bin/python web_ui.py
```

**Option 2: Using the startup script**
```bash
cd web
./start_web_ui.sh
```

The server will start on `http://localhost:8080`

You should see:
```
🚀 Starting AWS Knowledge Web UI...
📱 Open your browser to: http://localhost:8080
Press Ctrl+C to stop
```

### Accessing the Interface

Open your web browser and navigate to:
```
http://localhost:8080
```

## 📖 Using the Web UI

### Search AWS Documentation

1. **Enter your question** in the large search box
2. **Select a topic** from the dropdown (optional, defaults to "General")
3. **Choose result limit** (3, 5, or 10 results)
4. **Click "Search"** or press Enter

The results will appear below with:
- Document title
- Direct link to AWS documentation
- Context snippet from the document

### Topic Categories

Choose the right topic for better results:

| Topic | Best For |
|-------|----------|
| **General** | Best practices, architecture patterns, tutorials |
| **API/SDK Documentation** | boto3, AWS CLI, API references |
| **Troubleshooting** | Error messages, debugging guides |
| **CDK Concepts** | AWS CDK getting started, concepts |
| **CDK Code Examples** | Working CDK code samples |
| **CloudFormation** | CloudFormation templates and examples |
| **New Features** | Latest AWS announcements and updates |
| **Amplify Framework** | Amplify web/mobile development |

### Quick Examples

Click any of the pre-configured example buttons to try common queries:

- **Lambda basics** - "How to create a Lambda function"
- **S3 best practices** - "S3 security and best practices"
- **boto3 S3** - "boto3 S3 upload" (API Documentation topic)
- **Lambda errors** - "Lambda timeout error" (Troubleshooting topic)

These examples automatically set the appropriate topic and execute the search.

### View AWS Regions

Click the **"Show AWS Regions"** button to see all available AWS regions with their:
- Region ID (e.g., `us-east-1`)
- Full region name (e.g., "US East (N. Virginia)")

Click again to hide the regions list.

## 🎯 Search Tips

### Getting Better Results

1. **Be specific** - "Lambda timeout error" > "Lambda error"
2. **Include service names** - "boto3 S3 upload" > "upload file"
3. **Use exact error messages** - Copy/paste error text for troubleshooting
4. **Choose the right topic** - API docs for code, troubleshooting for errors
5. **Try different phrasings** - If no results, rephrase your question

### Example Queries by Topic

**General**
```
Lambda best practices
S3 security patterns
Serverless architecture
DynamoDB vs RDS
```

**API/SDK Documentation**
```
boto3 S3 upload_file
aws lambda invoke CLI
Lambda InvokeFunction API
DynamoDB PutItem boto3
```

**Troubleshooting**
```
Lambda timeout error
S3 access denied
DynamoDB throttling
API Gateway 403 error
```

**CDK Code Examples**
```
Lambda function CDK Python
API Gateway Lambda CDK
DynamoDB table CDK TypeScript
S3 bucket CDK
```

**CloudFormation**
```
Lambda CloudFormation template
DynamoDB CloudFormation
SAM template API Gateway
EventBridge rule CloudFormation
```

**New Features**
```
Lambda new features 2024
what's new in S3
ECS latest updates
RDS new capabilities
```

## 🎨 UI Features

### Search Section
- **Large search input** with auto-focus on page load
- **Topic dropdown** with 8 categories
- **Result limit selector** (3, 5, or 10)
- **Quick example buttons** for common queries

### Results Display
- **Card-based layout** for easy reading
- **Clickable links** that open in new tabs
- **Context snippets** showing relevant content
- **Result count badge** showing number of results
- **Smooth animations** when results appear

### Regions Viewer
- **Grid layout** of all AWS regions
- **Toggle show/hide** functionality
- **Region IDs and names** clearly displayed

### Responsive Design
- Works on desktop, tablet, and mobile
- Adapts layout for smaller screens
- Touch-friendly buttons and inputs

## 🔧 Configuration

### Change Port

Edit `web_ui.py` and modify the last line:

```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change 8080 to your port
```

### Customize Styling

Edit `static/css/style.css` to customize:

**Colors** (in `:root` section):
```css
:root {
    --primary-color: #FF9900;      /* AWS orange */
    --secondary-color: #232F3E;    /* AWS dark blue */
    --accent-color: #146EB4;       /* AWS light blue */
    /* ... more colors ... */
}
```

**Fonts:**
```css
body {
    font-family: 'Your Font', Arial, sans-serif;
}
```

### Add More Examples

Edit `templates/index.html` and add buttons in the quick examples section:

```html
<button class="example-btn" 
        data-query="Your query here" 
        data-topic="topic_name">
    Button Text
</button>
```

## 🌐 API Endpoints

The web UI exposes these REST endpoints:

### GET /
Returns the main HTML page.

### POST /api/search
Search AWS documentation.

**Request:**
```json
{
  "question": "How to create Lambda function",
  "topic": "general",
  "limit": 5
}
```

**Response:**
```json
{
  "results": [
    {
      "title": "Creating Lambda functions",
      "url": "https://docs.aws.amazon.com/...",
      "context": "Lambda functions are..."
    }
  ]
}
```

**Error Response:**
```json
{
  "error": "Question is required"
}
```

### GET /api/regions
Get all AWS regions.

**Response:**
```json
{
  "regions": [
    {
      "region_id": "us-east-1",
      "region_long_name": "US East (N. Virginia)"
    },
    {
      "region_id": "us-west-2",
      "region_long_name": "US West (Oregon)"
    }
  ]
}
```

## 🐛 Troubleshooting

### Port Already in Use

**Problem:** Error: "Address already in use"

**Solution:**
```bash
# Find process using port 8080
lsof -i :8080

# Kill the process
kill -9 <PID>

# Or change the port in web_ui.py
```

### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install flask mcp httpx
```

### Connection Errors

**Problem:** Cannot connect to MCP server

**Solutions:**
1. Check your internet connection
2. Verify the endpoint is accessible:
   ```bash
   curl https://knowledge-mcp.global.api.aws
   ```
3. Check browser console for errors (F12)
4. Try again later (service may be temporarily unavailable)

### No Results Found

**Problem:** Search returns no results

**Solutions:**
1. Try a different topic category
2. Rephrase your question to be more specific
3. Use service names explicitly (e.g., "Lambda" not "function")
4. Try the `general` topic for broad questions

### Slow Response

**Problem:** Search takes a long time

**Reasons:**
- Network latency
- MCP server load
- Complex queries

**Solutions:**
- Reduce result limit
- Be more specific with queries
- Check your internet connection

## 💡 Tips & Best Practices

### For Best Results

1. **Start with quick examples** to understand the format
2. **Use specific service names** in your queries
3. **Choose the appropriate topic** for your question type
4. **Open links in new tabs** (they do this automatically)
5. **Try different topics** if you don't get good results

### Keyboard Shortcuts

- **Enter** in search box - Execute search
- **Tab** - Navigate between fields
- **Esc** - Clear search (when focused)

### Mobile Usage

The UI is fully responsive and works great on mobile:
- Touch-friendly buttons
- Readable text sizes
- Scrollable results
- Collapsible sections

## 🚀 Production Deployment

For production use, consider:

### 1. Use a Production WSGI Server

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 web_ui:app
```

### 2. Add HTTPS

Use a reverse proxy like nginx:

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 3. Add Rate Limiting

Install Flask-Limiter:
```bash
pip install Flask-Limiter
```

Add to `web_ui.py`:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)
```

### 4. Enable Caching

Consider caching frequent queries to reduce load.

### 5. Disable Debug Mode

Change in `web_ui.py`:
```python
app.run(debug=False, host='0.0.0.0', port=8080)
```

## 📝 Advanced Usage

### Using the API Programmatically

You can call the web UI's API from other applications:

```python
import requests

# Search
response = requests.post('http://localhost:8080/api/search', json={
    'question': 'Lambda best practices',
    'topic': 'general',
    'limit': 5
})
results = response.json()['results']

# Get regions
response = requests.get('http://localhost:8080/api/regions')
regions = response.json()['regions']
```

### Embedding in Other Applications

You can embed the search functionality in your own web apps by calling the API endpoints.

---

**Enjoy the web UI! 🎉**
