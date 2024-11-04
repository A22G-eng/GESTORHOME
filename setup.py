from setuptools import setup, find_packages # type: ignore

setup(
    name='nome_do_seu_projeto',  # Nome do seu projeto
    version='0.1.0',  # Versão do seu projeto
    author='Seu Nome',  # Seu nome ou o nome da sua organização
    author_email='seu_email@example.com',  # Seu e-mail
    description='Uma breve descrição do seu projeto',  # Descrição do projeto
    long_description=open('README.md').read(),  # Descrição longa, geralmente lida de um README
    long_description_content_type='text/markdown',  # Tipo de conteúdo da descrição longa
    url='https://github.com/seu_usuario/nome_do_seu_projeto',  # URL do repositório
    packages=find_packages(),  # Encontra automaticamente os pacotes
    classifiers=[  # Classificadores para ajudar na categorização do seu projeto
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versão mínima do Python necessária
    install_requires=[  # Dependências do seu projeto
        'transformers',  # Exemplo de dependência
        'datasets',  # Exemplo de dependência
    ],
)