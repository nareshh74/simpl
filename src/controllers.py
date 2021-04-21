from .domain import User, Merchant, domain_service


# each function represents a process
def create_user(user_email: str = None,
                user_name: str = None,
                credit_limit: float = None):
    _ = User.sign_up(user_email=user_email,
                     user_name=user_name,
                     credit_limit=credit_limit)


def create_merchant(merchant_email: str = None, discount: float = None):
    _ = Merchant.sign_up(merchant_email=merchant_email, discount=discount)


def make_transaction(user_email: str = None,
                     merchant_email: str = None,
                     transaction_amount: float = None):
    user = User(user_email=user_email)
    merchant = Merchant(merchant_email=merchant_email)
    user.buy_from_merchant(merchant=merchant,
                           transaction_amount=transaction_amount)


def update_discount(merchant_email: str = None, new_discount: float = None):
    merchant = Merchant(merchant_email=merchant_email)
    merchant.update_discount(new_discount=new_discount)


def update_user_due(user_email: str = None, due: float = None):
    user = User(user_email=user_email)
    user.pay_dues(due=due)


def get_discounts_of_merchant(merchant: Merchant = None) -> float:
    return merchant.get_total_discount()


def get_due_balance_of_all_users() -> list:
    return domain_service.get_due_balance_of_all_users()


def get_users_zero_credit_limit() -> list:
    return domain_service.get_users_zero_credit_limit()


# simulation
def simulate():
    user1 = User.sign_up(user_email="user1@mail.com",
                         user_name="user1",
                         credit_limit=1000)
    user2 = User.sign_up(user_email="user2@mail.com",
                         user_name="user2",
                         credit_limit=500)
    merchant1 = Merchant.sign_up(merchant_email="merchant1@mail.com",
                                 discount=0.5)
    merchant2 = Merchant.sign_up(merchant_email="merchant2@mail.com",
                                 discount=1)

    user2.buy_from_merchant(merchant=merchant1, transaction_amount=700)
    user2.buy_from_merchant(merchant=merchant1, transaction_amount=200)
    user1.buy_from_merchant(merchant=merchant2, transaction_amount=1000)

    print("report - users due balance")
    print(domain_service.get_due_balance_of_all_users())

    print("report - users with exhausted credits")
    print(domain_service.get_users_zero_credit_limit())

    user1.pay_dues(due=1000)

    print("report - users due balance")
    print(domain_service.get_due_balance_of_all_users())

    print("report - total merchant discounts")
    print(f"merchant1 - {merchant1.get_total_discount()}")
    print(f"merchant2 - {merchant2.get_total_discount()}")

    print("report - users with exhausted credits")
    print(domain_service.get_users_zero_credit_limit())
