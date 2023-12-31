# Стек
<img src="https://img.shields.io/badge/Python-4169E1?style=for-the-badge"/> <img src="https://img.shields.io/badge/Aiogram-008000?style=for-the-badge"/> <img src="https://img.shields.io/badge/OPENAI-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FFMPEG-blue?style=for-the-badge"/>

## PracticumTest
### Бот для telegram.

Этот проет представляет из себя telegram-бота с возможностью просмотреть последнее селфи
автора, фото из старшей школы, прочитать небольшой пост об увлечениях,
прослушать голосовые сообщений от автора с ответами на 3 вопроса ("Что такое GPT?", "В чём разница между SQL и NoSQL?",
"История первой любви"). Так же этот бот может принимать голосовые сообщения и генерировать 
ответ с помощью ChatGPT.

Ответы на вопросы из задания 2 можно посмотреть по [ссылке](https://github.com/qzonic/PracticumTest/blob/master/Answers.md)

### Как запустить проект:

*Клонировать репозиторий и перейти в него в командной строке:*
```
https://github.com/qzonic/PracticumTest.git
```
```
cd PracticumTest/
```

В директории UrbanMedic нужно создать .env файл, в котором указывается, например, следующее:
```
TELEGRAM_TOKEN=
OPENAI_TOKEN=
```

Получить токен для бота [Telegram](https://t.me/BotFather)

Получить токен openai [OpenAI](https://platform.openai.com/account/api-keys)

Далее необходимо собрать Docker-контейнеры:
```
docker-compose up -d
```

Теперь бот запущен и готов к работе.


## Про деплой

Бот задеплоен на удаленный сервер и перейти к боту можно по [ссылке](https://t.me/practicum_for_me_bot)

### Автор
[![telegram](https://img.shields.io/badge/Telegram-Join-blue)](https://t.me/qzonic)
