
from config import LOCAL_EMBEDDING_MODEL_PATH
from sentence_transformers import SentenceTransformer

_embed_model = None

def _get_embed_model():
    global _embed_model
    if _embed_model is None:
        _embed_model = SentenceTransformer(LOCAL_EMBEDDING_MADE_PATH)
        return _embed_model

del get_embedding():