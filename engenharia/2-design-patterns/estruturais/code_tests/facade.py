import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional


# Data classes para estruturar informações
@dataclass
class Product:
    id: str
    name: str
    price: float
    category: str
    description: str
    weight: float


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float


@dataclass
class PaymentInfo:
    card_number: str
    expiry_date: str
    cvv: str
    cardholder_name: str
    billing_address: Dict[str, str]


@dataclass
class Address:
    street: str
    city: str
    state: str
    zip_code: str
    country: str


@dataclass
class OrderResult:
    success: bool
    order_id: Optional[str]
    total_amount: float
    estimated_delivery: Optional[datetime]
    tracking_number: Optional[str]
    error_message: Optional[str] = None


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


# Subsistemas complexos (simulados)
class ProductCatalogService:
    def __init__(self):
        # Simulação de um banco de dados de produtos
        self.products = {
            "LAPTOP001": Product(
                "LAPTOP001",
                "Gaming Laptop",
                1299.99,
                "Electronics",
                "High-performance gaming laptop",
                2.5,
            ),
            "MOUSE001": Product(
                "MOUSE001",
                "Wireless Mouse",
                29.99,
                "Electronics",
                "Ergonomic wireless mouse",
                0.2,
            ),
            "BOOK001": Product(
                "BOOK001",
                "Python Programming",
                39.99,
                "Books",
                "Learn Python programming",
                0.5,
            ),
            "SHIRT001": Product(
                "SHIRT001",
                "Cotton T-Shirt",
                19.99,
                "Clothing",
                "100% cotton t-shirt",
                0.3,
            ),
        }

    def get_product(self, product_id: str) -> Optional[Product]:
        print(f"CatalogService: Fetching product {product_id}")
        return self.products.get(product_id)

    def validate_product_exists(self, product_id: str) -> bool:
        exists = product_id in self.products
        print(f"CatalogService: Product {product_id} exists: {exists}")
        return exists

    def get_product_price(self, product_id: str) -> float:
        product = self.products.get(product_id)
        if product:
            print(f"CatalogService: Price for {product_id}: ${product.price}")
            return product.price
        return 0.0


class InventoryService:
    def __init__(self):
        # Simulação de níveis de estoque
        self.stock_levels = {
            "LAPTOP001": 15,
            "MOUSE001": 50,
            "BOOK001": 100,
            "SHIRT001": 25,
        }
        self.reservations = {}

    def check_availability(self, product_id: str, quantity: int) -> bool:
        available = self.stock_levels.get(product_id, 0)
        is_available = available >= quantity
        print(
            f"InventoryService: {product_id} availability check - needed: {quantity}, available: {available}, result: {is_available}"
        )
        return is_available

    def reserve_items(self, product_id: str, quantity: int, order_id: str) -> bool:
        if self.check_availability(product_id, quantity):
            reservation_id = str(uuid.uuid4())
            self.reservations[reservation_id] = {
                "product_id": product_id,
                "quantity": quantity,
                "order_id": order_id,
                "timestamp": datetime.now(),
            }
            self.stock_levels[product_id] -= quantity
            print(
                f"InventoryService: Reserved {quantity} units of {product_id} for order {order_id}"
            )
            return True
        print(
            f"InventoryService: Failed to reserve {quantity} units of {product_id} - insufficient stock"
        )
        return False

    def release_reservation(self, order_id: str) -> bool:
        for res_id, reservation in self.reservations.items():
            if reservation["order_id"] == order_id:
                product_id = reservation["product_id"]
                quantity = reservation["quantity"]
                self.stock_levels[product_id] += quantity
                del self.reservations[res_id]
                print(f"InventoryService: Released reservation for order {order_id}")
                return True
        return False


class PaymentService:
    def __init__(self):
        self.processed_payments = {}

    def validate_payment_info(self, payment_info: PaymentInfo) -> bool:
        # Simulação de validação de cartão
        is_valid = (
            len(payment_info.card_number) == 16
            and len(payment_info.cvv) == 3
            and payment_info.cardholder_name.strip() != ""
        )
        print(f"PaymentService: Payment info validation result: {is_valid}")
        return is_valid

    def process_payment(
        self, amount: float, payment_info: PaymentInfo
    ) -> Dict[str, Any]:
        print(f"PaymentService: Processing payment of ${amount:.2f}")

        if not self.validate_payment_info(payment_info):
            return {"success": False, "error": "Invalid payment information"}

        # Simulação de processamento
        if payment_info.card_number.startswith("4111"):  # Simulação de cartão válido
            transaction_id = str(uuid.uuid4())
            self.processed_payments[transaction_id] = {
                "amount": amount,
                "timestamp": datetime.now(),
                "status": "completed",
            }
            print(
                f"PaymentService: Payment successful - Transaction ID: {transaction_id}"
            )
            return {"success": True, "transaction_id": transaction_id}
        else:
            print("PaymentService: Payment failed - Card declined")
            return {"success": False, "error": "Card declined"}


