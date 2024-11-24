# Sistema de Reconhecimento Facial

Este é um sistema de reconhecimento facial desenvolvido em Python para monitoramento de câmeras em ambiente escolar. O sistema permite cadastrar pessoas e realizar reconhecimento facial em tempo real através de câmeras conectadas.

## Pré-requisitos

- Python 3.8 ou superior
- Sistema operacional Linux (testado em Ubuntu/Debian)
- Câmera conectada ao sistema

## Instalação

### 1. Instalar dependências do sistema

```bash
# Instalar Python e ferramentas de desenvolvimento
sudo apt install python3-full
sudo apt-get update
sudo apt-get install -y python3-dev
sudo apt-get install -y cmake
sudo apt-get install -y libopenblas-dev
sudo apt-get install -y liblapack-dev 
sudo apt-get install -y libjpeg-dev
sudo apt-get install -y pkg-config
sudo apt-get install -y build-essential
```

### 2. Configurar o ambiente virtual

```bash
# Criar pasta do projeto
mkdir reconhecimento_facial
cd reconhecimento_facial

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Atualizar pip
pip install --upgrade pip
```

### 3. Instalar bibliotecas Python

```bash
pip install opencv-python
pip install face-recognition
pip install numpy
```

## Estrutura do Projeto

```
reconhecimento_facial/
│
├── venv/                  # Ambiente virtual
├── fotos/                 # Pasta para fotos de cadastro
├── dados_faciais/         # Pasta onde serão salvos os dados
├── banco_dados_facial.py  # Gerenciamento do banco de dados
├── processador_imagem.py  # Processamento de imagens
├── visualizador.py        # Interface visual
├── sistema_reconhecimento.py  # Sistema principal
└── exemplo_uso.py         # Exemplo de utilização
```

## Como Usar

### 1. Ativar o ambiente virtual

Sempre que for usar o sistema, primeiro ative o ambiente virtual:

```bash
cd reconhecimento_facial
source venv/bin/activate
```

### 2. Executar o sistema

```python
from sistema_reconhecimento import SistemaReconhecimento

# Criar uma instância do sistema
sistema = SistemaReconhecimento()

# Cadastrar uma nova pessoa
sistema.cadastrar_pessoa("Nome da Pessoa", "fotos/pessoa.jpg")

# Iniciar o reconhecimento pela câmera
sistema.iniciar_camera()
```

### 3. Comandos durante a execução

- Pressione 'q' para sair do modo de câmera
- Os resultados do reconhecimento são mostrados em tempo real na tela

## Considerações Importantes

1. **Qualidade das fotos de cadastro:**
   - Use fotos com boa iluminação
   - A foto deve conter apenas uma face
   - A face deve estar clara e bem visível

2. **Performance:**
   - O desempenho depende do hardware disponível
   - Processadores mais potentes terão melhor performance
   - A qualidade da câmera afeta a precisão do reconhecimento

3. **Segurança:**
   - Mantenha o banco de dados de faces em local seguro
   - Implemente controle de acesso ao sistema
   - Siga as regulamentações de privacidade (LGPD)

## Solução de Problemas

### Erro ao instalar pacotes
Se encontrar erro de "externally-managed-environment", certifique-se de:
1. Estar usando o ambiente virtual
2. Ter ativado o ambiente virtual corretamente
3. Ter instalado python3-full

### Câmera não detectada
1. Verifique se a câmera está conectada
2. Teste a câmera com outro software
3. Verifique as permissões do usuário

### Baixa precisão no reconhecimento
1. Melhore a iluminação do ambiente
2. Use fotos de cadastro com melhor qualidade
3. Ajuste a posição da câmera

## Desativando o ambiente virtual

Quando terminar de usar o sistema:

```bash
deactivate
```

## Suporte

Para problemas e sugestões, por favor abra uma issue no repositório do projeto.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.