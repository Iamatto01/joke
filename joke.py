import pyjokes

def get_random_joke():
    return pyjokes.get_joke()

if __name__ == "__main__":
    print(get_random_joke())
