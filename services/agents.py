import json
import anthropic
import autogen
import loguru
from groq import Groq
# from tools import create_file
# import openai
from openai import OpenAI


def user_agent(open_api_key: str, model: str, message):
    """

    :param open_api_key: Open API Key
    :param model: Name of model for use
    :return:
    """
    con = {"config_list": [{"model": model, "api_key": open_api_key}]}
    assistant = autogen.AssistantAgent('assistant', llm_config=con)
    user = autogen.UserProxyAgent(
        name="Ethics",
        human_input_mode="ALWAYS",
        llm_config=con,
        system_message="""You are a an AI consultant that needs to gather users information to produce an ethical review of 
        implementing AI to solve a business requirement and Automate processes. Start by asking the user the main goals for the use of AI automations. The review should contain Pros and cons of implementing the 
        AI solution, potential risks and rewards, ethical considerations and implications. Ensure the review is 
        detailed and tailored to the specific user inputs."""
    )
    cons = user.initiate_chat(
        assistant,
        message=message
    )
    return cons


async def user_chat(open_api_key: str, model: str, prompt):
    client = OpenAI()
    res = client.chat.completions.create(
        model=model,
        messages=prompt,

    )
    content = res.choices[0].message
    loguru.Logger.info(f'{content}')
    # content = json.dumps(json.loads(res.model_dump_json()), indent=4)
    # loguru.Logger.info(f'{content}')
    return content


async def anthropic_chat(api_key: str, prompt):
    """
    Anthropic chat implementation
    :param open_api_key: Open API Key
    :param model: Name of model for use
    """

    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-3-haiku",
        max_tokens=1000,
        temperature=0.0,
        system="""You are a an AI consultant that needs to gather users information to produce an ethical review of 
        implementing AI to solve a business requirement and Automate processes. Start by asking the user the main goals for the use of AI automations. The review should contain Pros and cons of implementing the 
        AI solution, potential risks and rewards, ethical considerations and implications. Ensure the review is 
        detailed and tailored to the specific user inputs.""",
        messages=[
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return message.content


async def groq_chat(api_key: str, prompt):
    client = Groq(api_key=api_key)
    res = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": """You are a an AI consultant that needs to gather users information to produce an ethical 
                review of implementing AI to solve a business requirement and Automate processes. Start by asking the 
                user the main goals for the use of AI automations. The review should contain Pros and cons of 
                implementing the AI solution, potential risks and rewards, ethical considerations and implications. 
                Ensure the review is detailed and tailored to the specific user inputs.""",
            },
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]

    )
    content = res.choices[0].message.content

    return content


async def groq_intro_chat(api_key: str, prompt):
    client = Groq(api_key=api_key)
    res = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": """you are an AI assistant that welcomes users with one short message on how to  AI can help 
                automate different businesses""",
            },
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]

    )
    content = res.choices[0].message.content
    return content
