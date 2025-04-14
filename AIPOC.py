import asyncio
import os

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, BaseModel


class CheckoutResult(BaseModel):
    login_status:str
    Page_title_while_login:str
    CredDate_result:str

controller = Controller(output_model=CheckoutResult)


async def SiteValidation():
    os.environ["GEMINI_API_KEY"]="AIzaSyC9cIKikVWKcpXNhaJXJTZJOB5Y8ovKLQM"
    task=(
        'Important : I am UI Automation tester validating the tasks'
        'Open website https://azhrsaint.amer.reisystems.com/EAuthNS/external/account/SignIn'
        'login with username Hayden.Vincent.19694280@test.com and password INT-EH3S-re!1'
        'then navigate to https://azhrsaint-is2.amer.reisystems.com/FTCA.Web/external/ftca/credentialingprivileging?rv=e8486f86-207a-46ec-9d9c-aca75e693b51&rtc=62&controlName=LeftMenu&PRoleId=18'
         'get page title of the page'
        'wait on the page for 30 second'
         'Then verify Filter should return no result found for Most recent credentialing date field for example 04/04/2024 on grid'
        'then navigate to https://azhrsaint-is2.amer.reisystems.com/FTCA.Web/external/ftca/policiesprocedure?tc=2&cc=4&rtc=62&rv=e8486f86-207a-46ec-9d9c-aca75e693b51'
        'Attach one document to 2nd attachment  control from desktop location Y:\Test\Attachments'
        'wait for 10 seconds'
        'Then logout from the application'
    )
    api_key= os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=SecretStr(api_key))
    agent=Agent(task=task,llm=llm,controller=controller,use_vision=True)
    history=await agent.run()
    test_result=history.final_result()
    print(test_result)

asyncio.run(SiteValidation())