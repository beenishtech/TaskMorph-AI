from taskmorph.graph import build_graph


def main():
    app = build_graph()
    text = input("Enter your tasks: ")
    result = app.invoke({"user_input": text})
    print()
    print(result["output"])


if __name__ == "__main__":
    main()