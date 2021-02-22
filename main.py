#!/usr/bin/env python
# coding=utf-8

import train as t

def main():
    anwser = input('Am I biatch? ')
    if anwser:
        print('Yah, exactly you\'re biatch!')
        t.train(1 / len(anwser))

if __name__ == "__main__":
    main()
