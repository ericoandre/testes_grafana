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
CREATE TABLE "sensores" (
    "id" integer DEFAULT NOT NULL,
    "temp" real NOT NULL,
    "umid" real NOT NULL,
    "press" real NOT NULL,
    "time" timestamp NOT NULL,
    CONSTRAINT "sensores_pkey" PRIMARY KEY ("id")
);

```

Configurado o data source utilizando o plugin do postegres disponivel como core no grafana.

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/assets/Captura%20de%20tela%20de%202023-01-23%2008-15-52.png)

Configurando a conexão 

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/assets/Captura%20de%20tela%20de%202023-01-23%2008-16-35.png)

Criando um dashboard

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/assets/Captura%20de%20tela%20de%202023-01-23%2008-17-02.png)

Selecione o datsource em seguida a tabela e os campos que sera utilizado no painel e por fim click em salvar.

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/assets/Captura%20de%20tela%20de%202023-01-23%2008-17-56.png)

Dasheboard final

![](https://raw.githubusercontent.com/ericoandre/testes_grafana/main/assets/Captura%20de%20tela%20de%202023-01-22%2020-10-44.png)
