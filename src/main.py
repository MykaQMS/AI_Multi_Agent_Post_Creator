"""
Script principal do Criador Multi-Agente de Posts com a API do Gemini.

Este script executa a pipeline interativa dos 4 agentes diretamente no terminal.
"""

import sys
from datetime import date
from agents import (
    agente_buscador,
    agente_planejador,
    agente_redator,
    agente_revisor,
)


def main():
    print("=" * 65)
    print(" 🚀 SISTEMA MULTI-AGENTE DE CRIAÇÃO DE POSTS (GEMINI API) 🚀 ")
    print("=" * 65)

    topico = input(
        "\n❓ Digite o TÓPICO ou TENDÊNCIA sobre o qual deseja criar o post: "
    ).strip()

    if not topico:
        print("❌ O tópico não pode ser vazio. Encerrando o programa.")
        sys.exit(1)

    data_atual = date.today().strftime("%d/%m/%Y")
    print(f"\n📅 Data de referência: {data_atual}")

    try:
        print("\n[1/4] 🔍 Agente Buscador: Pesquisando novidades recentes no Google...")
        lancamentos = agente_buscador(topico, data_atual)
        print("✔ Pesquisa concluída com sucesso!")

        print("\n[2/4] 📋 Agente Planejador: Criando o roteiro do post...")
        plano = agente_planejador(topico, lancamentos)
        print("✔ Planejamento concluído com sucesso!")

        print("\n[3/4] ✍️ Agente Redator: Escrevendo o rascunho do post...")
        rascunho = agente_redator(topico, plano)
        print("✔ Rascunho gerado com sucesso!")

        print("\n[4/4] 🕵️ Agente Revisor: Revisando e polindo a versão final...")
        post_final = agente_revisor(topico, rascunho)
        print("✔ Revisão finalizada!")

        print("\n" + "=" * 65)
        print(" RESULTADO FINAL - POST PRONTO PARA O INSTAGRAM")
        print("=" * 65 + "\n")
        print(post_final)
        print("\n" + "=" * 65)

    except Exception as e:
        print(f"\n❌ Ocorreu um erro durante a execução dos agentes: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
