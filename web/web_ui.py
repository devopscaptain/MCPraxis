#!/usr/bin/env python3
"""
AWS Knowledge MCP Server - Web UI
Fancy web interface for querying AWS documentation
"""

from flask import Flask, render_template, request, jsonify
import asyncio
import json
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from datetime import timedelta

app = Flask(__name__)

class AWSKnowledgeAPI:
    def __init__(self):
        self.mcp_url = "https://knowledge-mcp.global.api.aws"
    
    async def search(self, question, topic="general", limit=5):
        """Search AWS documentation"""
        try:
            async with streamablehttp_client(
                self.mcp_url, 
                headers={}, 
                timeout=timedelta(seconds=60)
            ) as (read_stream, write_stream, _):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    
                    result = await session.call_tool(
                        "aws___search_documentation",
                        arguments={
                            "search_phrase": question,
                            "topics": [topic],
                            "limit": limit
                        }
                    )
                    
                    for content in result.content:
                        if hasattr(content, 'text'):
                            data = json.loads(content.text)
                            return data.get('content', {}).get('result', [])
                    
                    return []
        except Exception as e:
            return {"error": str(e)}
    
    async def list_regions(self):
        """List AWS regions"""
        try:
            async with streamablehttp_client(
                self.mcp_url, 
                headers={}, 
                timeout=timedelta(seconds=60)
            ) as (read_stream, write_stream, _):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    
                    result = await session.call_tool(
                        "aws___list_regions",
                        arguments={}
                    )
                    
                    for content in result.content:
                        if hasattr(content, 'text'):
                            data = json.loads(content.text)
                            return data.get('content', {}).get('result', [])
                    
                    return []
        except Exception as e:
            return {"error": str(e)}

api = AWSKnowledgeAPI()

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    """Search endpoint"""
    data = request.json
    question = data.get('question', '')
    topic = data.get('topic', 'general')
    limit = data.get('limit', 5)
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
    
    results = asyncio.run(api.search(question, topic, limit))
    return jsonify({"results": results})

@app.route('/api/regions', methods=['GET'])
def regions():
    """Get AWS regions"""
    results = asyncio.run(api.list_regions())
    return jsonify({"regions": results})

if __name__ == '__main__':
    print("\n🚀 Starting AWS Knowledge Web UI...")
    print("📱 Open your browser to: http://localhost:8080")
    print("Press Ctrl+C to stop\n")
    app.run(debug=True, host='0.0.0.0', port=8080)
