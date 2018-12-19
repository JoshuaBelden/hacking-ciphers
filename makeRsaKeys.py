import random, sys, os, rabinMiller, cryptomath

def main():
    print('Making key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('Key files made.')

def generateKey(keySize):
    print('Generating p prime...')
    