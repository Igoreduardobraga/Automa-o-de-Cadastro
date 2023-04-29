import pyautogui

pyautogui.click(975,610,duration=0.1)

for i in range(0,2):
    pyautogui.click(971,543,duration=0.1)
    pyautogui.write('igor')
    pyautogui.click(970,569,duration=0.1)
    pyautogui.write('1234')
    pyautogui.click(845,606,duration=0.1)


with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        pyautogui.click(620,527,duration=0.1)
        pyautogui.write(produto)

        pyautogui.click(601,561,duration=0.1)
        pyautogui.write(quantidade)

        pyautogui.click(599,589,duration=0.1)
        pyautogui.write(preco)

        pyautogui.click(518,791,duration=0.1)

