# W.T.S HUB — Деплой инструкция

## Структура файлов

```
/
├── index.html          ← Лендинг (на сервер)
├── music.mp3           ← Фоновая музыка (на сервер)
├── Untitled_YOECU2A6.mp4 ← Фоновое видео (на сервер)
├── bot.py              ← Telegram бот
└── requirements.txt    ← Зависимости бота
```

---

## 1. Деплой лендинга (wtswalletbot.pro)

Загрузи на сервер/хостинг:
- `index.html`
- `music.mp3`
- `Untitled_YOECU2A6.mp4`

Корень сайта должен отдавать `index.html`.

---

## 2. Запуск бота

### На VPS/сервере:

```bash
# Установить Python 3.10+
pip install -r requirements.txt
python bot.py
```

### Через systemd (автозапуск):

```ini
[Unit]
Description=WTS Telegram Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/bot.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

```bash
systemctl enable wts-bot
systemctl start wts-bot
```

---

## 3. Логика защиты ссылки на основной чат

- Ссылка хранится в коде в base64 (лёгкая обфускация от ботов-парсеров)
- Пользователю выдаётся **3 попытки** получить ссылку
- Таймер **10 минут** стартует при первом нажатии
- Таймер **не сбрасывается** при перезагрузке страницы (localStorage)
- По истечении попыток — сообщение с просьбой обратиться в @wtsproject

### Чтобы сменить ссылку (при ротации):
В `index.html` найди строку:
```js
const REAL_LINK_B64 = btoa("https://t.me/+WnmBiSONJkY4NmVl");
```
Замени ссылку внутри `btoa(...)` на новую.
