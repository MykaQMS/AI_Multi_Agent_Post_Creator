"""
Módulo de Agentes de IA utilizando a SDK oficial do Google Gemini (google-genai).

Este módulo define a lógica dos 4 agentes especialistas:
1. Buscador: Busca notícias recentes usando Google Search Grounding.
2. Planejador: Estrutura o roteiro do post com base nas pesquisas.
3. Redator: Escreve a primeira versão do post para o Instagram.
4. Revisor: Revisa a qualidade, tom de voz e clareza do texto final.
"""

import os
from datetime import date
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carrega variáveis de ambiente salvas no arquivo .env (se existir)
load_dotenv()

# Modelo padrão do Gemini para execução dos agentes
MODEL_ID = "gemini-2.5-flash"


def get_client() -> genai.Client:
    """Instancia e retorna o cliente oficial do Google Gemini SDK."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "Chave de API do Gemini não encontrada!\n"
            "Por favor, certifique-se de definir a variável GOOGLE_API_KEY no arquivo .env ou no sistema."
        )
    return genai.Client(api_key=api_key)


def agente_buscador(topico: str, data_de_hoje: str = None) -> str:
    """
    Agente 1 - Buscador de Notícias:
    Utiliza o Google Search Grounding do Gemini para buscar novidades e atualizações sobre o tema.
    """
    if not data_de_hoje:
        data_de_hoje = date.today().strftime("%d/%m/%Y")

    client = get_client()
    prompt = f"""
    Você é um pesquisador especialista em tecnologia e tendências.
    Pesquise no Google sobre o seguinte tópico: {topico}
    Considere a data atual como: {data_de_hoje}
    
    Identifique os lançamentos, atualizações ou novidades mais relevantes sobre o assunto.
    Resuma os pontos principais de forma objetiva e factual.
    """

    config = types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())]
    )

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config,
    )
    return response.text


def agente_planejador(topico: str, lancamentos_buscados: str) -> str:
    """
    Agente 2 - Planejador de Posts:
    Recebe as informações pesquisadas e cria o plano/roteiro estruturado para o post.
    """
    client = get_client()
    prompt = f"""
    Você é um estrategista de conteúdo para redes sociais.
    Tópico: {topico}
    Notícias e pesquisas encontradas:
    {lancamentos_buscados}
    
    Crie um plano estruturado para um post de Instagram sobre este tema.
    O plano deve conter:
    1. Gancho (Hook): Frase de impacto inicial para prender a atenção.
    2. Pontos Principais: 2 a 3 pontos essenciais que devem ser abordados.
    3. Chamada para Ação (CTA): Uma pergunta ou convite engajador para o leitor comentar.
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    return response.text


def agente_redator(topico: str, plano_de_post: str) -> str:
    """
    Agente 3 - Redator Criativo:
    Redige o rascunho do post de Instagram com linguagem acessível, emojis e hashtags.
    """
    client = get_client()
    prompt = f"""
    Você é um Redator Criativo especializado em redes sociais para a área de tecnologia.
    Tópico: {topico}
    Plano do Post:
    {plano_de_post}
    
    Escreva um rascunho de post para o Instagram com base no plano fornecido.
    Diretrizes:
    - Tom amigável, instrutivo e engajador.
    - Utilize emojis para deixar a leitura leve.
    - Inclua uma chamada para ação clara ao final.
    - Adicione de 2 a 4 hashtags relevantes no final do post.
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    return response.text


def agente_revisor(topico: str, rascunho_gerado: str) -> str:
    """
    Agente 4 - Revisor de Conteúdo:
    Faz a revisão final de tom de voz, clareza, concisão e gramática.
    """
    client = get_client()
    prompt = f"""
    Você é um Editor e Revisor de Conteúdo sênior para redes sociais.
    Público-alvo: Pessoas interessadas em tecnologia, ciência de dados e inteligência artificial (18 a 30 anos).
    
    Tópico: {topico}
    Rascunho a ser revisado:
    {rascunho_gerado}
    
    Examine o rascunho verificando clareza, tom de voz, correção gramatical e engajamento.
    Retorne o texto final aprimorado e pronto para publicação no Instagram.
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    return response.text
