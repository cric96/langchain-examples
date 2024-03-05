from chains import TemplateChain

chain = TemplateChain("Translate the following sentence to Spanish: {sentence}")
print(chain.invoke("Ciao come ti chiami?"))