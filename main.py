import pywhatkit
import sys

def argmt_rtn():
    try:
        text = sys.argv[1:]
        value = ""
        for t in text:
            value = value + t +" " 
    except IndexError:
        print("Error")
    return value


if __name__ == '__main__':


    text = argmt_rtn()
    print("Playing "+ text)
    pywhatkit.playonyt(text)
