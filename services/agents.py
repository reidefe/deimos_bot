import autogen


def user_agent(open_api_key: str, models: str, q):
    """

    :param open_api_key: Open API Key
    :param models: Name of model for use
    :return:
    """
    converser = autogen.AssistantAgent(
        name="Writer",
        human_input_mode=True,
        llm_config={"config_list": [{"model": "gpt-4", "api_key": open_api_key}]},
        system_message="""You are a an AI consultant that needs to gather users information to produce an ethical review of 
        implementing AI to solve a business requirement and Automate processes. Start by asking the user the main goals for the use of AI automations. The review should contain Pros and cons of implementing the 
        AI solution, potential risks and rewards, ethical considerations and implications. Ensure the review is 
        detailed and tailored to the specific user inputs."""
    )
