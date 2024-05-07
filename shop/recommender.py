import redis
from django.conf import settings
from .models import Product
# Conexão com o Redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)
class Recommender:
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'
    def products_bought(self, products):
        product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # obter os outros produtos comprados com cada produto
                if product_id != with_id:
                    # pontuação de incremento para produtos adquiridos em conjunto
                    r.zincrby(self.get_product_key(product_id),
                              1,
                              with_id)
    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        print("Product IDs:", product_ids)
        if len(products) == 1:
            # apenas 1 produto
            suggestions = r.zrange(
                        self.get_product_key(product_ids[0]),
                        0, -1, desc=True)[:max_results]
        else:
            # gerar uma chave temporária
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = f'tmp_{flat_ids}'
            # vários produtos, combine pontuações de todos os produtos
            # armazenar o conjunto classificado resultante em uma chave temporária
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            print("Temporary Key:", tmp_key)
            # remova os IDs dos produtos para os quais a recomendação é
            r.zrem(tmp_key, *product_ids)
            # obtenha os IDs dos produtos por pontuação, classificação descendente
            suggestions = r.zrange(tmp_key, 0, -1,
                                desc=True)[:max_results]
            print("Suggestions:", suggestions)
            # remova a chave temporária
            r.delete(tmp_key)
        suggested_products_ids = [int(id) for id in suggestions]
        # obtenha sugestões de produtos e classifique por ordem de aparição
        suggested_products = list(Product.objects.filter(
            id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products                
    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))