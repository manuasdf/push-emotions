from datetime import datetime
filename = "emotion.csv"
data = [input("What do you feel right now? "),
        input("What is the context you're in right now? "),
        datetime.today().strftime('%Y-%m-%d')]
with open(filename, "a") as f:
  try:
      f.write(",".join(data))
      f.write("\n")
  except EOFError:
      print("Error")
