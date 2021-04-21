from abc import abstractmethod, ABC
from typing import List


class RepositoryImplementation(ABC):
    @abstractmethod
    def create_user(_,
                    user_email: str = None,
                    user_name: str = None,
                    credit_limit: float = None):
        pass

    @abstractmethod
    def create_merchant(_, merchant_email: str = None, discount: float = None):
        pass

    @abstractmethod
    def make_transaction(_,
                         user_email: str = None,
                         merchant_email: str = None,
                         transaction_amount: float = None):
        pass

    @abstractmethod
    def update_discount(_,
                        merchant_email: str = None,
                        new_discount: float = None):
        pass

    @abstractmethod
    def update_user_due(_, user_email: str = None, due: float = None):
        pass

    @abstractmethod
    def get_discounts_of_merchant(_, merchant_email: str = None):
        pass

    @abstractmethod
    def get_due_balance_of_all_users(_):
        pass

    @abstractmethod
    def get_users_zero_credit_limit(_):
        pass


class InMemoryRepositoryImplementation(RepositoryImplementation):
    def __init__(self) -> None:
        self.__user_map = {}
        self.__merchant_map = {}

    def create_user(self,
                    user_email: str = None,
                    user_name: str = None,
                    credit_limit: float = None):
        if user_email in self.__user_map:
            print("Email already registered as user")
            return
        self.__user_map[user_email] = {
            "user_name": user_name,
            "credit_limit": credit_limit,
            "bought": 0,
            "payback": 0
        }
        print(f"user - {user_email} created")

    def create_merchant(self,
                        merchant_email: str = None,
                        discount: float = None):
        if merchant_email in self.__merchant_map:
            print("Email already registered as merchant")
            return
        self.__merchant_map[merchant_email] = {
            "discount": discount,
            "profit": 0
        }
        print(f"merchant - {merchant_email} created")

    def make_transaction(self,
                         user_email: str = None,
                         merchant_email: str = None,
                         transaction_amount: float = None):
        balance = self.__user_map[user_email]["credit_limit"] + self.__user_map[
            user_email]["payback"] - self.__user_map[user_email]["bought"]
        if balance < transaction_amount:
            print("Not enough credits available")
            return
        self.__user_map[user_email]["bought"] += transaction_amount
        self.__merchant_map[merchant_email]["profit"] += (
            (self.__merchant_map[merchant_email]["discount"] *
             transaction_amount) / 100)
        print(
            f"transaction success between user - {user_email} and merchant - {merchant_email}"
        )

    def update_discount(self,
                        merchat_email: str = None,
                        new_discount: float = None):
        self.__merchant_map[merchat_email]["discount"] = new_discount
        print(f"updated discount of merchant {merchat_email}")

    def update_user_due(self, user_email: str = None, due: float = None):
        self.__user_map[user_email]["payback"] += due
        print(f"updated due of user {user_email}")

    def get_discounts_of_merchant(self, merchant_email: str = None) -> float:
        return self.__merchant_map[merchant_email]["profit"]

    def get_due_balance_of_all_users(self) -> List:
        user_list = []
        for user_email in self.__user_map.keys():
            balance = self.__user_map[user_email]["bought"] - self.__user_map[
                user_email]["payback"]
            due = self.__user_map[user_email][
                "credit_limit"] - balance if balance < self.__user_map[
                    user_email]["credit_limit"] else 0
            user_list.append({
                user_email:
                self.__user_map[user_email]["credit_limit"] - due
            })
        return user_list

    def get_users_zero_credit_limit(self) -> List:
        user_list = []
        for user_email in self.__user_map.keys():
            balance = self.__user_map[user_email][
                "credit_limit"] + self.__user_map[user_email][
                    "payback"] - self.__user_map[user_email]["bought"]
            if balance <= 0:
                user_list.append(user_email)
        return user_list
