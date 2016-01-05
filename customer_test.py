from unittest import TestCase
from customer import Customer


class CustomerTest(TestCase):

    def test_when_create_customer_then_customer_should_have_name_and_lastName_notempty(self):
        customer = Customer('vero', 'rodriguez')
        assert customer.get_name()
        assert customer.get_last_name()

    def test_when_create_customer_with_parameters_empty_then_thrown_exception(self):
        with self.assertRaises(Exception):
            customer = Customer('', '')

    def test_when_create_customer_with_parameters_none_then_thrown_exception(self):
        with self.assertRaises(Exception):
            customer = Customer(None, None)

    def test_when_create_customer_with_identifier_type_celula_then_identifier_type_should_cedula_passport_ruc(self):
        customer = Customer('vero', 'rodri', 'celula')
        self.assertIn(customer.get_identifier_type(), ['celula', 'passport', 'ruc'])

    def test_when_create_customer_with_identifier_type_passport_then_identifier_type_should_cedula_passport_ruc(self):
        customer = Customer('vero', 'rodri', 'passport')
        self.assertIn(customer.get_identifier_type(), ['celula', 'passport', 'ruc'])

    def test_when_create_customer_with_identifier_type_unknown_then_throw_exception(self):
        with self.assertRaises(Exception):
            customer = Customer('vero', 'rodri', 'carnet')




