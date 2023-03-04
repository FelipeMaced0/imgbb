# Imgbb_Uploader

![GitHub repo size](https://img.shields.io/github/repo-size/FelipeMaced0/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/FelipeMaced0/README-template?style=for-the-badge)


## What is this all about?

This is a script to batch-upload images inside a directory to [imgbb](https://imgbb.com) cloud.
It will write the URLs returned by the API to a spreadsheet.

## 💻 Pre-requisites

Verify if you have Python 3.8.* installed. If not, checkout these resources:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Be sure to have correct version of [` Python 3`](https://www.python.org/downloads/)
* Create an account at [imgbb](https://imgbb.com) and get one API_KEY.
* Create a new file called .env and write your API_KEY on it. See the Example bellow

### Installing Dependencies 
Run on terminal, inside imgbb directory

    pip install -r requirements.txt

## ⚙️ Config of .env file
Inside your .env file type the following

⚠️ NO SPACES BEFORE OR AFTER THE = SIGN

    API_KEY=YOUR_API_KEY

## ☕ Using 
Before any execution

Examples of the arguments of send_imgs function

`send_imgs(full_folder_path:str, full_spread_sheet_path:str)`

| OS        |          full_folder_path         |        full_spread_sheet_path        |
|:--------- | --------------------------------- | ------------------------------------ |
| Linux     | /home/user1/Documents/photos/     | /home/user1/Documents/urls.xlsx      | 
| Windows   | C:\Users\user1\Documents\photos   | C:\Users\user1\Documents\urls.xlsx   |

### To be able to launch:
Inside the imbb directory type the following on the terminal

| Plataform |        Comand         |
| --------- | --------------------- |
| Windows   |`python sendImagens.py`|
| Linux     |`python3 sendImages.py`|


### The Following messages should appear on your terminal:

#### Linux
```bash
demon_slayer UPLOADED SUCCESSFULLY!!!

FULL_PATH: /home/<user>/<Directory>/demon_slayer.jpg
URL: https://i.ibb.co/StX4kjY/demon-slayer.jpg

```

#### Windows
```cmd
demon_slayer UPLOADED SUCCESSFULLY!!!

FULL_PATH: C:\Users\<user>/<Directory>/demon_slayer.jpg
URL: https://i.ibb.co/StX4kjY/demon-slayer.jpg

```

<br><br><br>

# Português

## 💻 Pré-requisitos

Antes de começar, verifique se você atende aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Você instalou a versão 3.8.* [` Python 3`](https://www.python.org/downloads/)
* Criar uma conta [imgbb](https://imgbb.com) and get one API_KEY.
* Criar um arquivo chamado .env e colocar sua API_KEY. Veja o exemplo abaixo

### Instalando as dependências 
    pip install -r requirements.txt

## ⚙️ Configuração do arquivo .env: 

⚠️ SEM EXPAÇOS ANTES OU DEPOIS DO SINAL DE =

    API_KEY=YOUR_API_KEY

   
## ☕ Usando 

### Antes de Executar

Examplos dos argumentos da função send_imgs

`send_imgs(full_folder_path:str, full_spread_sheet_path:str)`

| OS        |          full_folder_path         |        full_spread_sheet_path        |
|:--------- | --------------------------------- | ------------------------------------ |
| Linux     | /home/user1/Documents/photos/     | /home/user1/Documents/urls.xlsx      | 
| Windows   | C:\Users\user1\Documents\photos   | C:\Users\user1\Documents\urls.xlsx   |

### Para rodar o script:
    No terminal, dentro do diretório imgbb digite:

| Plaforma  |        Comando        |
| --------- | --------------------- |
| Windows   |`python sendImagens.py`|
| Linux     |`python3 sendImages.py`|

### A seguinte mensagem deverá aparecer no terminal:

#### Linux
```bash
demon_slayer UPLOADED SUCCESSFULLY!!!

FULL_PATH: /home/<user>/<Directory>/demon_slayer.jpg
URL: https://i.ibb.co/StX4kjY/demon-slayer.jpg

```

#### Windows
```cmd
demon_slayer UPLOADED SUCCESSFULLY!!!

FULL_PATH: C:\Users\<user>/<Directory>/demon_slayer.jpg
URL: https://i.ibb.co/StX4kjY/demon-slayer.jpg

```

[⬆ Voltar ao topo](#Imgbb_Uploader)<br>
