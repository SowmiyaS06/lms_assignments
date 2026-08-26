def braintree_success_page(data):
    print("Braintree payment successful")
    print(data)

    return "/thank-you"