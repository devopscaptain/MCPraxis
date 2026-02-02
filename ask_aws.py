#!/usr/bin/env python3
"""
Interactive AWS Knowledge Query Tool
Ask questions about AWS services and get answers from official documentation
"""

import asyncio
import sys
import json
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from datetime import timedelta


async def ask_aws(question, topic="general", limit=5):
    """
    Ask a question about AWS services
    
    Args:
        question: Your question about AWS
        topic: Topic category (default: "general")
        limit: Number of results (default: 5)
    """
    mcp_url = "https://knowledge-mcp.global.api.aws"
    
    print(f"\n🔍 Searching AWS Knowledge Base...")
    print(f"   Question: {question}")
    print(f"   Topic: {topic}")
    print(f"   Max Results: {limit}\n")
    
    try:
        async with streamablehttp_client(
            mcp_url, 
            headers={}, 
            timeout=timedelta(seconds=60)
        ) as (read_stream, write_stream, _):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                
                # Search documentation
                result = await session.call_tool(
                    "aws___search_documentation",
                    arguments={
                        "search_phrase": question,
                        "topics": [topic] if isinstance(topic, str) else topic,
                        "limit": limit
                    }
                )
                
                # Parse and display results
                print("=" * 80)
                print("📚 RESULTS")
                print("=" * 80)
                
                for content in result.content:
                    if hasattr(content, 'text'):
                        data = json.loads(content.text)
                        results = data.get('content', {}).get('result', [])
                        
                        if not results:
                            print("\n❌ No results found. Try a different query or topic.")
                            return
                        
                        for i, item in enumerate(results, 1):
                            print(f"\n{i}. {item['title']}")
                            print(f"   🔗 {item['url']}")
                            if item.get('context'):
                                context = item['context'][:300]
                                print(f"   📝 {context}...")
                            print()
                
                print("=" * 80)
                print("✅ Search completed!")
                print("=" * 80)
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check your internet connection and try again.")


def print_usage():
    """Print usage instructions"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    AWS Knowledge Query Tool                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

USAGE:
    python ask_aws.py "your question" [topic] [limit]

ARGUMENTS:
    question    Your question about AWS (required, use quotes)
    topic       Topic category (optional, default: general)
    limit       Number of results (optional, default: 5)

AVAILABLE TOPICS:
    general                  - Best practices, architecture, tutorials
    reference_documentation  - API/SDK/CLI documentation
    troubleshooting         - Error messages and debugging
    cdk_docs                - CDK concepts and API reference
    cdk_constructs          - CDK code examples and patterns
    cloudformation          - CloudFormation templates
    current_awareness       - New features and announcements
    amplify_docs            - Amplify framework documentation

EXAMPLES:
    # Basic question (uses default 'general' topic)
    python ask_aws.py "How to create a Lambda function"
    
    # Specify topic
    python ask_aws.py "boto3 S3 upload file" reference_documentation
    
    # Specify topic and limit
    python ask_aws.py "Lambda timeout error" troubleshooting 3
    
    # CDK examples
    python ask_aws.py "Lambda function CDK Python" cdk_constructs
    
    # Troubleshooting
    python ask_aws.py "AccessDenied S3 error" troubleshooting
    
    # New features
    python ask_aws.py "Lambda new features 2024" current_awareness

TIPS:
    - Use quotes around your question
    - Be specific with service names
    - Include language/framework when relevant
    - Use exact error messages for troubleshooting

For detailed topic guide, see: SEARCH_GUIDE.md
""")


def main():
    """Main entry point"""
    
    # Check arguments
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)
    
    # Parse arguments
    question = sys.argv[1]
    topic = sys.argv[2] if len(sys.argv) > 2 else "general"
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    
    # Validate topic
    valid_topics = [
        "general", "reference_documentation", "troubleshooting",
        "cdk_docs", "cdk_constructs", "cloudformation",
        "current_awareness", "amplify_docs"
    ]
    
    if topic not in valid_topics:
        print(f"\n❌ Invalid topic: {topic}")
        print(f"Valid topics: {', '.join(valid_topics)}")
        print("\nRun 'python ask_aws.py --help' for more information.")
        sys.exit(1)
    
    # Run the query
    asyncio.run(ask_aws(question, topic, limit))


if __name__ == "__main__":
    main()
