from .service import service
from .merchant import Merchant


class User(object):
    def __init__(self,
                 user_email: str = None,
                 user_name: str = None,
                 credit_limit: float = None) -> None:
        self.__user_email = user_email
        self.__user_name = user_name
        self.__credit_limit = credit_limit

    @classmethod
    def sign_up(cls,
                user_email: str = None,
                user_name: str = None,
                credit_limit: float = None):
        service.create_user(user_email=user_email,
                            user_name=user_name,
                            credit_limit=credit_limit)
        return cls(user_email=user_email)

    def pay_dues(self, due: float = None):
        service.update_user_due(user_email=self.__user_email, due=due)

    def buy_from_merchant(self,
                          merchant: Merchant = None,
                          transaction_amount: float = None):
        service.make_transaction(user_email=self.__user_email,
                                 merchant_email=merchant.merchant_email,
                                 transaction_amount=transaction_amount)
