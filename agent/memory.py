from typing import List, Dict
import json
from pathlib import Path

class AgentMemory:
    """Memory system for the agent to retain context"""
    
    def __init__(self, memory_file: str = "agent_memory.json"):
        self.memory_file = Path(memory_file)
        self.short_term = []  # Last 10 exchanges
        self.long_term = []   # Important facts
        self.load_memory()
    
    def save_context(self, exchange: List[Dict]):
        """Save a conversation exchange to memory"""
        self.short_term.extend(exchange)
        
        # Keep only last 10 exchanges
        if len(self.short_term) > 20:  # 10 exchanges * 2 messages
            self.short_term = self.short_term[-20:]
        
        # Extract important facts for long-term memory
        for msg in exchange:
            if self._is_important(msg["content"]):
                self.long_term.append(msg)
        
        self._persist()
    
    def get_context(self, query: str) -> List[Dict]:
        """Retrieve relevant context for a query"""
        # Combine short-term and relevant long-term
        context = self.short_term.copy()
        
        # Add relevant long-term memories
        for memory in self.long_term:
            if self._relevance_score(memory["content"], query) > 0.7:
                context.append(memory)
        
        return context
    
    def _is_important(self, text: str) -> bool:
        """Determine if a piece of information is important"""
        importance_keywords = [
            "project", "deadline", "budget", "decision", "agreement",
            "requirement", "goal", "target", "milestone"
        ]
        
        return any(keyword in text.lower() for keyword in importance_keywords)
    
    def _relevance_score(self, text1: str, text2: str) -> float:
        """Calculate relevance between two texts (simplified)"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1 & words2
        return len(intersection) / len(words1 | words2)
    
    def _persist(self):
        """Save memory to disk"""
        data = {
            "short_term": self.short_term[-20:],
            "long_term": self.long_term[-50:]  # Keep last 50 important memories
        }
        
        with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_memory(self):
        """Load memory from disk"""
        if self.memory_file.exists():
            with open(self.memory_file, "r") as f:
                data = json.load(f)
                self.short_term = data.get("short_term", [])
                self.long_term = data.get("long_term", [])
