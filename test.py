from openai import OpenAI

client = OpenAI(
    base_url="https://api.forge.tensorblock.co/v1", 
    api_key="forge-OWJm9bfadd921e05fba16fcaa99e5652c610",  
)
    
models = client.models.list()
print(models)


