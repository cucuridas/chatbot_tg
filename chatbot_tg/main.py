import uvicorn


def main():
    uvicorn.run(app="core.server:app")


if __name__ == "__main__":
    main()
