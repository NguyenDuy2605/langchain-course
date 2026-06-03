from dotenv import load_dotenv
import os
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
load_dotenv()


llm = ChatAnthropic(model_name="claude-sonnet-4-6", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Tìm kiếm cho tôi 3 thành phố của Việt Nam có nhiệt độ cao nhất hôm nay")})
    print(result)

if __name__ == "__main__":
    main()
