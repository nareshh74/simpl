simulation can be found in the function simulate() in src/controllers.py


requirements and system interfaces
1)  allow merchants to be onboarded with the amount of discounts they offer
    merchant = Merchant.sign_up(merchant_email="merchant@mail.com", discount = 1)



2)  allow merchants to change the discount they offer
    merchant = Merchant(merchant_email="merchant@email.com")
    merchant.update_discount(new_discount=2)




3)  allow users to be onboarded (name, email-id and credit-limit)
    user = User.sign_up(user_email="user@email.com", user_name="user name", credit_limit=100)



4)  allow a user to carry out a transaction of some amount with a merchant.
    user = User(user_email="user@email.com")
    merchant = Merchant(merchant_email="merchant@email.com")
    user.buy_from_merchant(merchant=merchant, transaction_amount=700)


5)  allow a user to pay back their dues (full or partial)
    user = User(user_email="user@email.com")
    user.pay_dues(due=10)




Reporting:
1)  how much discount we received from a merchant till date
    merchant = Merchant(merchant_email="merchant@email.com")
    total_discount = merchant.get_total_discount()


2)  which users have reached their credit limit
    users = domain_service.get_users_zero_credit_limit()


3)  total dues from all users 
    domain_service.get_due_balance_of_all_users()


****NOTE
currently entities - user, merchant are tightly dependant on service instance
was thinking about injecting it rther than using directly in function.
so we ll be able to mock at both service and repo levels.
But due to limited time i got to spend in this, didnt do that.
