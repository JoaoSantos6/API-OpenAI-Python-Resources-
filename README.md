# Projeto: Gerador de README Automatizado

## Descrição

O projeto **buildReadme** é uma solução automatizada desenvolvida para gerar arquivos README em formato markdown com base nos arquivos presentes em um diretório específico. Utilizando a API GPT-3.5/4 da OpenAI, ele gera descrições detalhadas sobre cada arquivo do projeto, facilitando a documentação e fornecendo uma visão clara da arquitetura do sistema.

Esse projeto visa otimizar o processo de documentação de projetos de software, garantindo que cada arquivo seja descrito com precisão e que o README resultante contenha informações valiosas para desenvolvedores e equipes técnicas.

## Funcionalidades

- **Geração Automática de README**: A partir dos arquivos presentes no diretório, o script gera um README detalhado que descreve cada arquivo.
- **Integração com a API GPT**: Utiliza o poder do GPT-3.5/4 para criar descrições textuais de alta qualidade.
- **Exclusão de Arquivos Específicos**: O arquivo responsável por gerar o README não é incluído na documentação.
- **Documentação Personalizada**: O conteúdo gerado é flexível e pode ser ajustado conforme o contexto do projeto.
- **Suporte para múltiplos formatos de arquivo**: O script lida com diferentes tipos de arquivo (como `.py`, `.xml`, `.js`, etc.), fornecendo descrições adequadas para cada um.

## Tecnologias Utilizadas

- **Python 3.10+**: Linguagem de programação utilizada para a construção do script.
- **API GPT-3.5/4 da OpenAI**: Motor de inteligência artificial utilizado para gerar o conteúdo do README.
- **Biblioteca `openai`**: Cliente oficial para a interação com a API da OpenAI.
- **Manipulação de Arquivos e Diretórios**: Utilização de módulos nativos do Python, como `os`, para a exploração recursiva de arquivos.

## Como Funciona

1. **Leitura dos Arquivos**: O script percorre recursivamente o diretório onde está localizado, listando todos os arquivos.
2. **Geração do README**: Com base na lista de arquivos, um prompt é enviado para a API GPT-3.5/4, que retorna um README em markdown, descrevendo cada arquivo individualmente.
3. **Exclusão de Arquivos Específicos**: O script exclui o próprio arquivo Python (`buildReadme.py`) da documentação, para evitar redundância.
4. **Salvamento do README**: O conteúdo gerado é salvo em um arquivo `README.md` no mesmo diretório.

## Como Utilizar

### 1. Instale as Dependências

Antes de executar o script, instale as dependências necessárias:

```bash
pip install openai
```

### 2. Configuração da Chave da API
api_key_file_path = r"C:\caminho\para\seu\arquivo\api_key.txt"

### 3. Execução do Script
python buildReadme.py

### 4. Resultado
O arquivo README.md será criado no mesmo diretório, contendo a documentação detalhada do projeto.

## Possíveis Melhorias
-	Análise de Código Estática: Implementar uma camada de análise de código para fornecer informações mais técnicas, como complexidade ciclomatica, ou dependências entre arquivos.
-	Geração de Diagrama de Arquitetura: Adicionar suporte para geração automática de diagramas visuais de arquitetura do projeto.
-	Customização Avançada: Permitir ao usuário personalizar o nível de detalhes gerado no README, como descrições de métodos/funções em arquivos de código.

## Aplicações no Mercado
- Documentação em Equipes Ágeis: Agiliza o processo de documentação, especialmente em equipes onde o foco é na entrega contínua de valor.
- Integração Contínua: Pode ser utilizado em pipelines de CI/CD para garantir que sempre exista um README atualizado em cada iteração do projeto.
- Onboarding de Desenvolvedores: Facilita o onboarding de novos desenvolvedores em projetos, fornecendo uma visão clara da estrutura do código e do propósito de cada arquivo.