# Lanchonetes
API de lanchonetes

# Build
1. instalar o virtualenv, pip e dependecias. 
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv .venv
source .venv/bin-activate
pip3 install -r requirements.txt
```
2. criar um super usuário para acessar o django admin
```
python3 manage.py createsuperuser
```
3. Ligando aplicação
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
<br>

# Rotas
1. Informações da API
```
127.0.0.1:8000/
```
2. Listar todas as lanchonetes
```
127.0.0.1:8000/lanchonete/
```
3. Buscar uma lanchonete pelo nome
```
127.0.0.1:8000/lanchonete/<Nome da Lanchonete>
```
4. Buscar lanchonetes por estado
```
127.0.0.1:8000/estado/<sigla estado>
```
5. Buscar lanchonetes por estado e cidade
```
127.0.0.1:8000/estado/<sigla estado>/cidade/<nome cidade>/
```
6. Buscar pratos por valor maximo
```
127.0.0.1:8000/max-preco/<valor>/
```
7. Buscar pratos por estado, cidade e valor máximo
```
127.0.0.1:8000/estado/<sigla estado>/cidade/<nome cidade>/max-preco/<valor>
```
