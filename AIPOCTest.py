import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr


async def sitevalidations():
    os.environ["GEMINI_API_KEY"]="AIzaSyC9cIKikVWKcpXNhaJXJTZJOB5Y8ovKLQM"
    task=(
        'Important : I am UI Automation tester validating the tasks'
        'Open website https://azhrsaint.amer.reisystems.com/EAuthNS/external/account/SignIn'
        'login with username Penni.Ratchford.10959690@test.com and password INT-EH3S-re!1'
        'then navigate to pp portal  https://azhrsaint-is2.amer.reisystems.com/FTCA.Web/external/ftca/policiesprocedure?tc=2&cc=4&rtc=62&rv=e8486f86-207a-46ec-9d9c-aca75e693b51'
         'Get the page header title while logged in'
        'Then logout from the application'
    )
    api_key= os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=SecretStr(api_key))
    agent=Agent(task,llm,use_vision=True)
    history=await agent.run()
    test_result=history.final_result()
    print(test_result)

asyncio.run(sitevalidations())