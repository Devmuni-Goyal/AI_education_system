from pydantic import BaseModel
from typing import List, Optional

class AISection(BaseModel):
    section_name: str
    description: str
    content_url: str

class ChatMessage(BaseModel):
    sender: str
    message: str
    timestamp: str

class SearchResult(BaseModel):
    title: str
    description: str
    resource_url: str
    type: Optional[str] = "resource"  # Could be 'video', 'pdf', etc.

class SearchRequest(BaseModel):
    query: str

class ChatRequest(BaseModel):
    user_message: str
