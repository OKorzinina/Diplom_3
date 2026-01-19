import requests


class Ingredients:
    @staticmethod
    def ingredients_body():
        return {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}


class CreatedOrder:
    @staticmethod
    def created_order(token):
        response = requests.post(
            'https://stellarburgers.education-services.ru/api/orders',
            headers={"Authorization": token},
            json=Ingredients.ingredients_body()
        )
        
        data = response.json()
        return str(data["order"]["number"])