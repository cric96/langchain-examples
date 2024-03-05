# Langchain prompting
This project showcases some simple prompting engineering techniques using [Langchain](https://www.langchain.com/).

## Installation
Creating a virtual environment is recommended. Then, install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## Usage

In chains.py, you can find the following code:
```python
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
```
That is a simple example of how to create a chain using Langchain. 
For the purpose of this lesson, the idea is to create a chain that prompts the user for a sentence and then returns the sentence.
Inside the template, the sentence should be specified in the following way:
```python
template = "Reply as if you would be a doctor. Sentence: {sentence}"
```

The `|` operator is used to chain the different runnables. In this case, the chain is composed of a `RunnablePassthrough` and a `ChatPromptTemplate` that prompts the user for a sentence. The `Ollama` model is used to generate a response based on the sentence provided by the user.
[Ollama](https://ollama.com/) support different models, in this case, the model "mistral" is considered as default.

## Examples

- main.py: showcases how to use the TemplateChain class to prompt the user for a sentence and then return the sentence.
- zero_shot.py: instruct the model to generate a response based on some fixed instructions (i.e., context). In some library, it is called "system prompt" or "system instruction".
- few_shot.py: it gives both the instructions and some examples of the expected input-output pairs.
- self-consistency: it is a technique to improve the quality of the model's response. It is used to check if the model's response is consistent with the input. It is typically combined with chain-of-thoughts to improve the quality of the model's response.
