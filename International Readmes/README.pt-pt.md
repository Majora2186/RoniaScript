# NanoFast Results Compiler

🌐 Leia em: [English](README.md) | [Português (Brasil)](README.pt-br.md) | [Português (Portugal)](README.pt-pt.md) | [Español](README.es.md) | [Français](README.fr.md)

## Para que serve o Script
O Compilador de Resultados NanoFast é uma ferramenta de automação em Python concebida para agilizar o processamento e a apresentação dos resultados de testes Nanofast. Este compila automaticamente resultados individuais num leitor ou guardados localmente para um modelo principal do Excel estruturado e de fácil leitura para análise posterior.

## Como funciona
1. **Recolha de Dados:** O script verifica os dados no diretório `Raw Data` ou no dispositivo leitor à procura de pastas de resultados. Para cada pasta, abre o ficheiro CSV de destino e o respetivo ficheiro `result.json`.
2. **Extração de Metadados:** Extrai metadados específicos do JSON (incluindo ID da Amostra, Identificador da Cassete, Código do Lote, detalhes do Protocolo, Data/Hora e Resultado Final) e junta-os aos dados brutos do CSV.
3. **Injeção de Modelo:** O script cria uma folha de cálculo Excel e cola os dados compilados na folha `Raw Data`, atribuindo uma coluna por cada resultado de teste.
4. **Lotes e Nomenclatura:** Para evitar o limite de capacidade do modelo, o script processa os resultados em lotes de 40. Gera dinamicamente ficheiros de saída nomeados com a data atual, hora e número do lote (por exemplo, `Compiled NanoFast Results - 07 Jul 26 - 15.43 - Part 1.xlsx`).
5. **Limpeza:** Após a conclusão com sucesso, se o script for executado localmente, os dados copiados são eliminados automaticamente da pasta `Raw Data` para garantir que esta fica vazia e pronta para a próxima execução.

## Como Instalar
### Pré-requisitos
* Instale o Python *diretamente a partir da Microsoft Store*. O script foi testado com `Python 3.13`.
* Descarregue o lançamento mais recente do repositório no GitHub, utilizando a secção de lançamentos (releases) na barra lateral.
* Na secção de ativos (assets) da página de lançamentos, descarregue o ficheiro .zip.
### Instalação
* Extraia o .zip diretamente para a sua unidade C:. Instalações noutros locais não são recomendadas e podem resultar em erros no caminho dos ficheiros.

### Primeira execução
* Na primeira utilização, o script descarrega automaticamente as dependências necessárias. Por favor, permita que este processo seja concluído.
* Após a instalação dos pacotes, ser-lhe-á pedido que selecione o seu idioma preferido.
* As execuções subsequentes ignorarão esta fase de configuração e prosseguirão diretamente para o compilador.

## Como Usar
### Passos de Execução
1. Se estiver a processar dados de um dispositivo, ligue o leitor Nanofast ao PC utilizando um cabo USB-C, ligue o leitor e coloque o dispositivo em 'Modo de Armazenamento de Massa' (Mass Storage Mode) utilizando o Menu no leitor. Se estiver a utilizar dados locais, copie todas as pastas de resultados de testes individuais (cada uma contendo um CSV e um `result.json`) para a pasta `Raw Data`.
2. Execute o ficheiro `Solus NanoFast Compliler.bat` com um duplo clique.
3. Selecione o local apropriado para o processamento de dados.
    * Pressione 1 para Automático. Isto obtém os resultados automaticamente do dispositivo.
    * Pressione 2 para Manual. Para esta opção, copie manualmente os resultados para a pasta chamada `Raw Data`.  
4. Selecione o intervalo de datas para o processamento de dados, utilizando as setas para cima e para baixo e selecionando com Enter.
5. O script irá mostrar um aviso no terminal a informar que a pasta `Raw Data` será eliminada após o processamento. Escreva `Y` e/ou pressione **Enter** para continuar. Os dados armazenados num Leitor não podem ser eliminados; isto só tem impacto se tiver transferido ficheiros manualmente.
6. O terminal irá mostrar o progresso à medida que divide em lotes e exporta os dados.
7. Assim que estiver concluído, recupere os seus ficheiros `Compiled NanoFast Results` recém-gerados no diretório principal. A pasta `Raw Data` estará agora vazia.

## Problemas Conhecidos
1. No primeiro arranque, o script instala com sucesso o pandas, mas falha ao inicializar na mesma sessão. Como solução temporária, reiniciar o script irá resolver o problema. Este é um problema conhecido que está agendado para resolução numa próxima atualização.

## Tradução
A tradução foi realizada pelo Google e não por um falante nativo. Por favor, forneça o seu feedback sobre a tradução no GitHub. Pedimos desculpa por quaisquer erros.

---
Script criado por Steve Carter em 2026.