class ShippingService:
    def __init__(self):
        self.shipments = {}
        self.shipping_rates = {"standard": 5.99, "express": 12.99, "overnight": 24.99}

    def calculate_shipping_cost(
        self, items: List[OrderItem], address: Address
    ) -> float:
        # Simulação de cálculo baseado em peso e distância
        total_weight = len(items) * 0.5  # Peso simulado
        base_cost = self.shipping_rates["standard"]

        # Ajuste por peso
        if total_weight > 2.0:
            base_cost += (total_weight - 2.0) * 2.0

        # Ajuste por localização
        if address.state in ["CA", "NY", "TX"]:
            base_cost += 2.0

        print(f"ShippingService: Calculated shipping cost: ${base_cost:.2f}")
        return base_cost

    def create_shipment(
        self, order_id: str, items: List[OrderItem], address: Address
    ) -> Dict[str, Any]:
        tracking_number = f"TRK{uuid.uuid4().hex[:10].upper()}"
        estimated_delivery = datetime.now() + timedelta(days=5)

        shipment_info = {
            "tracking_number": tracking_number,
            "order_id": order_id,
            "estimated_delivery": estimated_delivery,
            "status": "created",
        }

        self.shipments[tracking_number] = shipment_info
        print(
            f"ShippingService: Created shipment {tracking_number} for order {order_id}"
        )
        return shipment_info


class NotificationService:
    def __init__(self):
        self.sent_notifications = []

    def send_order_confirmation(
        self, customer_id: str, order_info: Dict[str, Any]
    ) -> bool:
        notification = {
            "type": "order_confirmation",
            "customer_id": customer_id,
            "order_id": order_info.get("order_id"),
            "timestamp": datetime.now(),
        }
        self.sent_notifications.append(notification)
        print(f"NotificationService: Sent order confirmation to customer {customer_id}")
        return True

    def send_shipping_notification(
        self, customer_id: str, tracking_info: Dict[str, Any]
    ) -> bool:
        notification = {
            "type": "shipping_notification",
            "customer_id": customer_id,
            "tracking_number": tracking_info.get("tracking_number"),
            "timestamp": datetime.now(),
        }
        self.sent_notifications.append(notification)
        print(
            f"NotificationService: Sent shipping notification to customer {customer_id}"
        )
        return True

    def send_payment_notification(
        self, customer_id: str, payment_info: Dict[str, Any]
    ) -> bool:
        notification = {
            "type": "payment_confirmation",
            "customer_id": customer_id,
            "transaction_id": payment_info.get("transaction_id"),
            "timestamp": datetime.now(),
        }
        self.sent_notifications.append(notification)
        print(
            f"NotificationService: Sent payment confirmation to customer {customer_id}"
        )
        return True


class AuditService:
    def __init__(self):
        self.audit_logs = []

    def log_order_event(
        self, order_id: str, event_type: str, details: Dict[str, Any]
    ) -> bool:
        log_entry = {
            "timestamp": datetime.now(),
            "type": "order_event",
            "order_id": order_id,
            "event_type": event_type,
            "details": details,
        }
        self.audit_logs.append(log_entry)
        print(f"AuditService: Logged {event_type} event for order {order_id}")
        return True

    def log_payment_event(self, transaction_id: str, event_type: str) -> bool:
        log_entry = {
            "timestamp": datetime.now(),
            "type": "payment_event",
            "transaction_id": transaction_id,
            "event_type": event_type,
        }
        self.audit_logs.append(log_entry)
        print(
            f"AuditService: Logged {event_type} payment event for transaction {transaction_id}"
        )
        return True


