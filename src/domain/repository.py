from .repository_implementation import RepositoryImplementation, InMemoryRepositoryImplementation


class Repository(object):
    def __init__(
            self,
            repository_implementation: RepositoryImplementation = None
    ) -> None:
        self.__repository_implementation = repository_implementation

    def create_user(self,
                    user_email: str = None,
                    user_name: str = None,
                    credit_limit: float = None):
        self.__repository_implementation.create_user(user_email=user_email,
                                                     user_name=user_name,
                                                     credit_limit=credit_limit)

    def create_merchant(self,
                        merchant_email: str = None,
                        discount: float = None):
        self.__repository_implementation.create_merchant(
            merchant_email=merchant_email, discount=discount)

    def make_transaction(self,
                         user_email: str = None,
                         merchant_email: str = None,
                         transaction_amount: float = None):
        self.__repository_implementation.make_transaction(
            user_email=user_email,
            merchant_email=merchant_email,
            transaction_amount=transaction_amount)

    def update_discount(self,
                        merchant_email: str = None,
                        new_discount: float = None):
        self.__repository_implementation.update_discount(
            merchant_email=merchant_email, new_discount=new_discount)

    def update_user_due(self, user_email: str = None, due: float = None):
        self.__repository_implementation.update_user_due(user_email=user_email,
                                                         due=due)

    def get_discounts_of_merchant(self, merchant_email: str = None) -> float:
        return self.__repository_implementation.get_discounts_of_merchant(
            merchant_email=merchant_email)

    def get_due_balance_of_all_users(self) -> list:
        return self.__repository_implementation.get_due_balance_of_all_users()

    def get_users_zero_credit_limit(self) -> list:
        return self.__repository_implementation.get_users_zero_credit_limit()


inmemory_repository_implementation = InMemoryRepositoryImplementation()
repository = Repository(
    repository_implementation=inmemory_repository_implementation)
