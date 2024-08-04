from passlib.context import CryptContext

class Password:
    pwd_context = CryptContext(schemes=['argon2'])

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        hashing password
        Args:
            password (str): password string

        Returns:
            str: hashed pasword
        """
        return Password.pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        verifying password with checking plain password and hashed one
        Args:
            plain_password (str): user input password
            hashed_password (str): user password from database

        Returns:
            bool: if passwords are correct
        """
        return Password.pwd_context.verify(plain_password, hashed_password)
    