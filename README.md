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
