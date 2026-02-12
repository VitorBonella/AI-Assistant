from dataclasses import dataclass
from datetime import datetime

@dataclass
class ChatMessage:
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = datetime.now()