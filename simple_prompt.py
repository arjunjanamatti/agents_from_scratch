import ollama

llm = "llama3.2"

question = """who had died on 09 Sep 2024?"""

response = ollama.chat(model=llm,
                       messages=[{'role':'system', 'content':''},
                                           {'role':'user', 'content':question}])

print(response['message']['content'])