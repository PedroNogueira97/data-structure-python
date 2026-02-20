# Git Workflow

## 🌿 Branch Naming

### Formato

```
<tipo>/<escopo-curto>
```

### Tipos permitidos

| Tipo | Quando usar |
|------|-------------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `refactor` | Refatoração sem mudança de comportamento |
| `chore` | Tarefas de manutenção, configs, dependências |
| `docs` | Documentação |
| `test` | Adição ou ajuste de testes |
| `hotfix` | Correção urgente em produção |

### Regras

- Letras minúsculas e hífens (`-`), sem espaços ou underscores
- Escopo curto e descritivo (máximo 4 palavras)
- Sem caracteres especiais

### Exemplos

```
feat/user-authentication
fix/login-redirect-error
refactor/payment-service
chore/update-dependencies
docs/api-endpoints
```

---

## ✅ Commits

Seguindo o padrão **Conventional Commits**.

### Formato

```
<tipo>(<escopo>): <descrição curta>

[corpo opcional]

[rodapé opcional]
```

### Regras

- Descrição no **imperativo**, em português ou inglês (manter um padrão no projeto)
- Máximo de **72 caracteres** na primeira linha
- Corpo separado da descrição por uma linha em branco
- Referenciar issues quando aplicável: `Closes #123`

### Exemplos

```
feat(auth): adiciona autenticação com Google OAuth

fix(cart): corrige cálculo de desconto para cupons expirados

refactor(api): simplifica camada de serviço do usuário

chore(deps): atualiza React para v19

docs(readme): adiciona instruções de instalação

test(payment): adiciona testes unitários para cálculo de frete
```

---

## 🔀 Pull Request

### Título

Seguir o mesmo padrão de commit:

```
<tipo>(<escopo>): <descrição curta>
```

### Template

```markdown
## 📋 Descrição
<!-- Descreva o que foi feito e por quê -->


## 🔗 Issue relacionada
Closes #


## 🧪 Como testar
<!-- Passo a passo para validar as mudanças -->
1. 
2. 
3. 

## 📸 Screenshots (se aplicável)
<!-- Adicione prints ou gravações de tela -->

## ✅ Checklist
- [ ] O código segue os padrões do projeto
- [ ] Testes foram adicionados ou atualizados
- [ ] A documentação foi atualizada (se necessário)
- [ ] Não há console.log ou código de debug
- [ ] A branch está atualizada com a branch base
```

### Regras gerais

- PRs devem ser pequenos e focados em uma única responsabilidade
- Branch base padrão: `main` (ou `develop` se o projeto usar Gitflow)
- Mínimo de 1 aprovação antes do merge
- Squash merge para manter histórico limpo

---

## 🔁 Fluxo Resumido

```
1. Criar branch     →  feat/minha-feature
2. Desenvolver      →  commits pequenos e descritivos
3. Push             →  git push origin feat/minha-feature
4. Abrir PR         →  título + template preenchido
5. Review           →  aguardar aprovação
6. Merge            →  squash merge na main
7. Deletar branch   →  limpeza após merge
```
