from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

class TemplateChain():
    def __init__(self, template: str, model: str = "mistral"):
        self.template = template
        prompt = ChatPromptTemplate.from_template(template)
        model = Ollama(model=model)

        self.chain = {"sentence": RunnablePassthrough()} | prompt | model

    def invoke(self, sentence: str):
      return self.chain.invoke(sentence)
    

def plain_chain():
    return TemplateChain("{sentence}")