import pyautogui as py, sys

n = int(py.prompt(text="Quantos elementos deseja adicionar ao array? "))

array = []

for i in range(n):
    elemento = py.prompt(text="digite o elemento")
    array.append(elemento)

print("Array final:", array)