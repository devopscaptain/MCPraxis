#!/usr/bin/env python3
"""
Interactive AWS Knowledge Assistant
Chat-style interface to ask questions about AWS
"""

import asyncio
import json
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from datetime import timedelta


class AWSAssistant:
    def __init__(self):
        self.mcp_url = "https://knowledge-mcp.global.api.aws"
        self.session = None
        
    async def connect(self):
        """Connect to AWS Knowledge MCP Server"""
        print("🔗 Connecting to AWS Knowledge MCP Server...")
        self.client = streamablehttp_client(
            self.mcp_url, 
            headers={}, 
            timeout=timedelta(seconds=60)
        )
        self.streams = await self.client.__aenter__()
        read_stream, write_stream, _ = self.streams
        
        self.session = ClientSession(read_stream, write_stream)
        await self.session.__aenter__()
        await self.session.initialize()
        print("✅ Connected!\n")
    
    async def disconnect(self):
        """Disconnect from server"""
        if self.session:
            await self.session.__aexit__(None, None, None)
        if self.client:
            await self.client.__aexit__(None, None, None)
    
    async def ask(self, question, topic="general", limit=3):
        """Ask a question"""
        try:
            result = await self.session.call_tool(
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
            print(f"❌ Error: {e}")
            return []
    
    async def list_regions(self):
        """List AWS regions"""
        try:
            result = await self.session.call_tool(
                "aws___list_regions",
                arguments={}
            )
            
            for content in result.content:
                if hasattr(content, 'text'):
                    data = json.loads(content.text)
                    return data.get('content', {}).get('result', [])
            
            return []
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
    
    async def check_availability(self, service, resource_type="product"):
        """Check service availability across regions"""
        try:
            result = await self.session.call_tool(
                "aws___get_regional_availability",
                arguments={
                    "resource_type": resource_type,
                    "filters": [service]
                }
            )
            
            for content in result.content:
                if hasattr(content, 'text'):
                    data = json.loads(content.text)
                    return data.get('content', {}).get('result', [])
            
            return []
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return []


def print_results(results):
    """Pretty print search results"""
    if not results:
        print("\n❌ No results found. Try a different query.\n")
        return
    
    print("\n" + "=" * 80)
    print("📚 RESULTS")
    print("=" * 80)
    
    for i, item in enumerate(results, 1):
        print(f"\n{i}. {item['title']}")
        print(f"   🔗 {item['url']}")
        if item.get('context'):
            context = item['context'][:250]
            print(f"   📝 {context}...")
    
    print("\n" + "=" * 80 + "\n")


async def interactive_mode():
    """Run interactive chat mode"""
    assistant = AWSAssistant()
    await assistant.connect()
    
    print("=" * 80)
    print("🤖 AWS Knowledge Assistant - Interactive Mode")
    print("=" * 80)
    print("\nCommands:")
    print("  ask <question>              - Ask about AWS services")
    print("  topic <name>                - Change topic (current: general)")
    print("  regions                     - List all AWS regions")
    print("  available <service>         - Check service availability")
    print("  topics                      - Show available topics")
    print("  help                        - Show this help")
    print("  quit / exit                 - Exit the assistant")
    print("\n" + "=" * 80 + "\n")
    
    current_topic = "general"
    
    try:
        while True:
            try:
                user_input = input("💬 You: ").strip()
                
                if not user_input:
                    continue
                
                # Parse command
                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                if command in ['quit', 'exit', 'q']:
                    print("\n👋 Goodbye!")
                    break
                
                elif command == 'help':
                    print("\nCommands:")
                    print("  ask <question>              - Ask about AWS services")
                    print("  topic <name>                - Change topic")
                    print("  regions                     - List all AWS regions")
                    print("  available <service>         - Check service availability")
                    print("  topics                      - Show available topics")
                    print("  quit / exit                 - Exit\n")
                
                elif command == 'topics':
                    print("\n📚 Available Topics:")
                    print("  • general                  - Best practices, architecture")
                    print("  • reference_documentation  - API/SDK/CLI docs")
                    print("  • troubleshooting         - Error messages, debugging")
                    print("  • cdk_docs                - CDK concepts")
                    print("  • cdk_constructs          - CDK code examples")
                    print("  • cloudformation          - CloudFormation templates")
                    print("  • current_awareness       - New features")
                    print("  • amplify_docs            - Amplify framework\n")
                
                elif command == 'topic':
                    if args:
                        current_topic = args
                        print(f"\n✅ Topic changed to: {current_topic}\n")
                    else:
                        print(f"\n📌 Current topic: {current_topic}\n")
                
                elif command == 'regions':
                    print("\n🌍 Fetching AWS regions...")
                    regions = await assistant.list_regions()
                    print("\n📍 AWS Regions:")
                    for region in regions[:10]:  # Show first 10
                        print(f"   • {region['region_id']:20} - {region['region_long_name']}")
                    if len(regions) > 10:
                        print(f"   ... and {len(regions) - 10} more regions")
                    print()
                
                elif command == 'available':
                    if args:
                        print(f"\n🔍 Checking availability for: {args}")
                        availability = await assistant.check_availability(args)
                        if availability:
                            print(f"\n✅ Found availability data:")
                            for item in availability[:5]:
                                print(f"   {item}")
                        else:
                            print(f"\n❌ No availability data found for: {args}")
                    else:
                        print("\n❌ Please specify a service name")
                    print()
                
                elif command == 'ask':
                    if args:
                        print(f"\n🔍 Searching for: {args}")
                        print(f"   Topic: {current_topic}")
                        results = await assistant.ask(args, current_topic, 3)
                        print_results(results)
                    else:
                        print("\n❌ Please provide a question\n")
                
                else:
                    # Treat entire input as a question
                    print(f"\n🔍 Searching for: {user_input}")
                    print(f"   Topic: {current_topic}")
                    results = await assistant.ask(user_input, current_topic, 3)
                    print_results(results)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Goodbye!")
                break
    
    finally:
        await assistant.disconnect()


if __name__ == "__main__":
    print("\n🚀 Starting AWS Knowledge Assistant...\n")
    asyncio.run(interactive_mode())
