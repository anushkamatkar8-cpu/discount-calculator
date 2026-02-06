#start

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    elif price <= 0:
        return "The price should be greater than 0"
    elif not isinstance(discount, (int, float)):
        return "The discount should be a number"
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        return price - (price * discount / 100)
price=int(input('Enter the price:'))
discount=float(input('Enter discount:'))
print(apply_discount(price,discount))

#end

