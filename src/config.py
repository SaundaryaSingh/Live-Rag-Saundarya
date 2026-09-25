import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Streaming Live RAG Engine"
    VERSION: str = "1.0.0"
    
    # LLM & Embedding Settings
    LLM_MODEL: str = "gpt-4o"  # Or your preferred instruction-tuned model
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    
    # Retrieval & Controller Thresholds
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    STABILITY_CONFIDENCE_THRESHOLD: float = 0.75
    MAX_RETRIEVAL_CHUNKS: int = 5

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()