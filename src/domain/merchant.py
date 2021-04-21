from .service import service


class Merchant(object):
    def __init__(self,
                 merchant_email: str = None,
                 discount: float = None) -> None:
        self.merchant_email = merchant_email
        self.__discount = discount

    @classmethod
    def sign_up(cls, merchant_email: str = None, discount: float = None):
        service.create_merchant(merchant_email=merchant_email,
                                discount=discount)
        return cls(merchant_email=merchant_email)

    def update_discount(self, new_discount: float = None):
        service.update_discount(merchant_email=self.merchant_email,
                                new_discount=new_discount)

    def get_total_discount(self):
        return service.get_discounts_of_merchant(self.merchant_email)
