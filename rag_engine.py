from langchain_core.vectorstores import VectorStore

import config
from docment_loader import load_document
import os

from text_split import SimpleTextSplit


class RagEngine:
    def __init__(self, vector_store: VectorStore, chat_func, embed_func):
        self.vector_store = vector_store
        self.chat_func = chat_func
        self.embed_func = embed_func

    def index_file(self, file_path:str, split_type:str='Simple'):
        text = load_document(file_path)
        source = os.path.basename(file_path)
        if split_type == 'Simple':
            spliter = SimpleTextSplit(config.CHUNK_SIZE,config.CHUNK_OVERLAP)

        chunks = spliter.split(text)
        texts = []
        metadatas = []
        for chunk in chunks:
            meta = chunk.get("matadata", {})
            mata["source"] = source
            metadatas.append(meta)

        self.vector_store.delete_by_source