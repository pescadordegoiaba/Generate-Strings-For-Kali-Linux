Portugues Brasileiro:
Objetivo:
A script em Python tem o objetivo de gerar códigos aleatórios com letras maiúsculas, minúsculas e dígitos, nos tamanhos de 4, 6, 8 e 16 dígitos. Esses códigos são salvos em arquivos de texto dentro de uma estrutura de pastas organizadas por tamanho e com base no horário de geração. A script continua a ser executada em um loop infinito, salvando os códigos no diretório "/home/kali/Desktop/Generated-Digits/".

Funcionalidades Principais:

    Geração de Códigos Aleatórios: A função generate_random_string(length) foi atualizada para incluir letras maiúsculas, minúsculas e dígitos na sequência aleatória gerada.

    Criação de Diretórios: A função create_directory_if_not_exists(directory) cria a estrutura de pastas necessária para armazenar os códigos gerados, caso não exista.

    Salvamento dos Códigos: A função save_to_file(size, code, destination_path) salva os códigos gerados em arquivos de texto dentro de pastas organizadas. Os arquivos são nomeados de acordo com o tamanho dos códigos gerados.

    Loop Infinito: O programa entra em um loop infinito na função main(), onde a cada iteração do loop, é gerado um novo código e salvo nos arquivos correspondentes.

Caminho de Saída:
O caminho de saída padrão é "/home/kali/Desktop/Generated-Digits/". A pasta "Generated-Digits" é criada no diretório "/home/kali/Desktop/" para armazenar os códigos gerados em subpastas organizadas por tamanhos (4, 6, 8 e 16 dígitos).

Execução Infinita:
A script irá executar infinitamente, gerando códigos aleatórios em intervalos de 1 segundo. Os códigos serão salvos em pastas separadas de acordo com seus tamanhos.

Diversidade dos Códigos:
Os códigos gerados são totalmente aleatórios e incluem letras maiúsculas, minúsculas e dígitos, proporcionando diversidade e complexidade.

Observação:
Certifique-se de que o diretório "/home/kali/Desktop/Generated-Digits/" exista e tenha permissões de escrita para que o script possa salvar os arquivos corretamente nesse local. A finalidade da script é apenas demonstrar a geração aleatória e o salvamento em arquivos de texto organizados em pastas.


English:

Objective:
The Python script aims to generate random codes consisting of uppercase letters, lowercase letters, and digits with lengths of 4, 6, 8, and 16 characters. These codes are saved in text files within a folder structure organized by size and based on the generation time. The script continues to run in an infinite loop, saving the codes in the directory "/home/kali/Desktop/Generated-Digits/".

Key Features:
Random Code Generation: The function generate_random_string(length) has been updated to include uppercase letters, lowercase letters, and digits in the generated random sequence.

Directory Creation: The function create_directory_if_not_exists(directory) creates the necessary folder structure to store the generated codes if it does not already exist.

Code Saving: The function save_to_file(size, code, destination_path) saves the generated codes in text files within organized folders. The files are named according to the size of the generated codes.

Infinite Loop: The program enters an infinite loop in the function main(), where in each iteration of the loop, a new code is generated and saved in the corresponding files.

Output Path:
The default output path is "/home/kali/Desktop/Generated-Digits/". The folder "Generated-Digits" is created in the directory "/home/kali/Desktop/" to store the generated codes in subfolders organized by sizes (4, 6, 8, and 16 digits).

Infinite Execution:
The script will execute indefinitely, generating random codes at intervals of 1 second. The codes will be saved in separate folders according to their sizes.

Diversity of Codes:
The generated codes are completely random and include uppercase letters, lowercase letters, and digits, providing diversity and complexity.

Note:
Make sure that the directory "/home/kali/Desktop/Generated-Digits/" exists and has write permissions so that the script can save the files correctly in that location. The purpose of the script is only to demonstrate random generation and saving to text files organized in folders.
