from network import is_online
from ai_core import offline_ai

def online_ai(msg):
    return "Online AI: "+msg

def hybrid_ai(msg):
    if is_online():
        try:
            return online_ai(msg)
        except:
            return offline_ai(msg)
    return offline_ai(msg)
