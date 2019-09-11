import itertools

def get_user_input():
    for i in itertools.count():
        yield i, input("[{}] Input : ".format(i))

def main():
    for i, user_input in get_user_input():
        print(i, user_input)

    
if __name__ == '__main__':
    main()