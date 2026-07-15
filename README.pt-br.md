# NanoFast Results Compiler

🌐 Leia em: [English](README.md) | [Português (Brasil)](README.pt-br.md) | [Português (Portugal)](README.pt-pt.md) | [Español](README.es.md) | [Français](README.fr.md)

## Para que serve o Script
O Compilador de Resultados NanoFast é uma ferramenta de automação em Python desenvolvida para agilizar o processamento e a apresentação dos resultados de testes Nanofast. Ele compila automaticamente resultados individuais armazenados em um leitor ou salvos localmente em um modelo mestre do Excel estruturado e de fácil leitura para análise posterior.

## Como funciona
1. **Coleta de Dados:** O script verifica os dados no diretório `Raw Data` ou no dispositivo leitor em busca de pastas de resultados. Para cada pasta, ele abre o arquivo CSV de destino e seu arquivo `result.json` correspondente.
2. **Extração de Metadados:** Ele extrai metadados específicos do JSON (incluindo ID da Amostra, Identificador do Cassete, Código do Lote, detalhes do Protocolo, Data/Hora e Resultado Final) e os empilha sobre os dados brutos do CSV.
3. **Injeção de Modelo:** O script cria uma planilha Excel e cola os dados compilados na aba `Raw Data`, atribuindo uma coluna por resultado de teste.
4. **Lotes e Nomenclatura:** Para evitar o transbordamento do modelo, o script processa os resultados em lotes de 40. Ele gera dinamicamente arquivos de saída nomeados com a data atual, hora e número do lote (por exemplo, `Compiled NanoFast Results - 07 Jul 26 - 15.43 - Part 1.xlsx`).
5. **Limpeza:** Após a conclusão bem-sucedida, se o script for executado localmente e os dados copiados, ele limpa automaticamente a pasta `Raw Data` para garantir que ela fique vazia e pronta para a próxima execução.

## Como Instalar
### Pré-requisitos
* Instale o Python *diretamente da Microsoft Store*. O script foi testado com `Python 3.13`.
* Baixe a versão mais recente do repositório no GitHub, usando a seção de lançamentos (releases) na barra lateral.
* Na seção de ativos (assets) da página de lançamentos, baixe o arquivo .zip.
### Instalação
* Extraia o .zip diretamente em sua unidade C:. Instalações em outros locais não são recomendadas e podem resultar em erros de caminho de arquivo.

### Primeira execução
* No primeiro uso, o script baixa automaticamente as dependências necessárias. Por favor, permita que este processo seja concluído.
* Após a instalação dos pacotes, você será solicitado a selecionar o idioma de sua preferência.
* As execuções subsequentes ignorarão esta fase de configuração e prosseguirão diretamente para o compilador.

## Como Usar
### Passos de Execução
1. Se for processar dados de um dispositivo, conecte o leitor Nanofast ao PC usando um cabo USB-C, ligue o leitor e coloque o dispositivo no 'Modo de Armazenamento em Massa' (Mass Storage Mode) usando o Menu no leitor. Se for usar dados locais, copie todas as pastas de resultados de testes individuais (cada uma contendo um CSV e um `result.json`) para a pasta `Raw Data`.
2. Execute o arquivo `Solus NanoFast Compliler.bat` clicando duas vezes.
3. Selecione o local apropriado para o processamento de dados.
    * Pressione 1 para Automático. Isso obtém os resultados automaticamente do dispositivo.
    * Pressione 2 para Manual. Para esta opção, copie os resultados manualmente para a pasta chamada `Raw Data`.  
4. Selecione o intervalo de datas para o processamento de dados, usando as setas para cima e para baixo e confirmando com Enter.
5. O script exibirá um aviso no terminal informando que a pasta `Raw Data` será excluída após o processamento. Digite `Y` e/ou pressione **Enter** para continuar. Os dados armazenados em um Leitor não podem ser excluídos; isso só importa se você tiver transferido arquivos manualmente.
6. O terminal exibirá o progresso à medida que divide em lotes e exporta os dados.
7. Quando concluído, recupere seus arquivos `Compiled NanoFast Results` recém-gerados no diretório principal. A pasta `Raw Data` agora estará vazia.

## Problemas Conhecidos
1. Durante a execução inicial, o script instala o pandas com sucesso, mas falha ao inicializar na mesma sessão. Como solução temporária, reiniciar o script resolverá o problema. Este é um problema conhecido programado para ser resolvido em uma próxima atualização.

## Tradução
A tradução foi realizada pelo Google e não por um falante nativo. Por favor, forneça feedback sobre a tradução no GitHub. Pedimos desculpas por quaisquer erros.

---
Script criado por Steve Carter em 2026.