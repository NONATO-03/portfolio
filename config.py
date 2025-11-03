#Este projeto é facilmente customizável, você pode alterar as informações aqui para refletir seu perfil.
#Basta alterar as strings e listas abaixo.
# Não se esqueça de alterar também o arquivo secrets_email.py com suas credenciais de email.
# Você pode adicionar mais projetos ou certificados na lista 'PROJETOS' 'EDUCACAO' seguindo o formato dos exemplos.
# Certifique-se de que os nomes dos ícones correspondam aos arquivos em static/img/icons
# e que as imagens dos projetos estejam na pasta static/img/projects.
# Boa sorte! Obrigado por usar este template.
# Se tiver dúvidas, abra uma issue no GitHub.
# Autor: Vitor Nonato

CONFIG = {
    'INFORMACOES_PESSOAIS': {
        'NOME': 'Vitor Nonato', #Seu nome rs
        'EMAIL': 'seu.email@exemplo.com', #seu email
        'TEXTO_HERO_1': 'Olá, me chamo', #Texto que aparece no ínicio
        'TEXTO_HERO_2': 'Dê uma olhada no meu site', #Texto que aparece no inicio p2
        'FOTO_VERTICAL_URL': '/img/foto_vertical.png' #Foto sua
    },
    'REDES_SOCIAIS': {
        'GITHUB_URL': 'https://github.com/seu-usuario', #Seu github
        'LINKEDIN_URL': 'https://linkedin.com/in/seu-usuario' #Seu linkedin
    },
    'NAVEGACAO': {
        'HOME': 'Home', #Nomes que aparecem na navegação
        'SOBRE': 'Sobre mim',
        'PROJETOS': 'Projetos',
        'EDUCACAO': 'Educação',
        'CONTATO': 'Contato'
    },
    'SOBRE_MIM': {
        'TITULO': 'Sobre mim', #Titulo da seção
        'CONTEUDO': """ 
            Aqui você escreve um parágrafo ou mais sobre você.
            Fale sobre suas paixões, suas habilidades técnicas, o que você busca na sua carreira
            e qualquer outra coisa que achar relevante. Este texto pode ser longo e conter
            quebras de linha.
        """
    },
    'LINGUAGENS': [ #Tecnologias que você domina, o nome deve ser igual ao do icone em static/img/icons
        {'nome': 'C', 'icone': 'c_icon.svg', 'ativo': True},
        {'nome': 'C++', 'icone': 'cpp_icon.svg', 'ativo': False},
        {'nome': 'C#', 'icone': 'cs_icon.svg', 'ativo': False},
        {'nome': 'CSS', 'icone': 'css_icon.svg', 'ativo': True},
        {'nome': 'Django', 'icone': 'django_icon.svg', 'ativo': False},
        {'nome': 'Flask', 'icone': 'flask_icon.svg', 'ativo': True},
        {'nome': 'Flutter', 'icone': 'flutter_icon.svg', 'ativo': False},
        {'nome': 'Git', 'icone': 'git_icon.svg', 'ativo': True},
        {'nome': 'HTML', 'icone': 'html_icon.svg', 'ativo': True},
        {'nome': 'Java', 'icone': 'java_icon.svg', 'ativo': True},
        {'nome': 'Javascript', 'icone': 'Javascript_icon.svg', 'ativo': False},
        {'nome': 'Kotlin', 'icone': 'Kotlin_icon.svg', 'ativo': False},
        {'nome': 'PHP', 'icone': 'php_icon.svg', 'ativo': False},
        {'nome': 'Python', 'icone': 'python_icon.svg', 'ativo': True},
        {'nome': 'React', 'icone': 'react_icon.svg', 'ativo': False},
        {'nome': 'Spring', 'icone': 'spring_icon.svg', 'ativo': False},
    ],
    'PROJETOS': [
        { # Exemplo de projeto
            "TITULO": "Meu Projeto 1",
            "DESCRICAO": "Breve descrição do projeto 1...",
            "DEMO": True, # Se tiver demo, coloque True, se não, False
            "DEMO_LINK": "https://demo-do-projeto-1.com",
            "REPOSITORIO": True, # Se tiver repositório, coloque True, se não, False
            "REPOSITORIO_LINK": "https://github.com/seu-usuario/projeto-1",
            "TECNOLOGIAS": ["PYTHON"],  # nomes dos icons/tecnologias
            "IMAGENS": ["projeto_1.png"]  # nomes dos arquivos em static/img/projects
        },
        {
            "TITULO": "Nome do Projeto 2",
            "DESCRICAO": "Este projeto resolve um problema interessante usando tecnologia X.",
            "DEMO": True, # Se tiver demo, coloque True, se não, False
            "DEMO_LINK": "https://demo-do-projeto-2.com",
            "REPOSITORIO": True, # Se tiver repositório, coloque True, se não, False
            "REPOSITORIO_LINK": "https://github.com/seu-usuario/projeto-2",
            "TECNOLOGIAS": ["PYTHON", "FLASK", "PANDAS", "HTML", "CSS"],  # nomes dos icons/tecnologias
            "IMAGENS": ["projeto_2.png"]  # nomes dos arquivos em static/img/projects
        },
        {
            "TITULO": "Nome do Projeto 3",
            "DESCRICAO": "Uma plataforma incrível para visualizar e analisar dados em tempo real.",
            "DEMO": True, # Se tiver demo, coloque True, se não, False
            "DEMO_LINK": "https://demo-do-projeto-3.com",
            "REPOSITORIO": True, # Se tiver repositório, coloque True, se não, False
            "REPOSITORIO_LINK": "https://github.com/seu-usuario/projeto-3",
            "TECNOLOGIAS": ["PYTHON", "FLASK", "HTML", "CSS", "JAVASCRIPT"],  # nomes dos icons/tecnologias
            "IMAGENS": ["projeto_3.png"]  # nomes dos arquivos em static/img/projects
        },
        {
            "TITULO": "Nome do Projeto 4",
            "DESCRICAO": "Um app para organizar o dia a dia, feito com a tecnologia Y.",
            "DEMO": True, # Se tiver demo, coloque True, se não, False
            "DEMO_LINK": "https://demo-do-projeto-4.com",
            "REPOSITORIO": True, # Se tiver repositório, coloque True, se não, False
            "REPOSITORIO_LINK": "https://github.com/seu-usuario/projeto-4",
            "TECNOLOGIAS": ["PYTHON", "FLASK", "REACT"],  # nomes dos icons/tecnologias
            "IMAGENS": ["projeto_4.png"]  # nomes dos arquivos em static/img/projects
        }
    ],
    'EDUCACAO': [
        {
            'TITULO': 'Instituição 1 — Curso X',
            'DESCRICAO': 'Período: 2020 – 2024. Foco em desenvolvimento de software.',
            'CERTIFICADO': False,
            'CERTIFICADO_ARQUIVO': 'documents/certificado_1.pdf' # PDF local em static/documents/
            # Ou use um link externo (não use ambos):
            # 'CERTIFICADO_LINK': 'https://exemplo.com/certificado1.pdf'
        },
        {
            'TITULO': 'CURSO A',
            'DESCRICAO': 'Concluído em 2023.',
            'CERTIFICADO': True,
            'CERTIFICADO_ARQUIVO': 'documents/certificado_2.pdf'
        },
        {
            'TITULO': 'Curso B',
            'DESCRICAO': 'Carga horária 40h.',
            'CERTIFICADO': False
        }
    ],
    'CONTATO': { # Seção de contato
        'TITULO': 'Me contate',
        'TEXTO_OU': 'Ou',
        'PLACEHOLDER_ASSUNTO': 'Assunto do Email',
        'PLACEHOLDER_MENSAGEM': 'Sua mensagem aqui...'
    }
}