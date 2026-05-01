import os
from typing import List, Dict, Any
from .memory import AgentMemory
from .tools import AgentTools

class DocumentAgent:
    """Main agent class that orchestrates document processing tasks"""
    
    def __init__(self, name: str = "DocAssist"):
        self.name = name
        self.memory = AgentMemory()
        self.tools = AgentTools()
        self.conversation_history = []
        
    def process_command(self, user_input: str) -> str:
        """Process user command and return agent response"""
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Analyze intent
        intent = self._analyze_intent(user_input)
        
        # Execute appropriate tool
        if intent["action"] == "summarize":
            response = self.tools.summarize_document(intent["target"])
        elif intent["action"] == "search":
            response = self.tools.search_documents(intent["query"])
        elif intent["action"] == "generate":
            response = self.tools.generate_content(intent["prompt"])
        elif intent["action"] == "compare":
            response = self.tools.compare_documents(intent["docs"])
        else:
            response = self._general_chat(user_input)
        
        # Add response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        # Save to memory
        self.memory.save_context(self.conversation_history[-2:])
        
        return response
    
    def _analyze_intent(self, user_input: str) -> Dict[str, Any]:
        """Analyze user input to determine intent and extract parameters"""
        user_lower = user_input.lower()
        
        # Summarization intent
        if any(word in user_lower for word in ["summarize", "summary", "总结", "摘要"]):
            return {
                "action": "summarize",
                "target": self._extract_document_name(user_input)
            }
        
        # Search intent
        if any(word in user_lower for word in ["find", "search", "查找", "搜索", "mention"]):
            return {
                "action": "search",
                "query": self._extract_search_query(user_input)
            }
        
        # Generation intent
        if any(word in user_lower for word in ["generate", "create", "write", "生成", "创建", "写"]):
            return {
                "action": "generate",
                "prompt": user_input
            }
        
        # Comparison intent
        if any(word in user_lower for word in ["compare", "对比", "比较", "difference"]):
            return {
                "action": "compare",
                "docs": self._extract_multiple_docs(user_input)
            }
        
        return {"action": "chat"}
    
    def _extract_document_name(self, text: str) -> str:
        """Extract document name from user input"""
        # Simple extraction - can be enhanced
        words = text.split()
        for i, word in enumerate(words):
            if word.endswith(('.pdf', '.docx', '.txt', '.doc')):
                return word
        return "latest_document"
    
    def _extract_search_query(self, text: str) -> str:
        """Extract search query from user input"""
        # Remove command words
        query = text.lower()
        for word in ["find", "search", "查找", "搜索", "all mentions of"]:
            query = query.replace(word, "")
        return query.strip()
    
    def _extract_multiple_docs(self, text: str) -> List[str]:
        """Extract multiple document names"""
        # Simple implementation
        return ["doc1", "doc2"]
    
    def _general_chat(self, user_input: str) -> str:
        """Handle general conversation"""
        return f"I understand you said: {user_input}. How can I help you with document processing today?"

if __name__ == "__main__":
    # Test the agent
    agent = DocumentAgent()
    
    test_commands = [
        "Summarize the quarterly report PDF",
        "Find all mentions of budget in these documents",
        "Generate meeting notes from this transcript"
    ]
    
    for cmd in test_commands:
        print(f"\nUser: {cmd}")
        response = agent.process_command(cmd)
        print(f"Agent: {response}")
