from chains import TemplateChain
template = """Translate the following sentence to Spanish.
Examples:
"Hello, how are you?" -> "Hola, ¿cómo estás?"
"Goodbye, see you later" -> "Adiós, hasta luego"
"Where is the bathroom?" -> "¿Dónde está el baño?"

Now, traslate this sentence and produce only the Spanish counterpart: {sentence}
"""
chain = TemplateChain("Translate the following sentence to Spanish: {sentence}")
print(chain.invoke("Ciao come ti chiami?"))