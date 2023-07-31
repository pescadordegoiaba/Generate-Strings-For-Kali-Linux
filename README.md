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

Indian:
उद्देश्य:
पायथन स्क्रिप्ट का उद्देश्य विभिन्न आकारों में 4, 6, 8 और 16 अंकों के बिना हिंदी वर्णमाला, लघु वर्णमाला और संख्याओं के साथ यादृच्छिक कोड उत्पन्न करना है। ये कोड टेक्स्ट फ़ाइलों में सहेजे जाते हैं, जिन्हें आकार के अनुसार संरचित किया गया है और उत्पन्न समय पर आधारित है। स्क्रिप्ट एक अनंत लूप में चलती रहती है, जिसमें हर लूप इटरेशन में एक नया कोड उत्पन्न किया जाता है और उसे संबंधित फ़ाइलों में सहेज दिया जाता है।

मुख्य विशेषताएँ:
यादृच्छिक कोड उत्पन्न करना: फ़ंक्शन generate_random_string(length) को अपडेट किया गया है ताकि उत्पन्न यादृच्छिक अनुक्रम में हिंदी वर्णमाला, लघु वर्णमाला और संख्याएँ शामिल हों।

निर्देशिका बनाना: फ़ंक्शन create_directory_if_not_exists(directory) नई निर्देशिका बनाता है जो उत्पन्न किए गए कोडों को संग्रहीत करने के लिए आवश्यक होती है, यदि यह पहले से मौजूद नहीं है।

कोड को सहेजना: फ़ंक्शन save_to_file(size, code, destination_path) नई फ़ाइलों में उत्पन्न किए गए कोडों को सहेजता है जो संगठित निर्देशिकाओं में होते हैं। फ़ाइलों का नाम उत्पन्न किए गए कोडों के आकार के अनुसार नामित होते हैं।

अनंत लूप: कार्यक्रम फ़ंक्शन में एक अनंत लूप में प्रवेश करता है, जिसमें प्रत्येक लूप इटरेशन में एक नया कोड उत्पन्न किया जाता है और संबंधित फ़ाइलों में सहेज दिया जाता है।

आउटपुट पथ:
डिफ़ॉल्ट आउटपुट पथ है "/home/kali/Desktop/Generated-Digits/"। उत्पन्न किए गए कोडों को संगठित उपनिर्देशिकाओं में संग्रहीत करने के लिए "/home/kali/Desktop/" निर्देशिका में "Generated-Digits" नामक फ़ोल्डर बनाया जाता है। उपनिर्देशिकाएँ आकार के अनुसार (4, 6, 8 और 16 अंक) अलग-अलग फ़ोल्डरों में संरचित होंगी।

अनंत निष्पादन:
स्क्रिप्ट अनंत निष्पादन करेगी, हर 1 सेकंड के अंतराल में यादृच्छिक कोड उत्पन्न करते हुए। कोड उनके आकार के अनुसार अलग-अलग फ़ोल्डरों में सहेजे जाएंगे।

कोडों का विविधता:
उत्पन्न किए गए कोड पूरी तरह से यादृच्छिक होते हैं और हिंदी वर्णमाला, लघु वर्णमाला, और संख्याएँ शामिल होते हैं, जिससे वे विविधता और जटिलता प्रदान करते हैं।

ध्यान दें:
सुनिश्चित करें कि निर्देशिका "/home/kali/Desktop/Generated-Digits/" मौजूद है और उसमें लेखन की अनुमति है, ताकि स्क्रिप्ट उस स्थान पर सही ढंग से फ़ाइलें सहेज सके। स्क्रिप्ट का उद्देश्य केवल यादृच्छिक उत्पन्न करने और फ़ोल्डरों में टेक्स्ट फ़ाइलें सहेजने का दिखाना है।

Russian:
Цель:
Скрипт на языке Python предназначен для генерации случайных кодов с использованием заглавных и строчных букв, а также цифр, длиной 4, 6, 8 и 16 символов. Эти коды сохраняются в текстовых файлах в структуре папок, организованных по размеру и основанных на времени создания. Скрипт продолжает выполняться в бесконечном цикле, сохраняя коды в каталоге "/home/kali/Desktop/Generated-Digits/".

Основные функции:

css

Генерация случайных кодов: Функция generate_random_string(length) была обновлена, чтобы включить в сгенерированную случайную последовательность заглавные и строчные буквы, а также цифры.

Создание каталогов: Функция create_directory_if_not_exists(directory) создает необходимую структуру папок для сохранения сгенерированных кодов, если она не существует.

Сохранение кодов: Функция save_to_file(size, code, destination_path) сохраняет сгенерированные коды в текстовых файлах в организованных папках. Файлы названы в соответствии с размером сгенерированных кодов.

Бесконечный цикл: Программа входит в бесконечный цикл в функции main(), где на каждой итерации цикла создается новый код и сохраняется в соответствующие файлы.

Выходной путь:
Стандартный выходной путь - "/home/kali/Desktop/Generated-Digits/". Папка "Generated-Digits" создается в каталоге "/home/kali/Desktop/" для хранения сгенерированных кодов в подпапках, организованных по размерам (4, 6, 8 и 16 символов).

Бесконечное выполнение:
Скрипт будет выполняться бесконечно, генерируя случайные коды через интервалы в 1 секунду. Коды будут сохранены в отдельных папках в соответствии с их размерами.

Разнообразие кодов:
Сгенерированные коды полностью случайны и включают заглавные и строчные буквы, а также цифры, обеспечивая разнообразие и сложность.

Примечание:
Убедитесь, что каталог "/home/kali/Desktop/Generated-Digits/" существует и имеет права на запись, чтобы скрипт мог правильно сохранять файлы в этом месте. Цель скрипта - только продемонстрировать случайную генерацию и сохранение в текстовые файлы, организованные в папках.

Translated By Translator Google
