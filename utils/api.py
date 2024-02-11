from utils.http_method import Http_methods

"""Методы для тестирования Google maps api"""

base_url = 'https://rahulshettyacademy.com'  # базовая url
key = '?key=qaclick123'  # параметр для всех запросов


class Google_maps_api():
    """Метод создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'  # ресурс метода post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = '/maps/api/place/get/json'  # Ресурс метода Get
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод обновления локации"""

    @staticmethod
    def update_place(place_id):
        json_for_update_location = {

            "place_id": place_id,

            "address": "100 Lenina street, RU",

            "key": "qaclick123"

        }
        update_source = '/maps/api/place/update/json'  # Ресурс метода put
        update_url = base_url + update_source + key
        print(update_url)
        result_put = Http_methods.put(update_url, json_for_update_location)
        print(result_put.text)

        return result_put

    '''Метод удаления локации'''

    @staticmethod
    def delete_place(place_id):
        json_for_delete_location = {

            "place_id": place_id

        }

        delete_source = '/maps/api/place/delete/json'  # Ресурс метода Delete
        delete_url = base_url + delete_source + key
        print(delete_url)
        result_delete = Http_methods.delete(delete_url, json_for_delete_location)
        print(result_delete.text)

        return result_delete
