#! /usr/bin/python3
#-*- coding:utf-8 -*-
def main():
    text = input('easy@box$ ')
    for ban in ['eval', 'exec', 'import','read', 'system', 'write','os','read','open', '"', '__']:
        if ban in text:
            print("Bad guy!")
            return;
    else:
        exec(text)
if __name__ == "__main__":
    main()
