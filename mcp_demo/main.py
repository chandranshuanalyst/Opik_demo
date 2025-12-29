from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from opik.integrations.langchain import OpikTracer
import asyncio 
import os
from dotenv import load_dotenv
import opik
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "llama-3.3-70b-versatile", api_key=GROQ_API_KEY, temperature=0)

server_params = StdioServerParameters(
    command = "python",
    args= ["mcp_tool.py"],
)

opik.configure(use_local=False)
os.environ["OPIK_PROJECT_NAME"] = "mcp-test-project"

opik_tracer = OpikTracer(tags=["mcp_agent","arithmetic_agent","ecl_calculation_agent"])

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("MCP session initialized.")
            tools = await load_mcp_tools(session)
            print("MCP tools loaded:", tools)
            agent = create_agent(
                model=model,
                tools=tools
            )
            
            print("Agent created. Running...")  
            response = await agent.ainvoke(
                    {"messages": [{"role": "user", "content": "What is ECL when PD is 0.01,LGD is 0.5 and EAD is 80.Also, Add 2 and 4, then raise the result to the power of 3."}]},
                    config={"callbacks": [opik_tracer]}
            )
            print("Agent response:", response['messages'][-1])
            return response['messages'][-1].content
        
if __name__ == "__main__":
    print("Starting MCP Client...")
    result = asyncio.run(run_agent())
    print("Final Result:", result)