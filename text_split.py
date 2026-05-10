
class SimpleTextSplit:
    """
    固定大小的文本分割
    默认每一个chunk长度为500，有50（overlap）的重叠
    """
    def __init__(self, chunk_size:int = 500, overlap:int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text:str):
        chunks = []
        start = 0
        text_len = len(text)
        while start < text_len:
            end = min(start + self.chunk_size, text_len)
            chunks.append(text[start:end])
            start = start + self.chunk_size - self.overlap

        return chunks
