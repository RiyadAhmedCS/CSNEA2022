from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from random import randint

def generatequote(gpt2_finetune):
    listofquotes = []
    for i in range(0,10):
      quote = gpt2_finetune("",clean_up_tokenization_spaces=True)
      gentext = quote[0]["generated_text"]
      if (len(gentext) != 0) and ("-" not in gentext):
        listofquotes.append(gentext)
      listofquotes = [i.rstrip() for i in listofquotes]

    cleanedQuotes = []
    for i in listofquotes:
      skip = False
      for j in i:
        if (j.isalpha() == False) and (j != " ") and (j != ".") and (j != ",") and (j != "\n"):
          skip = True
          break
      if (skip == False) and (len(i) > 4):
        cleanedQuotes.append(i.replace("\n", ""))

    return(cleanedQuotes[randint(0,len(cleanedQuotes)-1)].title())