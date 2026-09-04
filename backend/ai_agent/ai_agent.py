from threading import Lock
from langchain_ollama import ChatOllama
from langchain_core.messages import ToolMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
LLM_AUTH = os.getenv("LLM_AUTH", "")


class AiAgent:
    _lock = Lock()
    _instance = None

    def __init__(self, model: str, tools: list, temperature: float):
        self.tool_map = {t.name: t for t in tools}

        self.llm = ChatOllama(
            base_url='https://ollama.com',
            model=model,
            temperature=temperature,
            client_kwargs={
                "headers": {
                    "Authorization": LLM_AUTH,
                    # "X-Custom-Header": "custom_value"
                }
            }
        )

            # Bind the tools to the model
        self.llm_with_tools = self.llm.bind_tools(tools)

    @classmethod
    def init(cls, model: str, tools: list, temperature: float):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  
                    cls._instance = cls(model, tools, temperature)
        return cls._instance
    
    @classmethod
    async def chat(cls, prompt: str) -> str:
        if cls._instance is None:
            raise RuntimeError("AiAgent not initialized. Call AiAgent.init() first.")
        
        agent = cls._instance
        messages = [HumanMessage(content=prompt)]

        # first LLM call
        ai_msg = await agent.llm_with_tools.ainvoke(messages)
        messages.append(ai_msg)

        # handle tool calls if any
        if ai_msg.tool_calls:
            for tool_call in ai_msg.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]

                if tool_name in agent.tool_map:
                    tool_obj = agent.tool_map[tool_name]
                    try:
                        # use ainvoke for async tools
                        tool_output = await tool_obj.ainvoke(tool_args)
                    except Exception as e:
                        tool_output = f"Error executing tool: {str(e)}"

                    messages.append(
                        ToolMessage(
                            content=str(tool_output),
                            tool_call_id=tool_call["id"]
                        )
                    )

            # second LLM call with tool results
            final_msg = await agent.llm.ainvoke(messages)
            return final_msg.content

        return ai_msg.content