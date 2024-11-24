# Sistema de Reconhecimento Facial

Este é um sistema de reconhecimento facial em tempo real usando OpenCV. O sistema permite cadastrar pessoas e reconhecê-las através da webcam.

## 🚀 Funcionalidades

- Cadastro de pessoas através da webcam
- Captura múltiplas fotos para melhor precisão
- Reconhecimento em tempo real
- Indicador de confiança do reconhecimento
- Interface via terminal
- Persistência de dados

## 📋 Pré-requisitos

- Python 3.8+
- Webcam funcional
- Sistema operacional Linux (testado em Ubuntu/Debian)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd reconhecimento-facial
```

2. Crie um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install opencv-python
pip install opencv-contrib-python
```

## 💻 Estrutura do Projeto

```
reconhecimento-facial/
│
├── src/                    # Código fonte
│   ├── __init__.py
│   ├── recognition/        # Módulo de reconhecimento
│   │   ├── __init__.py
│   │   ├── detector.py    # Detector facial
│   │   └── recognizer.py  # Reconhecedor facial
│   │
│   ├── storage/           # Módulo de armazenamento
│   │   ├── __init__.py
│   │   └── data_manager.py
│   │
│   └── ui/                # Interface do usuário
│       ├── __init__.py
│       └── cli.py
│
├── data/                  # Dados salvos
│   ├── models/           # Modelos treinados
│   └── cadastros/        # Fotos de cadastro
│
├── tests/                # Testes
│   └── __init__.py
│
├── requirements.txt      # Dependências
├── README.md
└── main.py              # Ponto de entrada
```

## 🎮 Como Usar

1. Inicie o programa:
```bash
python main.py
```

2. Menu de opções:
   - 1: Cadastrar nova pessoa
   - 2: Iniciar reconhecimento
   - 3: Sair

### Cadastrando uma Pessoa

1. Selecione opção 1
2. Digite o nome da pessoa
3. Pressione 'c' para iniciar a captura
4. Mova levemente o rosto entre as capturas
5. Aguarde a captura das 30 fotos

### Reconhecimento em Tempo Real

1. Selecione opção 2
2. O sistema mostrará:
   - Nome da pessoa reconhecida
   - Nível de confiança
   - Retângulo verde: Pessoa conhecida
   - Retângulo vermelho: Desconhecido

## 📁 Armazenamento

- `modelo_facial.yml`: Modelo treinado
- `nomes.pkl`: Lista de nomes cadastrados
- Diretório `fotos_cadastro/`: Fotos de cadastro

## ⚙️ Configurações

Parâmetros configuráveis em `config.py`:
- Número de fotos para cadastro
- Limiar de confiança
- Tamanho mínimo da face
- Diretórios de dados

## 🔒 Segurança

- Os dados são armazenados localmente
- As fotos são processadas em tempo real
- Não há envio de dados para servidores externos

## 🛠️ Desenvolvimento

Para contribuir:

1. Crie um fork do projeto
2. Crie uma branch para sua feature
```bash
git checkout -b feature/nova-feature
```
3. Commit suas mudanças
```bash
git commit -m 'Adiciona nova feature'
```
4. Push para a branch
```bash
git push origin feature/nova-feature
```
5. Abra um Pull Request

## ✅ Testes

Execute os testes:
```bash
python -m pytest tests/
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Suporte

Para suporte, abra uma issue no repositório ou envie um email para [seu-email].

## 🔄 Atualizações Futuras

- [ ] Interface gráfica
- [ ] Suporte a múltiplas câmeras
- [ ] Exportação de relatórios
- [ ] Reconhecimento por vídeo
- [ ] Integração com sistemas de controle de acesso