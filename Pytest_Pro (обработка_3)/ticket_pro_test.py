import pytest
from ticket_pro import ticket_price

ticket_price_parametrize = [(0,"Бесплатно"),
                            (1,"Бесплатно"),
                            (7, "100 рублей"),
                            (18, "200 рублей"),
                            (25, "300 рублей"),
                            (60, "Бесплатно"),
                            (0.5, "Бесплатно"),
                            (-1, "Ошибка")
                            ]

@pytest.mark.parametrize("parametrize, excepted",
                         ticket_price_parametrize
                         )
class TestTicketPricePro:
    def test_price_pro(self, parametrize, excepted):
        assert ticket_price(parametrize==excepted), "Ошибка параметра"
