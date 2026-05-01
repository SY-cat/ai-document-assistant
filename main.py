#!/usr/bin/env python3
"""
AI Document Assistant - Main Entry Point

A Python-based AI agent that helps users process, analyze, and generate documents.
"""

import sys
import argparse
from pathlib import Path
from agent import DocumentAgent

def main():
    """Main function to run the AI Document Assistant"""
    
    parser = argparse.ArgumentParser(
        description="AI Document Assistant - Process and analyze documents with AI"
    )
    parser.add_argument(
        "--mode",
        choices=["interactive", "batch"],
        default="interactive",
        help="Run mode: interactive (chat) or batch (process files)"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="File to process (for batch mode)"
    )
    parser.add_argument(
        "--command",
        type=str,
        help="Command to execute (for batch mode)"
    )
    
    args = parser.parse_args()
    
    # Initialize the agent
    print("🤖 Initializing AI Document Assistant...")
    agent = DocumentAgent(name="DocAssist")
    print("✅ Agent initialized successfully!\n")
    
    if args.mode == "interactive":
        run_interactive_mode(agent)
    else:
        run_batch_mode(agent, args)

def run_interactive_mode(agent: DocumentAgent):
    """Run the agent in interactive chat mode"""
    print("=" * 60)
    print("AI Document Assistant - Interactive Mode")
    print("=" * 60)
    print("\nCommands you can try:")
    print("  • 'summarize [document]' - Summarize a document")
    print("  • 'find [query]' - Search for information")
    print("  • 'generate [prompt]' - Generate content")
    print("  • 'compare [doc1] [doc2]' - Compare documents")
    print("  • 'quit' or 'exit' - Exit the program")
    print("\n" + "=" * 60 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "q", "bye"]:
                print("\n👋 Goodbye! Thanks for using AI Document Assistant.")
                break
            
            # Process command
            print(f"\n{agent.name}: ", end="")
            response = agent.process_command(user_input)
            print(response)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using AI Document Assistant.")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again.\n")

def run_batch_mode(agent: DocumentAgent, args):
    """Run the agent in batch mode"""
    if not args.file or not args.command:
        print("❌ Error: Batch mode requires both --file and --command arguments")
        sys.exit(1)
    
    print(f"Processing file: {args.file}")
    print(f"Command: {args.command}\n")
    
    # Construct full command
    full_command = f"{args.command} {args.file}"
    
    # Process
    response = agent.process_command(full_command)
    print("Result:")
    print("=" * 60)
    print(response)
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Fatal Error: {str(e)}")
        sys.exit(1)
