# AWS Knowledge Query - Web UI Guide

Beautiful web interface for querying AWS documentation through the MCP server.

## 🎨 Features

- **Modern UI** - Clean, responsive design with AWS branding
- **Real-time Search** - Instant results from AWS Knowledge MCP Server
- **Topic Filtering** - 8 specialized categories for better results
- **Quick Examples** - One-click example queries
- **AWS Regions** - View all AWS regions with one click
- **Mobile Friendly** - Works on all devices

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Make sure you're in the project directory
cd mcp-project

# Install Flask (if not already installed)
venv/bin/pip install flask mcp httpx
```

### 2. Start the Web Server

```bash
# Run the web UI
venv/bin/python web_ui.py
```

You should see:
```
🚀 Starting AWS Knowledge Web UI...
📱 Open your browser to: http://localhost:8080
Press Ctrl+C to stop
```

### 3. Open in Browser

Open your web browser and go to:
```
http://localhost:8080
```

## 📖 How to Use

### Search AWS Documentation

1. **Enter your question** in the search box
2. **Select a topic** (optional) - defaults to "General"
3. **Choose result limit** (3, 5, or 10)
4. **Click Search** or press Enter

### Quick Examples

Click any of the quick example buttons to try pre-configured queries:
- **Lambda basics** - How to create a Lambda function
- **S3 best practices** - S3 security and best practices
- **boto3 S3** - Python SDK documentation
- **Lambda errors** - Troubleshooting Lambda issues

### View AWS Regions

Click the **"Show AWS Regions"** button to see all available AWS regions with their names.

## 🎯 Available Topics

| Topic | Best For |
|-------|----------|
| **General** | Best practices, architecture, tutorials |
| **API/SDK Documentation** | boto3, AWS CLI, API references |
| **Troubleshooting** | Error messages, debugging |
| **CDK Concepts** | CDK getting started, concepts |
| **CDK Code Examples** | Working CDK code samples |
| **CloudFormation** | CloudFormation templates |
| **New Features** | Latest AWS announcements |
| **Amplify Framework** | Amplify web/mobile development |

## 🎨 UI Features

### Search Section
- Large search input with auto-focus
- Topic dropdown selector
- Result limit selector
- Quick example buttons

### Results Display
- Clean card-based layout
- Clickable documentation links
- Context snippets
- Smooth animations
- Result count badge

### Regions View
- Grid layout of all AWS regions
- Region IDs and full names
- Toggle show/hide

## 🔧 Customization

### Change Port

Edit `web_ui.py`:
```python
app.run(debug=True, host='0.0.0.0', port=9000)  # Change 8080 to 9000
```

### Modify Styling

Edit `static/css/style.css` to customize:
- Colors (see `:root` variables)
- Fonts
- Layout
- Animations

### Add More Examples

Edit `templates/index.html` and add more example buttons:
```html
<button class="example-btn" 
        data-query="Your query" 
        data-topic="topic_name">
    Button Text
</button>
```

## 📁 Project Structure

```
mcp-project/
├── web_ui.py              # Flask backend
├── templates/
│   └── index.html         # HTML template
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   └── js/
│       └── app.js         # Frontend JavaScript
└── venv/                  # Python environment
```

## 🌐 API Endpoints

The web UI exposes these endpoints:

### GET /
Returns the main HTML page

### POST /api/search
Search AWS documentation

**Request:**
```json
{
  "question": "How to create Lambda",
  "topic": "general",
  "limit": 5
}
```

**Response:**
```json
{
  "results": [
    {
      "title": "...",
      "url": "...",
      "context": "..."
    }
  ]
}
```

### GET /api/regions
Get all AWS regions

**Response:**
```json
{
  "regions": [
    {
      "region_id": "us-east-1",
      "region_long_name": "US East (N. Virginia)"
    }
  ]
}
```

## 🐛 Troubleshooting

### Port Already in Use

If port 8080 is already in use:
```bash
# Find process using port 8080
lsof -i :8080

# Kill the process or change port in web_ui.py
```

### Module Not Found

```bash
# Reinstall dependencies
venv/bin/pip install flask mcp httpx
```

### Connection Errors

- Check your internet connection
- Verify the MCP endpoint is accessible
- Check browser console for errors (F12)

## 💡 Tips

1. **Use specific queries** - "Lambda timeout error" > "Lambda error"
2. **Choose the right topic** - Better results with correct category
3. **Try quick examples** - Learn by example
4. **Open links in new tabs** - Results open in new tabs automatically

## 🚀 Production Deployment

For production use, consider:

1. **Use a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8080 web_ui:app
   ```

2. **Add authentication** if needed

3. **Use HTTPS** with a reverse proxy (nginx, Apache)

4. **Add rate limiting** to prevent abuse

5. **Enable caching** for frequently asked questions

## 📝 License

This web UI is part of the AWS Knowledge MCP Query Tools project.

---

**Enjoy the fancy UI! 🎉**
