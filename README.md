Descrição da Script: Geração e Salvamento de Dígitos Aleatórios

Objetivo:
A script em Python tem o objetivo de gerar números e letras aleatórias de 4, 6, 8 e 16 dígitos, criando uma estrutura de pastas organizada para salvar os arquivos gerados. A cada ciclo, um código aleatório de tamanho aleatório é criado e salvo em um arquivo de texto correspondente ao seu tamanho em uma pasta separada.

Funcionalidades Principais:

    Geração de Códigos Aleatórios: A função generate_random_string(length) é responsável por gerar sequências aleatórias de letras maiúsculas e dígitos, com o tamanho especificado.

    Criação de Diretórios: A função create_directory_if_not_exists(directory) é utilizada para verificar se um diretório existe e, caso não exista, criá-lo. Essa função é responsável por criar a estrutura de pastas necessária para armazenar os arquivos de saída.

    Salvamento dos Códigos: A função save_to_file(size, code, destination_path) é responsável por salvar os códigos gerados nos arquivos de texto apropriados dentro das pastas correspondentes. Ela cria a pasta para o tamanho do código e adiciona o código em um arquivo "{size}strings.txt".

    Loop Infinito: O programa entra em um loop infinito na função main(), onde gera um novo código a cada iteração do loop e salva-o em seu respectivo arquivo.

Caminho de Saída:
O caminho de saída padrão é "/home/kali/Desktop/Generated-Digits/". A pasta "Generated-Digits" é criada no diretório "/home/kali/Desktop/" para armazenar os códigos gerados em subpastas organizadas por tamanhos (4, 6, 8 e 16 dígitos).

Execução Infinita:
A script irá executar infinitamente, gerando códigos aleatórios em intervalos de 1 segundo. Os códigos serão salvos em pastas separadas de acordo com seus tamanhos.

Uso:
Para executar a script, você pode copiar e colar o código em um arquivo com extensão ".py" e, em seguida, executá-lo usando o Python. Certifique-se de ter as permissões adequadas para criar pastas e salvar arquivos no diretório de saída especificado. A script continuará a ser executada até ser interrompida manualmente (por exemplo, pressionando Ctrl + C no terminal).

Observação:
Lembre-se de que a script gera códigos totalmente aleatórios, e não há garantia de unicidade ou validade dos códigos gerados. A finalidade é apenas demonstrar a geração aleatória e o salvamento em arquivos de texto organizados em pastas.
