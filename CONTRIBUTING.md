# Guia de Contribuição

Este documento descreve como implementar novas funcionalidades em cada módulo do sistema.

## 🏗️ Estrutura de Módulos

### 1. Domain (`src/domain/`)

#### Interfaces (`interfaces/`)
Para adicionar uma nova interface:

1. Crie um novo arquivo em `src/domain/interfaces/`
2. Use `ABC` e `@abstractmethod` para definir contratos
3. Atualize `__init__.py` para exportar a nova interface

Exemplo:
```python
# novo_servico.py
from abc import ABC, abstractmethod

class NovoServico(ABC):
    @abstractmethod
    def executar(self) -> None:
        pass
```

#### Entidades (`entities/`)
Para adicionar uma nova entidade:

1. Crie um novo arquivo em `src/domain/entities/`
2. Use `@dataclass` para definir entidades
3. Atualize `__init__.py` para exportar a nova entidade

Exemplo:
```python
# nova_entidade.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class NovaEntidade:
    id: str
    created_at: datetime
```

### 2. Infrastructure (`src/infrastructure/`)

#### Recognition (`recognition/`)
Para adicionar uma nova implementação de reconhecimento:

1. Crie um novo arquivo em `src/infrastructure/recognition/`
2. Implemente as interfaces necessárias
3. Atualize `__init__.py` para exportar a nova classe

Exemplo:
```python
# novo_detector.py
from ...domain.interfaces.face_detector import FaceDetector

class NovoDetector(FaceDetector):
    def detect_faces(self, image):
        # Implementação
        pass
```

### 3. Presentation (`src/presentation/`)

#### CLI (`cli/`)
Para adicionar novos comandos:

1. Modifique `main_menu.py`
2. Adicione novos métodos à classe `MainMenu`
3. Atualize o menu principal

Exemplo:
```python
def novo_comando(self):
    print("Executando novo comando...")
    # Implementação
```

#### Camera (`camera/`)
Para adicionar novas funcionalidades de câmera:

1. Modifique `camera_manager.py`
2. Adicione novos métodos à classe `CameraManager`

Exemplo:
```python
def capturar_video(self, duracao: int):
    # Implementação
    pass
```

## 🔄 Fluxo de Trabalho

1. **Crie uma branch**:
```bash
git checkout -b feature/nova-funcionalidade
```

2. **Implemente seguindo os padrões**:
- Use tipagem estática
- Adicione docstrings
- Siga PEP 8

3. **Teste sua implementação**

4. **Faça commit**:
```bash
git commit -m "Adiciona nova funcionalidade"
```

5. **Crie um Pull Request**

## ✅ Checklist de Implementação

- [ ] Segue princípios SOLID
- [ ] Interfaces bem definidas
- [ ] Documentação atualizada
- [ ] Código tipado
- [ ] Testes implementados
- [ ] Sem dependências circulares

## 📝 Convenções de Código

1. **Nomes de Classes**:
- PascalCase para classes
- Sufixo indicando o tipo (Interface, Service, Manager)

2. **Nomes de Métodos**:
- snake_case para métodos
- Verbos indicando ação

3. **Documentação**:
- Docstrings em todos os módulos
- Tipos explícitos em parâmetros

## 🎯 Áreas para Contribuição

1. **Novos Detectores**:
- Implementações usando outras bibliotecas
- Melhorias de performance

2. **Novas Interfaces**:
- GUI usando PyQt ou Tkinter
- Interface Web

3. **Armazenamento**:
- Persistência em banco de dados
- Armazenamento em nuvem

4. **Melhorias**:
- Sistema de logging
- Configurações via arquivo
- Testes automatizados

## ⚠️ Observações

- Mantenha a arquitetura limpa
- Evite acoplamento forte
- Documente alterações
- Teste antes de submeter

## 🤝 Suporte

Para dúvidas sobre implementação:
1. Abra uma issue
2. Descreva seu caso de uso
3. Aguarde feedback da equipe