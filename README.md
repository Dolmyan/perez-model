# Perez, лендинг модели

Статический сайт в папке `site/` (один `index.html` + `photos.js` + `img/`).

## Добавить фото
1. Положи фото в папки:
   - `photos/hero/` главное фото (берётся первое по алфавиту)
   - `photos/fashion/` одежда, lookbook, e-commerce
   - `photos/body/` тело, спорт, бельё
   - `photos/image/` лицо, портрет, бьюти
2. Запусти `python3 build.py` (уменьшит фото и обновит галерею).
Порядок в галерее = порядок имён файлов (01-..., 02-...). Пустые категории показывают плашку «soon».

## Контакты
В `site/index.html` найди блок `КОНТАКТЫ` (в конце файла) и впиши email, Instagram, WhatsApp, Telegram.

## Посмотреть локально
`python3 -m http.server 8765 --directory site` и открыть http://localhost:8765

## Публикация
Папку `site/` можно залить на Netlify / Vercel / GitHub Pages как есть, сборки не нужно.
