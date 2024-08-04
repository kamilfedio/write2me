from passlib.context import CryptContext

class Password:
    pwd_context = CryptContext(schemes=['argon2'])

    @staticmethod
    def get_password_hash(password: str) -> str:
        return Password.pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return Password.pwd_context.verify(plain_password, hashed_password)
    