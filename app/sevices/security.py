from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/auth/token")