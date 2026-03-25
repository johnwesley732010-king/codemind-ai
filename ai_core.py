import requests
def offline_ai(msg):
    try:
        r=requests.post("http://localhost:11434/api/generate",json={"model":"llama3","prompt":msg,"stream":False})
        return r.json()["response"]
    except:
        return "Offline AI: "+msg
