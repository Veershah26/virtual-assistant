import wikipedia

def wiki(query):
    start="According to Wikipedia"
    results=wikipedia.summary(query,sentences=2)
    print(start + " " + results)
    
wiki("query")