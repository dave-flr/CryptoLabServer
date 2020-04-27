# CryptoLab Encoder 

Herramienta de encriptado online.

## Hashes
 - MD5
 - SHA-1
 - SHA-256
 - SHA-512

![## Lifetimes of cryptographic hash functions](https://i.imgur.com/KyiiqYd.png)

> [Lifetimes of cryptographic hash functions](https://valerieaurora.org/hash.html)

## Malespin Code.

Algoritmo simple de sustitución mono alfabética.

[![](https://mermaid.ink/img/eyJjb2RlIjoiXG5zdGF0ZURpYWdyYW1cbkEgLS0-IEUgXG5JIC0tPiBPIFxuQiAtLT4gVCBcbkYgLS0-IEcgXG5QIC0tPiBNIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiXG5zdGF0ZURpYWdyYW1cbkEgLS0-IEUgXG5JIC0tPiBPIFxuQiAtLT4gVCBcbkYgLS0-IEcgXG5QIC0tPiBNIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

## X_crypt

Algoritmo simple de sustitución mono alfabética.


       def xcrypt(text):
        counter = 0
        list_str = list(text)
        for letter in text:
            space = 0
            for key, value in xcrypt_code.items():
                if letter == key or letter.upper() == key.upper():
                    list_str[counter] = value
                    break
                elif letter == value or letter.upper() == value.upper():
                    list_str[counter] = key
                    break
                space += 1
            counter += 1
        return ''.join(list_str)
 

Descripción:

Para cifrar un texto cualquiera usando Python:

 - Se convierte el texto a un array de caracteres.
 - En un ciclo de compara cada de una de las letras con un diccionario.
 - La primer letra se compara en otro ciclo interno con las claves y los valores del diccionario.
 - Si la letra es igual a la clave se intercambia por el valor de la clave.
 - Si la letra es igual al valor, se intercambia por el nombre de la clave.
 - Se construye un nuevo array con los valores intercambiados.
 - Se obtiene el resultado uniendo ese nuevo array en una cadena común y corriente.
