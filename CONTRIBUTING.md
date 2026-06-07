# Contribuindo para o Repositório-Modelo Acadêmico

Obrigado pelo seu interesse em contribuir! Este projeto visa auxiliar estudantes do Centro de Ciências Sociais Aplicadas (CCSA) da UFPB (nas áreas de Ciência de Dados, Economia e afins) a construírem trabalhos acadêmicos estruturados e reprodutíveis.

Como este é um projeto voltado à comunidade acadêmica, toda ajuda para aprimorá-lo é bem-vinda: correções de bugs, melhorias no pipeline de dados ou aprimoramentos nos templates LaTeX.

## Como posso contribuir?

### 1. Reportando Bugs ou Sugerindo Melhorias
Caso encontre algum erro de formatação (ex: regras da ABNT), falha no pipeline Python, ou tenha uma ideia para melhorar a experiência de uso do modelo:
- Abra uma **Issue** no repositório explicando detalhadamente o problema ou sugestão.
- Se for um bug, inclua logs de erro ou descrições de onde o código ou a compilação falhou.

### 2. Contribuindo com Código / LaTeX
Se você deseja implementar uma correção ou adicionar um novo recurso (como um novo template de documento):
1. Faça um **Fork** deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/minha-melhoria`).
3. Faça as alterações seguindo as boas práticas descritas abaixo.
4. Faça commit das suas alterações (`git commit -m 'feat: adiciona novo template para relatórios'`).
5. Faça o push para a branch (`git push origin feature/minha-melhoria`).
6. Abra um **Pull Request (PR)** e descreva o que foi feito.

## Boas Práticas e Padrões

Para mantermos a consistência e qualidade do template educacional, pedimos que observe os seguintes pontos:

- **Código Python:**
  - Utilize a formatação padrão da ferramenta `ruff` executando `make format`.
  - Mantenha os scripts organizados numericamente (ex: `01_...`, `02_...`).
  - Escreva docstrings didáticas em português e utilize type hints, visto que este template é lido por estudantes que estão aprendendo a programar.

- **Código LaTeX:**
  - Garanta que qualquer código LaTeX submetido seja compatível com a classe `abntex2`.
  - Evite bibliotecas que causam conflitos frequentes.
  - Sempre rode `make latex-all` localmente para garantir que sua contribuição não quebrou a compilação dos outros formatos de trabalho acadêmico já existentes.

- **Boas práticas de Git:**
  - Utilize mensagens de commit semânticas e atômicas (ex: `fix: corrige largura da tabela no dicionário de dados`).

Sua colaboração ajuda centenas de estudantes a alcançarem a excelência técnica na entrega de seus trabalhos!
