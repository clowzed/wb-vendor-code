import os
def get_environment_variable(variable:str):
    return os.environ.get(variable) or \
           exit(f"Environment variable '{variable}' should be set!")

BOT_TOKEN          = get_environment_variable("BOT_TOKEN")
INSTAGRAM_LOGIN    = get_environment_variable("INSTAGRAM_LOGIN")
INSTAGRAM_PASSWORD = get_environment_variable("INSTAGRAM_PASSWORD")
