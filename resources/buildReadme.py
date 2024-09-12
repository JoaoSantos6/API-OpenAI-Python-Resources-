import os
from openai import OpenAI

# Função para ler a chave da API de um arquivo txt
def read_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Função para listar os arquivos recursivamente
def list_files(directory):
    files_list = []
    for root, _, files in os.walk(directory):
        for file in files :
            file_path = os.path.join(root, file)
            files_list.append(file_path)
    return files_list

# Função para gerar o conteúdo do README usando GPT-4 ou GPT-3.5
def generate_readme_content(file_list, api_key):
    # Crie um prompt base com a lista dos arquivos
    prompt = (
        "Você é um especialista em documentação de software. Por favor, crie um README em formato markdown, "
        "em português, descrevendo detalhadamente a arquitetura do projeto e fornecendo descrições individuais "
        "para cada arquivo listado abaixo. Para cada arquivo, explique seu propósito no sistema, o que ele faz, "
        "como ele interage com outros arquivos, e sua importância para o funcionamento geral do projeto. "
        "Descreva também quaisquer dependências ou configurações importantes. Não inclua o arquivo que está gerando "
        "este README no resumo. Seja o mais detalhado possível em todas as explicações, fornecendo uma visão completa "
        "do projeto e seus componentes."
        "\n\nLista de arquivos:\n"
    )
    for file in file_list:
        prompt += f"- {file}\n"

    # Chamada da API do GPT-4 para gerar o README usando o novo método
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4",  # ou "gpt-4" dependendo da sua preferência
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    # Retornar o texto gerado pela API
    return completion.choices[0].message.content

# Função para salvar o README em um arquivo
def save_readme(content, output_path="README.md"):
    with open(output_path, "w") as f:
        f.write(content)

def main():
    # Endereço do arquivo contendo a chave da API
    api_key_file_path = r"local"

    # Ler a chave da API do arquivo txt
    api_key=read_api_key(api_key_file_path)

    # Diretório a ser explorado (onde o script está localizado)
    directory = os.path.dirname(os.path.abspath(__file__))

    # Listar os arquivos
    files = list_files(directory)

    # Gerar o conteúdo do README
    readme_content = generate_readme_content(files, api_key)

    # Salvar o conteúdo no arquivo README.md
    save_readme(readme_content)

    print("README.md criado com sucesso!")

if __name__ == "__main__":
    main()
