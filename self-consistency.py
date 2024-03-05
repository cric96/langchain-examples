from chains import TemplateChain
template = """
Reply ONLY the number of apples. No need of examplation. Reply structure: (A: <number>)
Q: Today I have 6 apples. Tomorrow I buy 3 more.
How many apples do I have?
A: 9
Q: Today I have 6 apples. Yesterday I ate 6 apples, How many apples
do I have?
A: 6
Q: {sentence}
"""
question = """
Today I have 6 apples. Tomorrow I buy 3 more. Yesterday I ate 6
apples, How many apples do I have?
"""
chain = TemplateChain(template)
consistencies_numbers = 5
replies = []
for i in range(consistencies_numbers):
  replies.append(chain.invoke(question))

for i in range(consistencies_numbers):
  print(replies[i])
# extract numbers taking the first three characters of the reply and then split the string by the : character
numbers = []
for reply in replies:
  numbers.append(int(reply[4]))

print(numbers)