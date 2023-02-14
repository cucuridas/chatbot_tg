import sys
import asyncio

sys.path.append("/Users/cucuridas/Desktop/chatbot_tg")
sys.path.append("/Users/cucuridas/Desktop/chatbot_tg/chatbot_tg")


from app.util.elasticsearch import Match, Document


if __name__ == "__main__":
    # print(Match().match("tgday"))
    # value = Document().getDocument(
    #     "tgday",
    #     "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kMWQ2YTFhZS0xOTE4LTRiMWUtODU5Yy0zYmNmZjU2NDczNmI",
    # )

    # print(value)

    asyncio.run(Match().serarch("tgday"))
