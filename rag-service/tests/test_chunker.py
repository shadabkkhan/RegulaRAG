from app.ingestion.chunker import chunk_text
import pytest

def test_chunk_text_basic():
    text = "ABCDEFGHIJ"
    chunk_size = 4
    overlap = 1

    result = chunk_text(text, chunk_size, overlap)

    assert result == ["ABCD", "DEFG", "GHIJ", "J"]


def test_chunk_text_invalid_chunk_size():
    text = "ABCDEFGHIJ"
    chunk_size = 0
    overlap = 0

    with pytest.raises(ValueError):
        chunk_text(text, chunk_size, overlap)


def test_chunk_text_invalid_overlap():
    text = "ABCDEFGHIJ"
    chunk_size = 4
    overlap = 4

    with pytest.raises(ValueError):
        chunk_text(text, chunk_size, overlap)

