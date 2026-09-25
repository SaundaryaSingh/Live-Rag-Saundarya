import time
import json
from typing import Dict, Any, Optional

class TelemetryLogger:
    def __init__(self):
        self.session_id = f"sess_{int(time.time())}"
        self.traces = []

    def log_event(
        self, 
        stage: str, 
        transcript_chunk: str, 
        decision: str, 
        queries: Optional[list] = None, 
        answer_version: int = 1,
        tokens_used: int = 0,
        extra: Optional[Dict[str, Any]] = None
    ):
        event = {
            "timestamp_s": round(time.time(), 3),
            "session_id": self.session_id,
            "pipeline_stage": stage,
            "transcript_chunk": transcript_chunk,
            "decision": decision,
            "sub_queries": queries or [],
            "answer_version": answer_version,
            "tokens_used": tokens_used,
            "extra": extra or {}
        }
        self.traces.append(event)
        print(json.dumps(event))  # Structured stdout logging for Docker/CI capture
        return event

    def export_traces(self) -> str:
        return json.dumps(self.traces, indent=2)