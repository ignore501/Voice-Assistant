from google.cloud import dialogflow
import os


# Чтобы привязать Dialogflow потребуется залогиниться через сервис аккаунт
# Скачиваем свой файл json с сайта googlecloud, указываем путь до файла
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'eva-jcy9-b782460e4394.json'
# ID проекта, к которому будем обращаться
PROJECT_ID = 'eva-jcy9'
# ID сессии, можно указать любой в формате str
SESSION_ID = 'eva'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(PROJECT_ID, SESSION_ID)


# Функция принимает запрос для dialogflow
# Возвращает текст ответа и событие
def dialog_flow_answer(text):
    text_input = dialogflow.TextInput(text=text, language_code='ru-RU')
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    result = response.query_result.fulfillment_text
    display_name = response.query_result.intent.display_name
    return result, display_name
