# Repositório-Modelo para Trabalhos Acadêmicos

> **Template multi-propósito para trabalhos acadêmicos da UFPB/CCSA: aplicável a áreas como Ciência de Dados, Economia e afins.**

Este repositório serve como modelo de referência para estudantes do **Centro de Ciências Sociais Aplicadas (CCSA)** da **Universidade Federal da Paraíba (UFPB)** que precisam organizar seus projetos de pesquisa (TCC, dissertação, tese, etc.). O foco é garantir **reprodutibilidade**, **boas práticas** e **documentação**, permitindo que a mesma pipeline de dados alimente diferentes formatos de documento acadêmico.

---

## Tipos de Documento Suportados

| Tipo | Descrição | Classe LaTeX | Estrutura |
|------|-----------|-------------|-----------|
| `tcc_artigo` | TCC em formato de artigo técnico-científico | `abntex2[article]` | Seções contínuas |
| `tcc` | TCC padrão / monografia com capítulos | `abntex2` | Capítulos |
| `artigo` | Artigo científico avulso | `abntex2[article]` | Seções contínuas |
| `dissertacao` | Dissertação de mestrado | `abntex2` | Capítulos |
| `tese` | Tese de doutorado | `abntex2` | Capítulos |
| `livro` | Livro didático / texto de apoio | `abntex2` | Capítulos |
| `relatorio` | Relatório técnico-científico | `abntex2[article]` | Seções contínuas |
| `projeto` | Projeto de pesquisa | `abntex2[article]` | Seções contínuas |

---

## O que é um Trabalho Científico?

Fazer ciência não é apenas apresentar números ou publicar um documento. Um trabalho científico se baseia em princípios fundamentais de **transparência, ética, honestidade intelectual e curiosidade**.

Para que uma pesquisa tenha validade e seja útil para a comunidade (colegas, professores e outros cientistas), ela precisa permitir que os resultados sejam verificados de forma independente.

Por isso, **os dados e os códigos devem ficar sempre disponíveis**. Se você treinou um modelo que obteve 95% de acurácia, qualquer outra pessoa usando seu repositório deve conseguir rodar o mesmo código e chegar exatamente nos mesmos 95%. Sem reprodutibilidade, um resultado não passa de uma afirmação sem provas.

---

## Estrutura do Repositório

```
projeto-tcc/
├── README.md                          ← Você está aqui
├── .gitignore
├── pyproject.toml                     ← Configuração do projeto (uv)
├── Makefile                           ← Automação de tarefas
│
├── tex/                               ← Arquivos LaTeX
│   ├── tcc_artigo/                    ← TCC formato artigo
│   │   ├── main.tex
│   │   ├── referencias.bib
│   │   ├── figuras/                   ← Figuras .eps
│   │   └── tabelas/                   ← Tabelas .tex
│   ├── tcc/                           ← TCC padrão / monografia
│   │   ├── main.tex
│   │   ├── referencias.bib
│   │   ├── figuras/
│   │   └── tabelas/
│   ├── artigo/
│   │   └── ... (mesma estrutura)
│   ├── dissertacao/
│   │   └── ...
│   ├── tese/
│   │   └── ...
│   ├── livro/
│   │   └── ...
│   ├── relatorio/
│   │   └── ...
│   └── projeto/
│       └── ...
│
├── dados/                             ← Bases de dados
│   ├── brutos/                        ← Dados originais (raw, imutáveis)
│   └── processados/                   ← Dados após pré-processamento
│
├── scripts/                           ← Scripts Python numerados
│   ├── 01_coleta_dados.py
│   ├── 02_analise_exploratoria.py
│   ├── 03_preprocessamento.py
│   ├── 04_treinamento_modelo.py
│   ├── 05_avaliacao_modelo.py
│   └── 06_exportar_figuras_eps.py
│
├── notebooks/                         ← Jupyter Notebooks
├── resultados/                        ← Resultados gerados
└── modelos/                           ← Modelos treinados
```

### Arquitetura dos Documentos

Cada tipo de documento em `tex/<tipo>/` é **autocontido**:

- `main.tex` — documento LaTeX completo
- `referencias.bib` — referências bibliográficas específicas do tipo
- `figuras/` — figuras vetoriais .eps geradas pela pipeline
- `tabelas/` — tabelas LaTeX geradas pela pipeline (script 05)

