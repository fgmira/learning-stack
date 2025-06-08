from abc import ABC, abstractmethod
from typing import Any, Dict


# Interface comum para processamento de pagamentos
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> bool:
        pass


# Serviços externos com interfaces diferentes
class PayPalService:
    def makePayment(self, amount: float, currency: str, email: str) -> Dict[str, Any]:
        # Simulação da API do PayPal
        print(f"PayPal: Processing ${amount} {currency} for {email}")
        return {"status": "success", "transaction_id": "pp_12345"}


class StripeService:
    def charge(self, price_in_cents: int, card_token: str) -> Dict[str, Any]:
        # Simulação da API do Stripe
        print(f"Stripe: Charging {price_in_cents} cents with token {card_token}")
        return {"paid": True, "id": "ch_1234567890"}


class PagSeguroService:
    def processPagamento(
        self, valor: float, tipo_cartao: str, dados_cartao: Dict[str, str]
    ) -> Dict[str, Any]:
        # Simulação da API do PagSeguro
        print(f"PagSeguro: Processando R${valor} via {tipo_cartao}")
        return {"sucesso": True, "codigo_transacao": "ps_98765"}


# Adapters para cada serviço
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_service: PayPalService):
        self.paypal_service = paypal_service

    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> bool:
        try:
            email = payment_data.get("email")
            currency = payment_data.get("currency", "USD")

            result = self.paypal_service.makePayment(amount, currency, email)
            return result.get("status") == "success"
        except Exception as e:
            print(f"PayPal payment failed: {e}")
            return False


class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_service: StripeService):
        self.stripe_service = stripe_service

    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> bool:
        try:
            card_token = payment_data.get("card_token")
            price_in_cents = int(amount * 100)  # Converter para centavos

            result = self.stripe_service.charge(price_in_cents, card_token)
            return result.get("paid", False)
        except Exception as e:
            print(f"Stripe payment failed: {e}")
            return False


class PagSeguroAdapter(PaymentProcessor):
    def __init__(self, pagseguro_service: PagSeguroService):
        self.pagseguro_service = pagseguro_service

    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> bool:
        try:
            tipo_cartao = payment_data.get("card_type", "credito")
            dados_cartao = {
                "numero": payment_data.get("card_number"),
                "cvv": payment_data.get("cvv"),
                "titular": payment_data.get("cardholder_name"),
            }

            result = self.pagseguro_service.processPagamento(
                amount, tipo_cartao, dados_cartao
            )
            return result.get("sucesso", False)
        except Exception as e:
            print(f"PagSeguro payment failed: {e}")
            return False


# Sistema principal que usa os adapters
class ECommerceSystem:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_order_payment(
        self, amount: float, payment_data: Dict[str, Any]
    ) -> bool:
        print(f"Processing payment of ${amount}")
        success = self.payment_processor.process_payment(amount, payment_data)

        if success:
            print("Payment processed successfully!")
        else:
            print("Payment failed!")

        return success


# Exemplo de uso
def main():
    # Criando instâncias dos serviços externos
    paypal = PayPalService()
    stripe = StripeService()
    pagseguro = PagSeguroService()

    # Criando adapters
    paypal_adapter = PayPalAdapter(paypal)
    stripe_adapter = StripeAdapter(stripe)
    pagseguro_adapter = PagSeguroAdapter(pagseguro)

    # Testando PayPal
    ecommerce_paypal = ECommerceSystem(paypal_adapter)
    paypal_data = {"email": "user@example.com", "currency": "USD"}
    ecommerce_paypal.process_order_payment(100.0, paypal_data)

    print("-" * 50)

    # Testando Stripe
    ecommerce_stripe = ECommerceSystem(stripe_adapter)
    stripe_data = {"card_token": "tok_visa"}
    ecommerce_stripe.process_order_payment(75.50, stripe_data)

    print("-" * 50)

    # Testando PagSeguro
    ecommerce_pagseguro = ECommerceSystem(pagseguro_adapter)
    pagseguro_data = {
        "card_type": "credito",
        "card_number": "1234567890123456",
        "cvv": "123",
        "cardholder_name": "João Silva",
    }
    ecommerce_pagseguro.process_order_payment(200.0, pagseguro_data)


if __name__ == "__main__":
    main()
