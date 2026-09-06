
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
    }
]