import uvicorn
from service.webhook import WebexHook


def main():
    WebexHook().addHook()
    uvicorn.run(app="core.server:app")


if __name__ == "__main__":
    main()
