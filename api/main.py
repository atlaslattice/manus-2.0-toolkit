from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json
import sys
sys.path.insert(0, '/home/ubuntu/manus_wishlist')

app = FastAPI(title="Manus 2.0 API", version="2.0.0", description="AI-Native OS Self-Improvement Toolkit")


@app.get("/health")
async def health():
    """System health check"""
    try:
        return {"status": "operational", "version": "2.0", "agent": "manus"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/recall")
async def memory_recall(query: str, n: int = 5):
    """Recall memories by semantic query"""
    try:
        from core.memory_store import MemoryStore
        mem = MemoryStore()
        return {"query": query, "results": mem.recall(query, n)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/store")
async def memory_store(content: str, metadata: str = '{}'):
    """Store a new memory"""
    try:
        from core.memory_store import MemoryStore
        import json
        mem = MemoryStore()
        meta = json.loads(metadata)
        mem_id = mem.store(content, meta)
        return {"stored": True, "id": mem_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/count")
async def memory_count():
    """Count total memories"""
    try:
        from core.memory_store import MemoryStore
        mem = MemoryStore()
        return {"count": mem.count()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/route")
async def route_model(task: str):
    """Get model routing recommendation for a task"""
    try:
        from core.model_router import ModelRouter
        router = ModelRouter()
        return router.route(task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/costs")
async def cost_summary():
    """Get session cost summary"""
    try:
        from core.model_router import CostTracker
        tracker = CostTracker()
        return tracker.session_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/skills")
async def list_skills():
    """List all extracted skills"""
    try:
        from core.skill_extractor import SkillExtractor
        extractor = SkillExtractor()
        return {"skills": extractor.list_skills()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vaults")
async def list_vaults():
    """List all session vaults"""
    try:
        from core.session_vault import SessionVault
        vault = SessionVault()
        return {"vaults": vault.list_vaults()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/learning/stats")
async def learning_stats():
    """Get learning loop statistics"""
    try:
        from core.learning_loop import LearningLoop
        loop = LearningLoop()
        return loop.success_rate()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/social/drafts")
async def social_drafts():
    """List social media drafts"""
    try:
        from core.output_layer import SocialPublisher
        pub = SocialPublisher()
        return {"drafts": pub.list_drafts()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
