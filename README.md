# Testes Grafana

### Requisitos 

para o Arch Linux

```bash
sudo pacman -S docker
sudo systemctl enable docker.service

groupadd docker
sudo usermod -aG docker $USER
```

Neste projeto foi utilizado o dockerfile do repositorio do grafana

```bash
mkdir testes_grafana
cd testes_grafana

git clone https://github.com/grafana/grafana.git

touch docker-compose.yml
```




![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/Captura%20de%20tela%20de%202023-01-22%2020-10-44.png)
