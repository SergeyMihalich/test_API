import json

import pytest

from Base.base import BaseClass, WebPage
from resources.data import pages_url as pu


class TestMainPagePositive(BaseClass, WebPage):
    def test_get_list_users(self, browser):
        endpoint = "?page=2"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'list_users')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_get_single_user(self, browser):
        endpoint = "/2"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_user')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_get_single_user_not_found(self, browser):
        endpoint = "/23"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_user_not_found')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_get_list_resource(self, browser):
        response = self.get_request(f"{pu['main_page']}{pu['unknown']}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'list_resource')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_get_single_resource(self, browser):
        endpoint = "/2"
        response = self.get_request(f"{pu['main_page']}{pu['unknown']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_resource')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_get_single_resource_not_found(self, browser):
        endpoint = "/23"
        response = self.get_request(f"{pu['main_page']}{pu['unknown']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_resource_not_found')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_post_create(self, browser):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.post_request(f"{pu['main_page']}{pu['users']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'create')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_put_update(self, browser):
        endpoint = "/2"
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = self.put_request(f"{pu['main_page']}{pu['users']}{endpoint}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'update')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_patch_update(self, browser):
        endpoint = "/2"
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = self.patch_request(f"{pu['main_page']}{pu['users']}{endpoint}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'patch_update')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_delete(self, browser):
        endpoint = "/2"
        response = self.del_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'delete')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_post_register_successful(self, browser):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = self.post_request(f"{pu['main_page']}{pu['register']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'register_successful')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_post_register_unsuccessful(self, browser):
        payload = {
            "email": "sydney@fife"
        }
        response = self.post_request(f"{pu['main_page']}{pu['register']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'register_unsuccessful')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_post_login_successful(self, browser):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = self.post_request(f"{pu['main_page']}{pu['login']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'login_successful')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_post_login_unsuccessful(self, browser):
        payload = {
            "email": "peter@klaven"
        }
        response = self.post_request(f"{pu['main_page']}{pu['login']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'login_unsuccessful')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'

    def test_get_delayed_response(self, browser):
        endpoint = "?delay=3"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'delayed_response')
        assert response.status_code == page_code, 'Статус код не совпадает'
        assert response.json() == json.loads(
            page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'


class TestMainPageNegative(BaseClass, WebPage):
    @pytest.mark.parametrize('n', range(5))
    def test_get_list_users(self, browser, n):
        endpoint = f"?page={n}"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'list_users')
        if n != 2:
            with pytest.raises(AssertionError):
                assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
                assert response.status_code == page_code, 'Статус код не совпадает'

    @pytest.mark.parametrize('n', [0, 'a', ''])
    def test_get_single_user(self, browser, n):
        endpoint = f"/{n}"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_user')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    def test_get_single_user_not_found(self, browser):
        endpoint = "/2"
        response = self.get_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_user_not_found')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    @pytest.mark.parametrize('n', [0, 1, 5, 10, 'a', ''])
    def test_get_single_resource(self, browser, n):
        endpoint = f"/{n}"
        response = self.get_request(f"{pu['main_page']}{pu['unknown']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_resource')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    def test_get_single_resource_not_found(self, browser):
        endpoint = "/2"
        response = self.get_request(f"{pu['main_page']}{pu['unknown']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'single_resource_not_found')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'
    @pytest.mark.parametrize('n', [{"name": "", "job": "leader"}, {"name": "morpheus", "job": ""}])
    def test_post_create(self, browser, n):

        response = self.post_request(f"{pu['main_page']}{pu['users']}", n)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'create')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    @pytest.mark.parametrize('n', [{"name": "", "job": "leader"}, {"name": "morpheus", "job": ""}])
    def test_put_update(self, browser, n):
        endpoint = "/2"
        response = self.put_request(f"{pu['main_page']}{pu['users']}{endpoint}", n)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'update')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    @pytest.mark.parametrize('n', [{"name": "", "job": "leader"}, {"name": "morpheus", "job": ""}])
    def test_patch_update(self, browser, n):
        endpoint = "/2"
        response = self.patch_request(f"{pu['main_page']}{pu['users']}{endpoint}", n)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'patch_update')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    @pytest.mark.parametrize('n', [2, 2, 50])
    def test_delete(self, browser, n):
        endpoint = f"/{n}"
        response = self.del_request(f"{pu['main_page']}{pu['users']}{endpoint}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'delete')
        with pytest.raises(json.decoder.JSONDecodeError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'
    @pytest.mark.parametrize('n', [{"email": "michael.lawson@reqres.in", "password": "pistol"},
                                   {"email": "", "password": "pistol"},
                                   {"email": "eve.holt@reqres.in", "password": ""}])

    def test_post_register_successful(self, browser, n):
        response = self.post_request(f"{pu['main_page']}{pu['register']}", n)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'register_successful')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    def test_post_register_unsuccessful(self, browser):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = self.post_request(f"{pu['main_page']}{pu['register']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'register_unsuccessful')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'
    @pytest.mark.parametrize('n', [{"email": "eve.holt@reqres.in", "password": "pistol"},
                                   {"email": "", "password": "pistol"},
                                   {"email": "eve.holt@reqres.in", "password": ""}])
    def test_post_login_successful(self, browser, n):
        response = self.post_request(f"{pu['main_page']}{pu['login']}", n)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'login_successful')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    def test_post_login_unsuccessful(self, browser):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = self.post_request(f"{pu['main_page']}{pu['login']}", payload)
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'login_unsuccessful')
        with pytest.raises(AssertionError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'

    @pytest.mark.parametrize('n', ["?deay=3", "?=3", "delay=3", "?delay=10", "?delay", "?delay3"])
    def test_get_delayed_response(self, browser, n):
        response = self.get_request(f"{pu['main_page']}{pu['users']}{n}")
        page_code, page_body = self.compare_with_page(pu['main_page'], browser, 'delayed_response')
        with pytest.raises(json.decoder.JSONDecodeError):
            assert response.json() == json.loads(
                page_body), f'Текст ответа не совпадает,\n{response.json()} - ответ запроса,\n{json.loads(page_body)} - ответ на сайте'
            assert response.status_code == page_code, 'Статус код не совпадает'