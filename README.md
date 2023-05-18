# API-Flask-Oauth2
Aplicação Flask que consome API utilizando o autenticador Oauth2

Ferramentas utilizadas:

Python ( Linguagem back-end )
Flask ( Framework Web Python )
Oauth2 ( Autenticador )
Google ( Autenticador )
VScode ( IDE )

Etapas para execução e criação do projeto.

<h1>Etapa 1</h1>

Criação do ambiente de desenvolvimento

Criação de uma máquina virtual

Instalando extensões FLASK e Python no Vscode

<h4>Dificuldade: escolha das tecnologias para realização da aplicação</h4>
<h4>Motivo da escolha(Python e Flask): Facilidade de aprendizado e aplicação se comparado a outras linguagens e frameworks</h4>

<h1>Etapa 2</h1>
Criar uma candidatura em um serviço compatível com Oauth2, serviço utilizado: https://marketplace.gohighlevel.com/

Criando client keys para ter acesso as credenciais client_id e client_secret e utilizar dentro da aplicação para geração de token usando a documentação https://highlevel.stoplight.io/docs/integrations/

<h4>Dificuldade: Entender o motivo da geração do client_id e client_secret</h4>
<h4>Motivo da escolha: marketplace.gohighlevel já entrega o client_id e client_secret com poucos cliques e já pronto para utilização. </h4>

<h1>Etapa 3</h1>

Implementar a autorização Oauth2 no código web incluindo:

a. Redirecionando usuários para a URL de autorização

b. Manipulando o retorno de chamada de autorização

c. Trocar o código de autorização por um token de acesso

d. Armazenando o token de acesso com segurança

Utilizando o chatGPT e a documentação do próprio Oauth2 e Flask pude implementar a autorização Oauth2 e acrescentar uma autorização do Google para melhor segurança.

<h4>Dificuldade: Trocar o código de autorização por um token de acesso, tendo que recorrer a várias documentações e principalmente stackOverFlow, junto ao chatGPT para conseguir, mas na própria documentação do Oauth2 há uma explicação mostrando como fazer essa troca</h4>

<h1>Etapa 4</h1>

Usar o token de acesso para fazer uma solicitação da API e buscar dados como ( informações de perfil, lista de contatos e etc)

<h4>Dificuldade: Criação de rotas que utilizem da API e busca dos dados</h4>

<h1>Etapa 5</h1>

Criação de uma página web simples para exibir os resultados de busca de dados de forma organizada

<h1>Vídeo de exemplo do projeto</h1>











