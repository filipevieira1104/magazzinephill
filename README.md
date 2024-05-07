![logo](https://github.com/filipevieira1104/magazzinephill/assets/61087331/5f8a590f-3703-41fa-83a8-b08275a8e514)

<h1>Projeto: Loja online de produtos eletrônicos</h1>

![image](https://github.com/filipevieira1104/magazzinephill/assets/61087331/f48239b2-8791-43a2-a311-9cf3dd1b5d19)
<hr>
<h3>Detalhes do Projeto</h3>

<p>Loja de produtos eletrônicos completa:</p>

<li>Categorias de produtos</li>
<li>Detalhe dos Produtos</li>
<li>Carrinho de compras</li>
<li>Envio de e-mail para o usuário informando o número do pedido e a fatura de compras em PDF</li>
<li>Integração com a API da Stripe (Gateway de pagamento com cartões)</li>
<hr>
<h3>Configurações</h3>

<p>Instalar dependências</p>

<p><strong>pip install -r requirements.txt</strong></p>
<hr
<p><strong>Celery</strong></p>
<li>Baixar imgem Docker RabbitMQ</li>
<p><strong>docker pull rabbitmq</strong></p>
<p>(* observação: Isso fará o download da imagem RabbitMQ Docker para a sua máquina local. Você pode encontrar informações sobre a imagem oficial do RabbitMQ Docker em https://hub.docker.com/_/rabbitmq</p>
<li>Iniciar o servidor RabbitMQ com Docker</li>
<p><strong>docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management</strong></p>
<li>Iniciando uma task Celery</li>
<p><strong>celery -A myshop worker -l info --pool=solo</strong></p>
<hr>
<p><strong>E-mail Backend</strong></p>
<p>Adicionar nos settings os dados do servidor de email, conforme exemplo abaixo</p>

![image](https://github.com/filipevieira1104/magazzinephill/assets/61087331/6937f85c-1167-477e-83d9-8ceb2f3e4ad1)
<hr>
<p><strong>Stripe (Gateway de pagamento)</strong></p>
<p>Seguir as seguintes etapas:</p>
<li>Criar conta no site da Stripe  https://dashboard.stripe.com/register</li>
<li>Obter a chave da API</li>
<p>Após configurar o Stripe no settings, conforme exemplo abaixo:</p>

![image](https://github.com/filipevieira1104/magazzinephill/assets/61087331/e54080b2-db9a-4231-ba47-0c517de6dde5)


