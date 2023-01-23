# Testes Grafana

Configuração do docker para o Arch Linux

```bash
sudo pacman -S docker
sudo systemctl enable docker.service

groupadd docker
sudo usermod -aG docker $USER
```

Neste projeto foi utilizado o dockerfile do repositório do grafana juntamente com banco de dados postgres. Tem um diretório com um script python e um base de dados de sensores, ele serve para simular o envio de dados dos sensores de temperatura, umidade e pressão. 

```bash
mkdir testes_grafana
cd testes_grafana

git clone https://github.com/grafana/grafana.git

docker-composer -d up  
```

No postegres foi criado uma tabela para armazenar os dados das leituras dos sensores de temperatura, umidade e pressão, tendo mais um atributo que é o time que armazena um timestemp do momento da leitora dos sensores. 


```sql

```


Foi configurado o data source utilizando o plugin do postegres disponivel como core no grafana.


Dasheboard final

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/Captura%20de%20tela%20de%202023-01-22%2020-10-44.png)
