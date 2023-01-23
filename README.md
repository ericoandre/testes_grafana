# Testes Grafana

Requisitos para o Arch Linux

```bash
sudo pacman -S docker
sudo systemctl enable docker.service

groupadd docker
sudo usermod -aG docker $USER
```

Neste projeto foi utilizado o dockerfile do repositorio do grafana juntamente com baco de dados postgres. Tem uma diretorio com um script python e um base de dados de sensore, ele serve para simular o envio de dados dos sensores de temperatura umidade e pressão. 

```bash
mkdir testes_grafana
cd testes_grafana

git clone https://github.com/grafana/grafana.git

touch docker-compose.yml
```

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/Captura%20de%20tela%20de%202023-01-22%2020-10-44.png)
