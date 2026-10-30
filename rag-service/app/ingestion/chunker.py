def chunk_text(text, chunk_size, overlap):

    if chunk_size <= 0:
        raise  ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and less than chunk_size")
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        end = min(end, len(text))

        chunk = text[start:end]
        chunks.append(chunk)

        start = (start + chunk_size) - overlap

    return chunks