# FACADE - Interface simplificada que coordena todos os subsistemas
class ECommerceFacade:
    def __init__(self):
        self.catalog_service = ProductCatalogService()
        self.inventory_service = InventoryService()
        self.payment_service = PaymentService()
        self.shipping_service = ShippingService()
        self.notification_service = NotificationService()
        self.audit_service = AuditService()

        self.orders = {}

    def process_order(
        self,
        customer_id: str,
        items: List[OrderItem],
        payment_info: PaymentInfo,
        shipping_address: Address,
    ) -> OrderResult:
        """
        Método principal que coordena todos os subsistemas para processar um pedido.
        O cliente só precisa chamar este método - toda a complexidade é gerenciada internamente.
        """
        print(f"\n=== Processing Order for Customer {customer_id} ===")

        order_id = str(uuid.uuid4())

        try:
            # 1. Validar produtos e calcular totais
            print("Step 1: Validating products and calculating totals...")
            total_amount = 0.0
            for item in items:
                if not self.catalog_service.validate_product_exists(item.product_id):
                    return OrderResult(
                        False,
                        None,
                        0.0,
                        None,
                        None,
                        f"Product {item.product_id} not found",
                    )

                product_price = self.catalog_service.get_product_price(item.product_id)
                item.unit_price = product_price
                total_amount += product_price * item.quantity

            # 2. Verificar disponibilidade no estoque
            print("Step 2: Checking inventory availability...")
            for item in items:
                if not self.inventory_service.check_availability(
                    item.product_id, item.quantity
                ):
                    return OrderResult(
                        False,
                        None,
                        0.0,
                        None,
                        None,
                        f"Insufficient stock for {item.product_id}",
                    )

            # 3. Calcular custos de envio
            print("Step 3: Calculating shipping costs...")
            shipping_cost = self.shipping_service.calculate_shipping_cost(
                items, shipping_address
            )
            total_amount += shipping_cost

            # 4. Processar pagamento
            print("Step 4: Processing payment...")
            payment_result = self.payment_service.process_payment(
                total_amount, payment_info
            )
            if not payment_result["success"]:
                return OrderResult(
                    False, None, total_amount, None, None, payment_result.get("error")
                )

            # 5. Reservar itens no estoque
            print("Step 5: Reserving inventory...")
            for item in items:
                if not self.inventory_service.reserve_items(
                    item.product_id, item.quantity, order_id
                ):
                    # Rollback do pagamento seria necessário em um sistema real
                    return OrderResult(
                        False,
                        None,
                        total_amount,
                        None,
                        None,
                        "Failed to reserve inventory",
                    )

            # 6. Criar envio
            print("Step 6: Creating shipment...")
            shipment_info = self.shipping_service.create_shipment(
                order_id, items, shipping_address
            )

            # 7. Enviar notificações
            print("Step 7: Sending notifications...")
            order_info = {
                "order_id": order_id,
                "total_amount": total_amount,
                "items": items,
            }
            self.notification_service.send_order_confirmation(customer_id, order_info)
            self.notification_service.send_payment_notification(
                customer_id, payment_result
            )
            self.notification_service.send_shipping_notification(
                customer_id, shipment_info
            )

            # 8. Registrar auditoria
            print("Step 8: Logging audit events...")
            self.audit_service.log_order_event(
                order_id,
                "order_created",
                {
                    "customer_id": customer_id,
                    "total_amount": total_amount,
                    "item_count": len(items),
                },
            )
            self.audit_service.log_payment_event(
                payment_result["transaction_id"], "payment_processed"
            )

            # 9. Armazenar pedido
            self.orders[order_id] = {
                "customer_id": customer_id,
                "items": items,
                "total_amount": total_amount,
                "status": OrderStatus.CONFIRMED,
                "created_at": datetime.now(),
                "tracking_number": shipment_info["tracking_number"],
            }

            print(f"=== Order {order_id} processed successfully! ===\n")

            return OrderResult(
                success=True,
                order_id=order_id,
                total_amount=total_amount,
                estimated_delivery=shipment_info["estimated_delivery"],
                tracking_number=shipment_info["tracking_number"],
            )

        except Exception as e:
            print(f"Error processing order: {str(e)}")
            # Em um sistema real, aqui teria rollback completo
            return OrderResult(False, None, 0.0, None, None, f"System error: {str(e)}")

    def get_product_details(self, product_id: str) -> Optional[Product]:
        """Método simplificado para obter detalhes de produto"""
        return self.catalog_service.get_product(product_id)

    def check_product_availability(self, product_id: str, quantity: int) -> bool:
        """Método simplificado para verificar disponibilidade"""
        return self.catalog_service.validate_product_exists(
            product_id
        ) and self.inventory_service.check_availability(product_id, quantity)

    def calculate_order_total(
        self, items: List[OrderItem], shipping_address: Address
    ) -> Dict[str, float]:
        """Método simplificado para calcular total do pedido"""
        subtotal = 0.0
        for item in items:
            price = self.catalog_service.get_product_price(item.product_id)
            subtotal += price * item.quantity

        shipping_cost = self.shipping_service.calculate_shipping_cost(
            items, shipping_address
        )
        total = subtotal + shipping_cost

        return {"subtotal": subtotal, "shipping": shipping_cost, "total": total}

    def cancel_order(self, order_id: str, reason: str) -> bool:
        """Método simplificado para cancelar pedido"""
        if order_id not in self.orders:
            return False

        print(f"Cancelling order {order_id}...")

        # Liberar reservas de estoque
        self.inventory_service.release_reservation(order_id)

        # Atualizar status do pedido
        self.orders[order_id]["status"] = OrderStatus.CANCELLED

        # Registrar auditoria
        self.audit_service.log_order_event(
            order_id, "order_cancelled", {"reason": reason}
        )

        print(f"Order {order_id} cancelled successfully")
        return True

    def get_order_status(self, order_id: str) -> Optional[Dict[str, Any]]:
        """Método simplificado para consultar status do pedido"""
        return self.orders.get(order_id)


