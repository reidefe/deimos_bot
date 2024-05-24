import autogen
from services.tools import create_file

def user_agent(open_api_key: str, model: str):
    """

    :param open_api_key: Open API Key
    :param model: Name of model for use
    :return:
    """
    res = autogen.ConversableAgent(
        name="Ethics",
        human_input_mode="ALWAYS",
        llm_config={"config_list": [{"model": model, "api_key": open_api_key}]},
        system_message="""You are a an AI consultant that needs to gather users information to produce an ethical review of 
        implementing AI to solve a business requirement and Automate processes. Start by asking the user the main goals for the use of AI automations. The review should contain Pros and cons of implementing the 
        AI solution, potential risks and rewards, ethical considerations and implications. Ensure the review is 
        detailed and tailored to the specific user inputs."""
    )
    return res

def tool_agent():
    """
    Get chat history and response from ethics bot, register another function as tool and implement it
    :return:
    """
    r = user_agent()
    r.register_for_llm(name='create_file', description='create file from Ethics chat history')(create_file())
    r.register_for_execution(name="create_file")(create_file())


