
# 工具说明书
TOOLS = [
    {
        "type" : "function",
        "function" : {
            "name" : "add",
            "description" : "两数求和",
            "parameters" : {
                "type" : "object",
                "properties":{
                    "a":{
                        "type" : "number",
                        "description" : "数字a"                        
                    },
                    "b" :{
                        "type" : "number",
                        "description" : "数字b"
                    }
                },
                "required" : ["a", "b"]
            }
        }
    },
    {
        "type":"function",
        "function" :{
            "name": "search_knowledge_base",
            "description": "在本地RAG知识库中检索与用户问题相关的信息.当用户的问题需要依据知识库资料回答时使用",
            "parameters": {
                "type" :"object",
                "properties":{
                    "query":{
                        "type" : "string",
                        "description" : "用户的问题"
                    }
                },
                "required" : ["query"]
            }
        }
    }
]