from decouple import config
from dotenv import load_dotenv


load_dotenv()

class Settings:
    PROJECT_TITLE:  str = "UNOPS DATA INTEGRATION"
    PORJECT_DESCRIPTION: str = "A data integration system that helps UNOPS send their data to USI system"
    PROJECT_VERSION :str = "0.1"

    BULKUPLOADFORMDATA_DESCRIPTION = "Create form data_in in the server using an xlsx, json , csv or xml format"
    BULKUPLOADFORMDATA_SUMMARY = "Create form data_in in the server using an xlsx, json , csv or xml format"

    QUESTIONS_SUMMARY="create a list of questions on our server and the output server"
    QUESTIONS_DESCRIPTION="create a list of questions on our server and the output server"

    QUESTION_UPDATE_SUMMARY = 'Update a question'
    QUESTION_UPDATE_DESCRIPTION = 'Update a question'

    FORMS_DESCRIPTION = "Create a list of forms on our server and the output server"
    FORMS_SUMMARY = "Create a list of forms on our server and the output server"

    FORM_QUESTIONS_DESCRIPTION = "Create a list of questions for a specific form using an excel "
    FORM_QUESTIONS_SUMMARY = "Create a list of questions for a specific form using an excel "

    CREATE_USER_DESCRIPTION = "create user in the db with hashed password"
    CREATE_USER_SUMMARY = "create user in the db with hashed password"

    GET_USER_DESCRIPTION = "get user by username or email in the db with hashed password"
    GET_USER_SUMMARY = "get user by username or email in the db with hashed password"

    GET_USERS_DESCRIPTION = "get users in the db with hashed password"
    GET_USERS_SUMMARY = "get users in the db with hashed password"

    UPDATE_USER_DESCRIPTION = "admin can Update any user "
    UPDATE_USER_SUMMARY = "admin can Update any user"

    DELETE_USER_DESCRIPTION = "admin can DELETE any user "
    DELETE_USER_SUMMARY = "admin can DELETE any user"

    REGISTRATION_DESCRIPTION = 'register normal users on the system'
    REGISTRATION_SUMMARY = 'register normal users on the system'

    REGISTER_ADMIN_DESCRIPTION = 'register an admin on the system'
    REGISTER_ADMIN_SUMMARY = 'register an admin on the system'

    ALGORITHM = config('ALG', cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES = config('TOKEN_EXPIRING',cast=int)
    SECRET_KEY : str = config('SECRET_KEY',cast=str)

    LOGIN_DESCRIPTION = 'Basic login system without differencing the admin or normal users'
    LOGIN_SUMMARY = 'Basic login system without differencing the admin or normal users'

    DOCS_URL = '/'






settings = Settings()
