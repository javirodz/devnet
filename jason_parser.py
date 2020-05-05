import json

def main():
    with open('jason.json', 'r') as jsonFile:
        #load jason file
        myJasonFile = json.load(jsonFile)
    print(myJasonFile)


if __name__ == "__main__":
    # calling main function
    main()
