from openAI_lib import OpenAILibrary


openAI= OpenAILibrary()

client= openAI.get_openai_instance()

# Single random conversation with No history

user_input= input("You: ")
response= openAI.first_conversation(client, user_input)
print("Bot: ", response.output_text)
current_response_id= response.id

# Conversation with history. the chat ends by entering 'exit', 'bye', 'quit' 

current_response_id= None
while True:
      user_input= input("You: the chat ends by entering- exit or bye or quit ")
      if user_input.lower() in ['exit', 'bye', 'quit']:
            print("Goodbye!")
            break
      
      input= openAI.input_message("user", user_input)
      response= openAI.next_conversation(client, input, current_response_id)
      print("Bot: ", response.output_text)
      current_response_id= response.id

# query Knowledge base/ File Search

user_input= input("You: Enter query to search knowledge base ")
input= openAI.input_message("user", user_input)
response = openAI. query_knowledge_base(client, input)

for output_item in response.output:
      if output_item.type == "file_search_call":
            print ("Search Results: ")
            for i, result in enumerate(output_item.results, 1):
                  print(f"Result {i}")
                  print(f"Filename: {result.filename}")
                  print(f"Score: {result.score}")
                  print(f"Text snippet: {result.text[:250]}..." if len(result.text) > 250 else f"Test snippet: {result.text}")
      
      if output_item.type == "message":
             for content_item in output_item.content:
                   if content_item.type == "output_text":
                         print("Annotation: ")
                         for annotation in content_item.annotations:
                               if annotation.type== "file_citation":
                                     print(f" Citation from File: {annotation.filename}")

# Web Search

user_input= input("You: Enter query to search the web ")
input= openAI.input_message("user", user_input)
response = openAI. web_search(client, input)

print("AI Response: ", response.output_text)

print("\nCitations:")

for block in response.output:
    if not hasattr(block, 'content'):
        continue

    for content_item in block.content:
        if not hasattr(content_item, 'annotations'):
            continue

        for annotation in content_item.annotations:
            if annotation.type == 'url_citation':
                print(f"- {annotation.title}: {annotation.url}")


#image search
topic= "what's in this image?"
image_url= "C:/Users/PROLINK Staff/OneDrive - PROLINK Insurance Inc/Desktop/ProlinkLibrary/prolink.png"
response= openAI.analyze_image(client, topic, image_url )
print(response.output_text)