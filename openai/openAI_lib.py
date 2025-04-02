from openai import OpenAI
from dotenv import dotenv_values

secrets= dotenv_values (".env")

#self=OpenAI()

class OpenAILibrary:        

    def get_openai_instance(self):
        client=OpenAI()
        return client
    
    def input_message(role, topic):
        input_message = [
            {
                "role": role,
                "content": topic
            }
        ]
        return input_message
    
    def response_create_model(self):
        model= "gpt-4o-mini"
        return model
    
    # --------------------------------------------------------------------------
    # Manual conversation state, single random chat no state/history is retained
    # --------------------------------------------------------------------------

    def first_conversation(self, client, content):
        model=self.response_create_model()
        response = client.responses.create(
            model=model,
            input=content,
        )
        return response
    
    # -------------------------------------------------------------------------------------
    # OpenAI conversation state is retained to stay in the chat topic (default is to store)
    # -------------------------------------------------------------------------------------

    def next_conversation(self, client, input, response_id):
        model= self.response_create_model()
        next_response = client.responses.create(
            model= model,
            previous_response_id=response_id,
            input=input,
            #store= True (set default)
        )
        return next_response

    # ----------------------------------------------------------------------------------------
    # OpenAI query your Knowledge base using file_search
    # We need a vector database service like PineCone and connect agent to that vectore Db OR
    # Create a vector database in platform.openai.com -> storage -> Vector stores -> +Create
    # Then upload files to our Vector store
    # Copy the ID of the Vectore store created and add to the vector_store_ids in tools
    # ----------------------------------------------------------------------------------------

    def query_knowledge_base(self, client, input):
        tools = [{
        "type": "file_search",
        "vector_store_ids": ["Vector_store1_id", "Vector_store2_id"],
        "max_num_results": 3
        }]
        model= self.response_create_model()
        response = client.responses.create(
        model= model,
        instructions= "You are a helpful assistant.",
        input=input,
        tools=tools, 
        include= ["file_search_call.results"]       
        )       
        return response
    
    # ---------------------------------
    # OpenAI query web using web_search
    # ---------------------------------
    
    def web_search(self, client, input):
        tools=[
            {
                "type": "web_search_preview",
                "user_location": {
                    "type": "approximate",
                    "country": "GB",
                    "city": "London",
                    "region": "London",
                }
            }
        ]
        model=self.response_create_model()
        response = client.responses.create(
            model=model,
            instructions="When looking up real time data using web search, do not ask for the user's location. It will be provided by the web search tool itself.",
            input=input,
            tools=tools
        )
        return response
    
# Analyze the content of an image

def analyze_image(self, client, topic, image_url ):
    model=self.response_create_model()
    response = client.responses.create(
    model=model,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": topic},
            {
                "type": "input_image",
                "image_url": image_url,
                "detail": "low",
            },
        ],
    }],
)

    return response