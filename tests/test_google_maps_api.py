import json

from utils.cheking import Cheking
import requests
from utils.api import Google_maps_api
import allure

"""Создание, изменение и удаление новой локации"""


@allure.epic('Test create new location')
class Test_create_place():
    @allure.description('Test create, update, delete new place')
    def test_create_new_place(self):
        print('Метод Post')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print('Метод Get')
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'accuracy', '50')

        print('Метод Put')
        result_put = Google_maps_api.update_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод Get Put')
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Cheking.check_json_value(result_get, "language","French-IN")

        print('Метод Delete')
        result_delete = Google_maps_api.delete_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print('Метод Get Delete')
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get, ['msg'])
        Cheking.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")

        print('Тестирование создания, изменения и удаления новой локации прошло успешно')
