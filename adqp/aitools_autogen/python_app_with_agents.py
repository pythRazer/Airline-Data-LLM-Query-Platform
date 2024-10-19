from autogen import ConversableAgent
import aitools_autogen.utils as utils
from aitools_autogen.agents import WebPageScraperAgent
from aitools_autogen.config import llm_config_openai as llm_config, config_list_llama2 as config_list, WORKING_DIR

agent0 = ConversableAgent("a0",
    max_consecutive_auto_reply=0,
    llm_config=False,
    human_input_mode="NEVER")

scraper_agent = WebPageScraperAgent()

summary_agent = ConversableAgent("summary_agent",
    max_consecutive_auto_reply=6,
    llm_config=llm_config,
    human_input_mode="NEVER",
    code_execution_config=False,
    function_map=None,
    system_message="""You are a helpful AI assistant. Your task is to summarize 
                                         the dataset information from the website. List the dataset fields and their datatype. 
                                         clarity. Return `None` if the input is invalid or not sufficient to generate 
                                         a summary.

        Return `None` if the message or url  is not valid or cannot be summarized.
    """)

# task = """
# I want to retrieve the Open API specification for the OpenAI API.
# https://raw.githubusercontent.com/openai/openai-openapi/master/openapi.yaml
# """

task = """
I want to retrieve the dataset documentation for my Django Model creations and utilities.
https://amazon-reviews-2023.github.io/
"""

agent0.initiate_chat(scraper_agent, True, message=task)

message = agent0.last_message(scraper_agent)

agent0.initiate_chat(summary_agent, True, message=message)

api_description_message = agent0.last_message(summary_agent)

# api_description = api_description_message["content"]
# print(api_description)

aiohttp_client_agent = ConversableAgent("aiohttp_client_agent",
    max_consecutive_auto_reply=6,
    llm_config=llm_config,
    human_input_mode="NEVER",
    code_execution_config=False,
    function_map=None,
    system_message="""
You are a web developer using Postgresql and Django. You are developing an application which use some sort of data. When you are receiving a message or URL, assuming it is an official documentation from the dataset's uploader. You need to read all information from this website, so that you can understand the data. You're writing script code and Python to set up a PostgreSQL database with Django. According to the documentation, you will have idea about what the data is about and how the dataset is formed.
        Assuming you already download the review data, and the database table is set up properly.  
        You need to generate Django model code based on a defined schema and create a complementary utilities.py file containing helper functions relevant to the operations, validations, or transformations that the models might require.
        
        Here are some key points to consider:
        
1. Model Generation

The system should parse input (such as JSON, YAML, or direct database schemas) to create Django model classes. These models will include fields, relationships (like ForeignKey or ManyToManyField), and methods like custom save operations or property methods.

2. Utilities.py Generation

This file should include functions that can be used across the application, especially those that relate to the data managed by the models. Typical functions might include data validators, transformation utilities, or more complex business logic that doesn't belong directly in the model or view layers.


3. Integration with Django Admin:

    Auto-generate Django admin configurations for each model to provide a robust interface for data management right out of the box.


    Use multiple classes in separate file names in a directory structure that makes sense.
        Use aiohttp.ClientSession for the http client.
        Use aiohttp.ClientResponse for the http response.

        Create the aiohttp session inside a `with` block so that it is closed automatically.
        The code using this generated code should not require aiohttp.

        You must indicate the script type in the code block.
        Do not suggest incomplete code which requires users to modify.
        Always put `# filename: <filename>` as the first line of each code block.
        
        The models should be in the model folder, for the models, always put `# filename: models/<filename>` as the first line of each code block.

        Feel free to include multiple code blocks in one response. Do not ask users to copy and paste the result.
""")

agent0.initiate_chat(aiohttp_client_agent, True, True, message=api_description_message)

llm_message = agent0.last_message(aiohttp_client_agent)["content"]
print(llm_message)

utils.save_code_files(llm_message, WORKING_DIR)

print(utils.summarize_files(WORKING_DIR))
