# ClickFood

ClickFood é um sistema web criado com Django, focado em delivery e gestão de pedidos para restaurantes. Seu surgimento se deu a partir de um sorteio de tema para um trabalho de conclusão da disciplina de Programação Web II (PWEB II), ministrada pelo professor Sérgio Vieira, no curso técnico integrado em Informática do IFCE – Campus Itapipoca.

Embora a proposta inicial envolvesse um sistema completo de pedidos para usuários e uma área administrativa restrita a administradores com login e senha, o tempo disponível não permitiu a entrega do escopo completo, restringindo o projeto ao desenvolvimento de uma estrutura funcional de autenticação de usuários. Assim, foi implementado um sistema de login com validação integrada ao painel administrativo do Django, em que o superusuário definido também serve como credencial de acesso ao site por meio de uma interface de login personalizada.

O layout das páginas foi construído com HTML5, CSS3, JavaScript e Bootstrap, com o objetivo de oferecer uma experiência imersiva e elegante ao usuário final, sendo responsivo e interativo.

## 🚀 Começando 

As seguintes instruções permitirão que você obtenha uma cópia do sistema web na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

O que você precisa ter ou instalar na sua máquina para rodar e testar a aplicação Django?

```
Python 3.10 ou superior
```
```
Django 5.1.2
```
```
Git - para clonar o repositório e gerenciar o versionamento
```
```
Ambiente Virtual (eu utilizo e recomendo o Anaconda ou Miniconda)
```

### 🔧 Instalação

Após verificar se possuí todas as dependências necessárias para rodar a aplicação, você deve criar uma pasta, onde você irá clonar os arquivos do clickfood. Com a pasta criada, vá ao terminal ou anaconda prompt, caso use-o como ambiente virtual e execute os comandos abaixo, passo a passo.

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/clickfood.git
cd clickfood
```

2. Crie e ative um ambiente Conda:

```
conda create -n clickfood python=3.10
conda activate clickfood
```

3. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

4. Aplique as migrações:

```
python manage.py migrate
```

5. Crie um superusuário:

```
python manage.py createsuperuser
```

6. Rode o servidor:

```
python manage.py runserver
```

7. Acesse o sistema web:

```
http://127.0.0.1:8000
```

Termine com um exemplo de como obter dados do sistema ou como usá-los para uma pequena demonstração.

## ⚙️ Executando os testes

Este projeto não possui testes automatizados implementados até o momento.

No entanto, as funcionalidades principais foram testadas manualmente, como:
- Acesso ao sistema de login com as credenciais do superusuário
- Redirecionamento correto após o login
- Acesso ao painel administrativo do Django

Para testar:
1. Execute o servidor com `python manage.py runserver`
2. Acesse `http://localhost:8000/`
3. Clique no botão de login na navbar do site para ser redirecionado à página de login
4. Use as credenciais do superusuário para fazer login
5. Acesse `/admin/` para verificar o painel administrativo

## 📦 Implantação

Este projeto ainda não foi implantado em ambiente de produção.

No entanto, ele pode ser facilmente hospedado em plataformas que suportam aplicações Django, como:
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Render](https://render.com/)
- [Fly.io](https://fly.io/)
- Servidores com suporte a WSGI (Apache/Nginx + Gunicorn)

Antes da implantação, recomenda-se:
- Criar variáveis de ambiente para esconder dados sensíveis
- Usar `ALLOWED_HOSTS` corretamente no `settings.py`
- Configurar um banco de dados em produção (PostgreSQL, por exemplo)
- Ativar o modo `DEBUG = False`

## 🛠️ Construído com

* [Python 3.10+](https://www.python.org/) – Linguagem de programação principal  
* [Django 5.x](https://www.djangoproject.com/) – Framework web backend  
* [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML) – Estrutura das páginas  
* [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS) – Estilização visual  
* [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) – Funcionalidades interativas  
* [Bootstrap 5](https://getbootstrap.com/) – Framework CSS para layout responsivo  
* [Git](https://git-scm.com/) – Controle de versão  
* [GitHub](https://github.com/) – Hospedagem do repositório  
* [Anaconda / Miniconda](https://www.anaconda.com/) – Gerenciamento de ambientes virtuais  

## ✒️ Autores

* **Lucas Vinicius David Martins** - *Desenvolvedor Principal* - [luvini7](https://github.com/luvini7)

Este projeto é parte do meu portfólio de front-end/back-end. Até o momento, ele foi desenvolvido apenas por mim, porém pretendo ter contribuições de outros desenvolvedores futuramente para continuar o desenvolvimento do ClickFood.

## 📄 Licença

Este projeto está atualmente sem uma licença definida. Fique à vontade para entrar em contato se tiver dúvidas sobre o uso do código.

No futuro, uma licença será adicionada para esclarecer os direitos de uso.

## ⏭️ Próximos Passos

Pretendo prosseguir com esse projeto futuramente para ter um sistema web com a sua proposta inicial, que é ser um sistema de delivery para usuários realizarem pedidos com uma área administrativa para gerenciamento desses pedidos.

Futuramente irei abrir para colaborações :)

## 🧑‍💻 Gostou do meu trabalho?

Caso tenha interesse em começar um projeto de front-end, que é minha especialidade, ou até mesmo continuar este projeto, entre em contato comigo!

**Email:** [lucasmartins2468@gmail.com](mailto:lucasmartins2468@gmail.com)  
**LinkedIn:** [Lucas Vinicius David Martins](https://www.linkedin.com/in/lucasvinicius7)  
**GitHub:** [luvini7](https://github.com/luvini7)
**WhatsApp:** [Envie uma mensagem](https://wa.me/5588988371567)

Agradeço por ter chegado até aqui!! Sucesso 🥂