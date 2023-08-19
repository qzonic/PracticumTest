import openai
from os import getenv

from dotenv import load_dotenv


load_dotenv()


TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
AI_TOKEN = getenv('AI_TOKEN')
openai.api_key = getenv('OPENAI_TOKEN')


OPENAI_SYSTEM_ROLE = 'system'
OPENAI_USER_ROLE = 'user'


LAST_SELFIE_MESSAGE = 'Последнее селфи'
SCHOOL_PHOTO_MESSAGE = 'Фото из школы'
POST_MESSAGE = 'Пост'
SOURCES_MESSAGE = 'Исходники'
VOICES_MESSAGE = 'Голосовые'


WHAT_IS_GPT = 'Что такое GPT?'
WHAT_IS_GPT_CALLBACK = 'GPT'
WHAT_IS_GPT_VOICE_ID = 'AwACAgIAAxkBAAICIWTfYQUSL074NCPO2xDcSwn1MecsAAISMQACjtT5SqrHR3LfG0BgMAQ'

DIFFERENCE_BETWEEN_SQL_NOSQL = 'В чём разница между SQL и NoSQL?'
DIFFERENCE_BETWEEN_SQL_NOSQL_CALLBACK = 'SQLNOSQL'
DIFFERENCE_BETWEEN_SQL_NOSQL_VOICE_ID = 'AwACAgIAAxkBAAICK2TfYWOg5vSoDfE_uVsG3mxg2tfdAAIiMQACjtT5St5kzr6pxqubMAQ'

FIRST_LOVE = 'История первой любви'
FIRST_LOVE_CALLBACK = 'LOVE'
FIRST_LOVE_VOICE_ID = 'AwACAgIAAxkBAAICHmTfYMTn3szT9vSI7imVhHpXFJ2bAAIsMQACjtT5Sr_X650HSo4FMAQ'


START_MESSAGE = """
Привет ✋🏻! Меня зовут Уралов Данил, я занимаюсь backend-разработкой
на языке Python. Для получения справки отправь мне /help
"""

COMMAND_INFO = """
{0} - {1}
{2}
"""

HELP_COMMAND = """
Помощь и справка о боте
Для того тобы получить информацию
о команде используй /help команда
"""

LAST_SELFIE_URL = 'https://clck.ru/35MGgf'
SCHOOL_PHOTO_URL = 'https://clck.ru/35MG5B'

POST = """
Приветствую! Я хочу рассказать тебе о моих главных увлечениях.
В жизни удовольствие мне приносят 2 вещи - программирование и авто.
1. Я могу часами сидеть за каким-то проектом и пытаться оживить его.
Люблю изучать новые технологии, а потом применять их в работе.

2. Автомобили - это еще одна моя страсть, я обожаю длинные поездки на машинах,
люблю когда внедорожник может позволить мне заехать в места, которые недоступны для глаз
многих других людей.
"""

SOURCES_ANSWER = """
Исходники можно найти по ссылке: <a href='https://github.com/qzonic/PracticumTest'>GitHub</a>
"""

OPENAI_SYSTEM_CONTENT = """
Представь, что ты наставник на курсе Python-разработчик для школьников 13-17 лет.
Отвечай максимально кратко (максимум 40 слов), предерживаясь роли преподавателя.
"""


OPENAI_CONTENT = [
    {'role': OPENAI_SYSTEM_ROLE, 'content': OPENAI_SYSTEM_CONTENT},
    {'role': OPENAI_USER_ROLE}
]

RECOGNITION_ERROR = 'Ошибка распознования голоса!'

OPENAI_ANSWER = 'Идет процесс генерации ответа на вопрос - {0}\nЭто может занять несколько секунд... 🤷‍'
