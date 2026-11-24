#!/bin/bash
# Публикация site/ на GitHub Pages (ветка gh-pages). Нужен вход: gh auth login
set -e
cd "$(dirname "$0")"
REPO=perez-model
OWNER=$(gh api user -q .login)
gh auth setup-git
if ! gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  gh repo create "$REPO" --public --description "Perez, universal model. Landing page"
fi
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$OWNER/$REPO.git"
git push -u origin main
git push origin "$(git subtree split --prefix site main)":refs/heads/gh-pages --force
gh api -X POST "repos/$OWNER/$REPO/pages" -f "source[branch]=gh-pages" -f "source[path]=/" >/dev/null 2>&1 || true
echo "https://$OWNER.github.io/$REPO/"