As pastas `figuras/` e `tabelas/` são geradas **diretamente** em cada subdiretório de documento pelos scripts 05 e 06, garantindo que cada tipo tenha seus próprios arquivos sem necessidade de sincronização manual.

---

## Reprodutibilidade

> **Princípio fundamental:** Qualquer pessoa deve conseguir clonar este repositório e reproduzir todos os resultados executando os scripts na ordem numerada.

### Fluxo de Trabalho Reprodutível

```
1. Clonar repositório
2. Instalar dependências (uv sync)
3. Executar pipeline (make pipeline)
4. Compilar o documento LaTeX desejado (make latex DOC=tipo)
5. O PDF final contém todos os resultados atualizados
```

### Garantias de Reprodutibilidade

| Aspecto | Como garantimos |
| ----------------------- | ----------------------------------------------- |
| **Seed aleatória** | `SEED = 42` definida em todos os scripts |
| **Dependências** | Versões mínimas em `pyproject.toml` |
| **Dados brutos** | Imutáveis em `dados/brutos/` (nunca modificados) |
| **Pipeline sequencial** | Scripts numerados (01 → 06) |
| **Versionamento** | Git rastreia todo o código e configurações |
| **Tabelas automáticas** | Script 05 gera `.tex` direto dos resultados |
| **Figuras automáticas** | Script 06 converte para `.eps` vetorial |
| **Documentos múltiplos** | Todos os tipos compartilham a mesma pipeline |

---

## Como Usar Este Repositório

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/projeto-tcc.git
cd projeto-tcc
```

### Passo 2: Instalar Dependências

Recomendamos o uso do **[uv](https://docs.astral.sh/uv/)**, um gerenciador de pacotes extremamente rápido em Python:

```bash
uv sync
```

> **Alternativa com pip:** `pip install -r requirements.txt`

### Passo 3: Executar o Pipeline Completo

```bash
make pipeline
```

Ou manualmente:
```bash
uv run python scripts/01_coleta_dados.py
uv run python scripts/02_analise_exploratoria.py
# ... até 06
```

### Passo 4: Compilar o Documento LaTeX

**Compilar o tipo padrão (TCC artigo):**
```bash
make latex
```

**Compilar um tipo específico:**
```bash
make latex DOC=tcc          # TCC monografia
make latex DOC=dissertacao  # Dissertação de mestrado
make latex DOC=tese         # Tese de doutorado
make latex DOC=artigo       # Artigo avulso
make latex DOC=livro        # Livro didático
make latex DOC=relatorio    # Relatório técnico
make latex DOC=projeto      # Projeto de pesquisa
```

**Compilar todos os documentos de uma vez:**
```bash
make latex-all
```

### Passo 5: Escolher e Customizar seu Documento

Ao clonar este repositório para iniciar o seu próprio projeto, você não precisa manter todos os formatos de documento. Recomenda-se o seguinte fluxo:

1. **Escolha o seu modelo:** Defina qual tipo de documento você vai produzir (ex: `tcc_artigo`, `dissertacao`, etc.).
2. **Delete os demais modelos:** Remova as pastas dos tipos de documento que você **não** vai utilizar de dentro de `tex/` para manter seu repositório limpo e focado no seu trabalho.
3. **Personalize o documento escolhido:** Cada `main.tex` é um **esqueleto independente**. Você deve:
   - Editar o preâmbulo (instituição, título, autor, orientador)
   - Substituir o conteúdo de exemplo pelo seu próprio texto
   - Manter os imports de `figuras/` e `tabelas/` locais
   - Adicionar ou remover seções conforme necessário

### Criar um Novo Tipo de Documento

```bash
make new-doc TYPE=monografia
```

Isso cria `tex/monografia/` com `main.tex`, `figuras/` e `tabelas/` a partir do template base. Depois edite o arquivo e compile com:

```bash
make latex DOC=monografia
```

---

## Comandos do Makefile

| Comando | Descrição |
|---------|-----------|
| `make help` | Mostra o menu de ajuda |
| `make setup` | Instala dependências Python |
| `make pipeline` | Executa pipeline completa (01 → 06) |
| `make latex` | Compila o documento LaTeX padrão (tcc_artigo) |
| `make latex DOC=tipo` | Compila um tipo específico de documento |
| `make latex-all` | Compila todos os tipos de documento |
| `make latex-clean` | Remove artefatos LaTeX do documento atual |
| `make latex-clean-all` | Remove artefatos LaTeX de todos os documentos |
| `make sync-media` | Sincroniza figuras/tabelas para todos os tipos (removido — cada modelo tem seus próprios arquivos) |
| `make list-docs` | Lista os tipos de documento disponíveis |
| `make new-doc TYPE=x` | Cria um novo tipo de documento |
| `make clean` | Remove artefatos gerados (dados, modelos, cache) |
| `make clean-all` | Limpeza total (dados + LaTeX + cache) |

---

## Dependências

### Gerenciador `uv` (Recomendado)

| SO | Comando de Instalação |
|----|---------|
| **Windows** | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"` |
| **macOS / Linux** | `curl -LsSf https://astral.sh/uv/install.sh | sh` |
| **macOS (Homebrew)** | `brew install uv` |

