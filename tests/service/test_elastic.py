import sys

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")


from chatbot_tg.service.elasticsearch import Match

if __name__ == "__main__":
    print(Match().match("tgday"))
