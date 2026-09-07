import requests

# 二者求和
def add(a: float,b: float) ->float:
    """
    计算两个数字的和。
    Args:
        a(float):
            数字a
        b(float):
            数字b

    Returns:
        float:
            两数之和
    """
    return a + b

RAG_SEARCH_URL = "http://127.0.0.1:8001/search"

def search_knowledge_base(query:str) -> str:
    payload = {
        "question": query,
        "top_k": 3
    }

    response = requests.post(
        RAG_SEARCH_URL,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    results = data["results"]

    if not results:
        return "知识库中没有检索到相关资料。"

    parts = []

    for index, item in enumerate(results, start=1):
        parts.append(
            f"""[资料{index}]
来源文件: {item["filename"]}
Chunk ID: {item["chunk_id"]}
Distance: {item["distance"]}
内容: {item["content"]}"""
        )

    return "\n\n".join(parts)