### Python (3.9+)

| Biblioteca | Versão Mínima | Uso |
| ------------ | ------------- | ------------------------ |
| pandas | ≥ 2.0 | Manipulação de dados |
| numpy | ≥ 1.24 | Computação numérica |
| scikit-learn | ≥ 1.3 | Machine Learning |
| lightgbm | ≥ 4.0 | Gradient Boosting |
| matplotlib | ≥ 3.7 | Visualização |
| seaborn | ≥ 0.12 | Visualização estatística |
| joblib | ≥ 1.3 | Persistência de modelos |
| jupyter | ≥ 1.0 | Notebooks interativos |

### LaTeX

| Pacote | Uso |
| ------------- | --------------------------------- |
| `abntex2` | Classe do documento (normas ABNT) |
| `abntex2cite` | Citações no padrão ABNT |
| `imakeidx` | Índice remissivo |
| `booktabs` | Tabelas profissionais |
| `graphicx` | Importação de figuras |
| `epstopdf` | Conversão EPS → PDF |
| `hyperref` | Links e referências clicáveis |
| `siunitx` | Formatação de números |
| `listings` | Código-fonte formatado |
| `subcaption` | Subfiguras |
| `csquotes` | Citações diretas |
| `amsmath` | Equações matemáticas |

**Instalação do LaTeX:**
- **macOS:** `brew install --cask mactex`
- **Linux:** `sudo apt install texlive-full`
- **Windows:** Baixe [MiKTeX](https://miktex.org/download)

---

## Sobre o Documento LaTeX

### Arquitetura Multi-Documento Autocontida

Cada tipo de documento em `tex/<tipo>/main.tex` é independente e autocontido com seus próprios recursos:

- **Figuras:** `tex/<tipo>/figuras/` — geradas diretamente pelo script 06
- **Tabelas:** `tex/<tipo>/tabelas/` — geradas diretamente pelo script 05
- **Referências:** `tex/<tipo>/referencias.bib` — compartilhadas entre os tipos

A compilação ocorre de **dentro do diretório do documento**:
```bash
cd tex/tcc_artigo && latexmk -pdf main.tex
```

Isso garante que todos os caminhos relativos (`figuras/`, `tabelas/`, `referencias.bib`) resolvam corretamente.

### Recursos Inclusos em Todos os Documentos

| Recurso | Descrição |
|---------|-----------|
| Citação indireta ABNT | `\cite{chave}` |
| Citação online ABNT | `\citeonline{chave}` |
| Notas de rodapé | `\footnote{texto}` |
| Figuras importadas | `\includegraphics{arquivo.eps}` |
| Tabelas modulares | `\input{tabelas/arquivo.tex}` |
| Equações numeradas | `\begin{equation}...\label{eq:nome}\end{equation}` |
| Ambiente {dica} | Bloco pedagógico azul itálico |
| Abstract ABNT | Ambiente `resumo` com formatação padrão |
| Palavras-chave | Ao final do resumo |
| Código fonte formatado | `\begin{lstlisting}` |

### Recursos Específicos por Tipo

| Tipo | Índice Remissivo | Apêndices | Ambiente Exercício |
|------|:-:|:-:|:-:|
| `tcc_artigo` | — | — | — |
| `tcc` | ✓ | ✓ (pipeline + resultados) | — |
| `artigo` | — | — | — |
| `dissertacao` | ✓ | ✓ (scripts, questionário) | — |
| `tese` | ✓ | ✓ (experimentos, folds, glossário) | — |
| `livro` | ✓ | ✓ (respostas, instalação) | ✓ |
| `relatorio` | — | — | — |
| `projeto` | — | — (cronograma incluso) | — |

### Exemplos Incluídos

O documento `tex/tcc_artigo/main.tex` (mais completo) demonstra:

| Recurso | Exemplo no Documento |
| ------------------------- | ------------------------------------------------ |
| Citação indireta ABNT | `\citeonline{hastie2009}` |
| Citação direta | `"texto" \cite[p.~119]{hastie2009}` |
| Notas de rodapé | `\footnote{explicação}` |
| Importação de tabelas | `\input{tabelas/tab_nome.tex}` |
| Importação de figuras EPS | `\includegraphics[width=...]{fig.eps}` |
| Figuras com subcaption | `\begin{subfigure}...\end{subfigure}` |
| Referências cruzadas | `Tabela~\ref{tab:nome}`, `Figura~\ref{fig:nome}` |
| Formatação de números | `\num{1000}` (com siunitx) |
| Código Python | `\begin{lstlisting}...\end{lstlisting}` |
| Bloco de dica | `\begin{dica}...\end{dica}` |
| Índice remissivo | `\index{termo}` (tcc, dissertacao, tese, livro) |
| Apêndices | `\chapter{Apêndice}` com tabelas e figuras |

---

## Tema de Demonstração: Previsão de Churn

Este repositório usa como exemplo a **previsão de churn de clientes** em telecomunicações (classificação binária). O pipeline inclui:

| Etapa | Script | Descrição |
| ----------------- | ---------------------------- | --------------------------------------- |
| Coleta | `01_coleta_dados.py` | Gera dataset fictício (1000 registros) |
| EDA | `02_analise_exploratoria.py` | Estatísticas descritivas, distribuições |
| Pré-processamento | `03_preprocessamento.py` | Limpeza, encoding, normalização |
| Treinamento | `04_treinamento_modelo.py` | LogReg, Random Forest, LightGBM |
| Avaliação | `05_avaliacao_modelo.py` | Métricas, ROC, tabelas LaTeX |
| Exportação | `06_exportar_figuras_eps.py` | Conversão PNG → EPS vetorial |

### Adaptando para Seu Projeto

1. **Substitua** o dataset em `dados/brutos/` pelo seu dataset
2. **Modifique** os scripts conforme seu pipeline
3. **Atualize** as variáveis, modelos e métricas
4. **Escolha ou crie** o tipo de documento em `tex/<tipo>/`
5. **Reescreva** o conteúdo do documento com seu texto
6. Execute `make pipeline` para regenerar figuras e tabelas

---

## Boas Práticas

### Organização de Código

- Scripts numerados sequencialmente
- Docstrings e comentários em português
- Funções modulares e reutilizáveis
- Constantes em MAIÚSCULAS no topo

### Versionamento (Código)

- Commits atômicos e descritivos
- `.gitignore` abrangente
- Resultados e métricas são regeneráveis (não versionamos binários gerados, apenas o código)

### Versionamento de Dados e Arquivos Grandes

O Git foi projetado para versionar texto (código-fonte), **não** para arquivos binários grandes. Estratégias recomendadas:

1. **Até ~50 MB:** Podem ficar no repositório. Dados brutos são read-only.
2. **De 50 MB a ~2 GB:** Use [Git LFS](https://git-lfs.com/).
3. **Acima de 2 GB:** Hospede em nuvem (Zenodo, Kaggle, AWS S3) e faça download automático no script `01_coleta_dados.py`, ou use [DVC](https://dvc.org/).

> **Importante:** O `.gitignore` já ignora modelos (`modelos/*.joblib`) e dados processados.

---

## Licença

Este repositório é disponibilizado como **template educacional** para uso acadêmico. Sinta-se à vontade para utilizar, modificar e compartilhar conforme necessário para seu projeto de pesquisa.

---

## Créditos

- **Modelo LaTeX:** Baseado na classe [abnTeX2](https://www.abntex.net.br/)
- **Dados:** Fictícios, gerados para fins de demonstração
- **Instituição:** Universidade Federal da Paraíba (UFPB) — Centro de Ciências Sociais Aplicadas (CCSA)
- **Áreas:** Projetado para Ciência de Dados, Economia e áreas afins.
