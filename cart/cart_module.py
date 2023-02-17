from Shop.models import Product

CART_SESSION_ID = 'cart'


class Cart:

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            item['product'] = Product.objects.get(id=int(item['id']))
            item['total'] = int(item['price']) * int(item['quantity'])
            yield item

    def unique_id_generator(self, id, color, size):
        result = f'{id}-{color}-{size}'
        return result

    def add(self, product, quantity, color, size):
        unique = self.unique_id_generator(product.id, color, size)
        if unique not in self.cart:
            self.cart[unique] = {'quantity': 0, 'price': str(product.price), 'color': color, 'size': size, 'id': str(product.id)}

        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True



