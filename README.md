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
Sair 
```bash
deactivate 
```

3. Instale as dependências:
```bash
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
```

4. Configure o PYTHONPATH (necessário para Linux):
```bash
export PYTHONPATH=$(pwd)/src:$PYTHONPATH
```
5. run 
```bash
python main.py 
```
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
