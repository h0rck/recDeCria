# Sistema de Reconhecimento Facial

Sistema de reconhecimento facial em tempo real usando Python e OpenCV. O projeto utiliza princípios SOLID e uma arquitetura limpa para facilitar manutenção e extensibilidade.

## 🚀 Funcionalidades

- Detecção facial em tempo real
- Cadastro de pessoas através da webcam
- Reconhecimento facial em tempo real
- Interface via linha de comando
- Captura múltiplas fotos para melhor precisão

## 📋 Pré-requisitos

- Python 3.8+
- OpenCV
- Webcam funcional
- Sistema operacional Linux (testado em Ubuntu/Debian)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd reconhecimento-facial
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
```

## 💻 Estrutura do Projeto

```
reconhecimento_facial/
│
├── src/
│   ├── domain/           # Interfaces e entidades
│   │   ├── interfaces/   # Contratos do sistema
│   │   └── entities/     # Entidades de domínio
│   │
│   ├── infrastructure/   # Implementações concretas
│   │   └── recognition/  # Implementações OpenCV
│   │
│   └── presentation/     # Interface com usuário
│       ├── cli/         # Interface de linha de comando
│       └── camera/      # Gerenciamento de câmera
│
├── main.py              # Ponto de entrada
└── README.md
```

## 🎮 Como Usar

1. Execute o programa:
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
3. Pressione 'c' para capturar fotos
4. Mova levemente o rosto entre as capturas
5. São necessárias 30 fotos para completar o cadastro
6. Pressione 'q' para cancelar

### Reconhecimento em Tempo Real

1. Selecione opção 2
2. O sistema mostrará:
   - Retângulo verde: Pessoa reconhecida
   - Retângulo vermelho: Pessoa desconhecida
   - Nome da pessoa (se reconhecida)
3. Pressione 'q' para voltar ao menu

## 🏗️ Arquitetura

O projeto segue princípios SOLID e Clean Architecture:

1. **Domain**: 
   - Interfaces e contratos do sistema
   - Independente de implementações

2. **Infrastructure**: 
   - Implementações concretas das interfaces
   - Adaptadores para bibliotecas externas

3. **Presentation**: 
   - Interface com usuário
   - Gerenciamento de câmera

## 🤝 Contribuindo

Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como implementar novas funcionalidades.

## 📝 Licença

Este projeto está sob a licença MIT.

## 🐛 Problemas Conhecidos

- A precisão do reconhecimento depende da qualidade das fotos de cadastro
- Iluminação pode afetar o reconhecimento
- Performance depende do hardware

## 📞 Suporte

Para suporte, abra uma issue no repositório.