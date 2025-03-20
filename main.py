from pynput import keyboard
import numpy as np


hard_keys = {
    'q': ['-1', '', ''],
    'w': ['-2', '', ''],
    'e': ['-3', '', ''],
    'r': ['-4', '', ''],
    't': ['-5', '', ''],
    'y': ['-6', '', ''],
    'u': ['-7', '', ''],
    'i': ['-8', '', ''],
    'o': ['-9', '', ''],
    'p': ['-10', '', ''],
    '[': ['-11', '', ''],

    'a': ['', '-1', ''],
    's': ['', '-2', ''],
    'd': ['', '-3', ''],
    'f': ['', '-4', ''],
    'g': ['', '-5', ''],
    'h': ['', '-6', ''],
    'j': ['', '-7', ''],
    'k': ['', '-8', ''],
    'l': ['', '-9', ''],
    ';': ['', '-10', ''],
    '\\': ['', '-11', ''],

    'z': ['', '', '-1'],
    'x': ['', '', '-2'],
    'c': ['', '', '-3'],
    'v': ['', '', '-4'],
    'b': ['', '', '-5'],
    'n': ['', '', '-6'],
    'm': ['', '', '-7'],
    ',': ['', '', '-8'],
    '.': ['', '', '-9'],
    '/': ['', '', '-10'],

    'Q': ['1', '', ''],
    'W': ['2', '', ''],
    'E': ['3', '', ''],
    'R': ['4', '', ''],
    'T': ['5', '', ''],
    'Y': ['6', '', ''],
    'U': ['7', '', ''],
    'I': ['8', '', ''],
    'O': ['9', '', ''],
    'P': ['10', '', ''],
    '{': ['11', '', ''],

    'A': ['', '1', ''],
    'S': ['', '2', ''],
    'D': ['', '3', ''],
    'F': ['', '4', ''],
    'G': ['', '5', ''],
    'H': ['', '6', ''],
    'J': ['', '7', ''],
    'K': ['', '8', ''],
    'L': ['', '9', ''],
    ':': ['', '10', ''],
    '|': ['', '11', ''],

    'Z': ['', '', '1'],
    'X': ['', '', '2'],
    'C': ['', '', '3'],
    'V': ['', '', '4'],
    'B': ['', '', '5'],
    'N': ['', '', '6'],
    'M': ['', '', '7'],
    '<': ['', '', '8'],
    '>': ['', '', '9'],
    '?': ['', '', '10'],

    ' ': ['', '', '']

}

keys = []


def on_press(key):
    try:
        # print('Tecla alfanumérica {0} presionada'.format(key.char))
        # print(key.char)
        print(hard_keys[key.char])
        keys.append(hard_keys[key.char])
        # if format(key.char) == 'Key.backspace':
        #     print("Deleting")
    except AttributeError:
        print('Tecla especial {0} presionada'.format(key))


def on_release(key):
    # print('{0} liberada'.format(key))
    if key == keyboard.Key.esc:
        # Detener el listener
        print(keys)
        matrix = np.array(keys)
        matrix_transposed = matrix.T
        print('Guardando en archivo tablatura.csv')
        np.savetxt('tablatura.csv', matrix_transposed, delimiter=',', fmt='%s')
        return False
    if key == keyboard.Key.backspace:
        keys.pop()
    if key == keyboard.Key.space:
        keys.append(hard_keys[' '])
    if key == keyboard.Key.ctrl_l:
        keys.append(['0', '0', '0'])
        print(['0', '0', '0'])


def main():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()