# Cliente que usa o sistema através do Facade
class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.ecommerce = ECommerceFacade()

    def place_order(
        self,
        items: List[OrderItem],
        payment_info: PaymentInfo,
        shipping_address: Address,
    ) -> OrderResult:
        """
        Cliente faz pedido através do Facade - não precisa conhecer subsistemas internos
        """
        return self.ecommerce.process_order(
            self.customer_id, items, payment_info, shipping_address
        )

    def view_product(self, product_id: str) -> Optional[Product]:
        return self.ecommerce.get_product_details(product_id)

    def check_availability(self, product_id: str, quantity: int) -> bool:
        return self.ecommerce.check_product_availability(product_id, quantity)


# Exemplo de uso
def main():
    # Criando um cliente
    customer = Customer("CUST001", "John Doe")

    # Criando endereço de entrega
    shipping_address = Address(
        street="123 Main St",
        city="New York",
        state="NY",
        zip_code="10001",
        country="USA",
    )

    # Criando informações de pagamento
    payment_info = PaymentInfo(
        card_number="4111111111111111",  # Número de teste válido
        expiry_date="12/25",
        cvv="123",
        cardholder_name="John Doe",
        billing_address={
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "zip_code": "10001",
        },
    )

    # Consultando produtos disponíveis
    print("=== Product Catalog ===")
    laptop = customer.view_product("LAPTOP001")
    if laptop:
        print(f"Product: {laptop.name} - ${laptop.price}")
        print(f"Available: {customer.check_availability('LAPTOP001', 1)}")

    mouse = customer.view_product("MOUSE001")
    if mouse:
        print(f"Product: {mouse.name} - ${mouse.price}")
        print(f"Available: {customer.check_availability('MOUSE001', 2)}")

    # Criando itens do pedido
    order_items = [
        OrderItem("LAPTOP001", 1, 0.0),  # Preço será definido pelo sistema
        OrderItem("MOUSE001", 2, 0.0),
        OrderItem("BOOK001", 1, 0.0),
    ]

    # Calculando total antes do pedido
    ecommerce = ECommerceFacade()
    order_total = ecommerce.calculate_order_total(order_items, shipping_address)
    print(f"\n=== Order Summary ===")
    print(f"Subtotal: ${order_total['subtotal']:.2f}")
    print(f"Shipping: ${order_total['shipping']:.2f}")
    print(f"Total: ${order_total['total']:.2f}")

    # Processando o pedido (toda a complexidade é escondida no Facade)
    result = customer.place_order(order_items, payment_info, shipping_address)

    if result.success:
        print(f"\nOrder placed successfully!")
        print(f"Order ID: {result.order_id}")
        print(f"Total Amount: ${result.total_amount:.2f}")
        print(f"Tracking Number: {result.tracking_number}")
        print(f"Estimated Delivery: {result.estimated_delivery.strftime('%Y-%m-%d')}")

        # Consultando status do pedido
        order_status = ecommerce.get_order_status(result.order_id)
        if order_status:
            print(f"Order Status: {order_status['status'].value}")

        # Demonstrando cancelamento
        print(f"\n=== Order Cancellation Test ===")
        cancel_success = ecommerce.cancel_order(
            result.order_id, "Customer changed mind"
        )
        print(f"Cancellation successful: {cancel_success}")

    else:
        print(f"Order failed: {result.error_message}")

    # Testando pedido com erro (produto inexistente)
    print(f"\n=== Error Handling Test ===")
    error_items = [OrderItem("INVALID001", 1, 0.0)]
    error_result = customer.place_order(error_items, payment_info, shipping_address)
    print(f"Error order result: {error_result.error_message}")


if __name__ == "__main__":
    main()
