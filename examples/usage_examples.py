"""
Example usage of the AI Document Assistant Agent

This file demonstrates various ways to use the agent programmatically.
"""

from agent import DocumentAgent

def example_1_summarization():
    """Example 1: Document Summarization"""
    print("=" * 60)
    print("Example 1: Document Summarization")
    print("=" * 60)
    
    agent = DocumentAgent()
    
    # Simulate user commands
    commands = [
        "Summarize the quarterly_report.pdf",
        "Can you provide a summary of the strategy_document.docx?",
        "I need a brief overview of meeting_notes.txt"
    ]
    
    for cmd in commands:
        print(f"\n👤 User: {cmd}")
        response = agent.process_command(cmd)
        print(f"🤖 Agent: {response[:200]}...")  # Print first 200 chars

def example_2_search():
    """Example 2: Intelligent Search"""
    print("\n" + "=" * 60)
    print("Example 2: Intelligent Search")
    print("=" * 60)
    
    agent = DocumentAgent()
    
    search_queries = [
        "Find all mentions of budget in these documents",
        "Search for revenue projections",
        "Locate all references to customer satisfaction"
    ]
    
    for query in search_queries:
        print(f"\n👤 User: {query}")
        response = agent.process_command(query)
        print(f"🤖 Agent: Found relevant information...")

def example_3_generation():
    """Example 3: Content Generation"""
    print("\n" + "=" * 60)
    print("Example 3: Content Generation")
    print("=" * 60)
    
    agent = DocumentAgent()
    
    generation_requests = [
        "Generate a project status report based on these meeting notes",
        "Create an executive summary from the technical documentation",
        "Write a follow-up email summarizing our discussion"
    ]
    
    for request in generation_requests:
        print(f"\n👤 User: {request}")
        response = agent.process_command(request)
        print(f"🤖 Agent: I've generated the content...")

def example_4_comparison():
    """Example 4: Document Comparison"""
    print("\n" + "=" * 60)
    print("Example 4: Document Comparison")
    print("=" * 60)
    
    agent = DocumentAgent()
    
    comparison_request = "Compare the Q2_strategy.pdf and Q3_strategy.pdf documents"
    print(f"\n👤 User: {comparison_request}")
    response = agent.process_command(comparison_request)
    print(f"🤖 Agent: Here's a detailed comparison...")

def example_5_conversation():
    """Example 5: Multi-turn Conversation"""
    print("\n" + "=" * 60)
    print("Example 5: Multi-turn Conversation with Memory")
    print("=" * 60)
    
    agent = DocumentAgent()
    
    conversation = [
        "Hi, I need help with document analysis",
        "Can you summarize the quarterly report?",
        "What were the key findings?",
        "Can you elaborate on the budget section?",
        "Thanks, that was helpful"
    ]
    
    for message in conversation:
        print(f"\n👤 User: {message}")
        response = agent.process_command(message)
        print(f"🤖 Agent: {response[:150]}...")

if __name__ == "__main__":
    print("\n🚀 AI Document Assistant - Usage Examples\n")
    
    # Run all examples
    example_1_summarization()
    example_2_search()
    example_3_generation()
    example_4_comparison()
    example_5_conversation()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed successfully!")
    print("=" * 60 + "\n")
