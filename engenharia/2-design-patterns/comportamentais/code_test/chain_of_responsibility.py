from abc import ABC, abstractmethod
from typing import Optional


class ExpenseRequest:
    def __init__(self, amount: float, description: str, requester: str):
        self.amount = amount
        self.description = description
        self.requester = requester

    def __str__(self):
        return f"Despesa: R$ {self.amount:.2f} - {self.description} (Solicitante: {self.requester})"


class ApprovalHandler(ABC):
    def __init__(self):
        self._next_handler: Optional[ApprovalHandler] = None

    def set_next(self, handler: "ApprovalHandler") -> "ApprovalHandler":
        self._next_handler = handler
        return handler

    def handle(self, request: ExpenseRequest) -> str:
        if self.can_approve(request.amount):
            return self._approve(request)
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return f"Despesa de R$ {request.amount:.2f} rejeitada - valor acima do limite autorizado"

    @abstractmethod
    def can_approve(self, amount: float) -> bool:
        pass

    @abstractmethod
    def _approve(self, request: ExpenseRequest) -> str:
        pass


class SupervisorHandler(ApprovalHandler):
    def can_approve(self, amount: float) -> bool:
        return amount <= 1000.00

    def _approve(self, request: ExpenseRequest) -> str:
        return f"APROVADO pelo Supervisor: {request}"


class ManagerHandler(ApprovalHandler):
    def can_approve(self, amount: float) -> bool:
        return amount <= 5000.00

    def _approve(self, request: ExpenseRequest) -> str:
        return f"APROVADO pelo Gerente: {request}"


class DirectorHandler(ApprovalHandler):
    def can_approve(self, amount: float) -> bool:
        return amount <= 20000.00

    def _approve(self, request: ExpenseRequest) -> str:
        return f"APROVADO pelo Diretor: {request}"


class CEOHandler(ApprovalHandler):
    def can_approve(self, amount: float) -> bool:
        return amount <= 100000.00

    def _approve(self, request: ExpenseRequest) -> str:
        return f"APROVADO pelo CEO: {request}"


# Configuração da cadeia
def create_approval_chain() -> ApprovalHandler:
    supervisor = SupervisorHandler()
    manager = ManagerHandler()
    director = DirectorHandler()
    ceo = CEOHandler()

    supervisor.set_next(manager).set_next(director).set_next(ceo)

    return supervisor


# Exemplo de uso
def main():
    approval_chain = create_approval_chain()

    # Casos de teste
    requests = [
        ExpenseRequest(800.00, "Material de escritório", "João Silva"),
        ExpenseRequest(3500.00, "Notebook para desenvolvimento", "Maria Santos"),
        ExpenseRequest(15000.00, "Software de infraestrutura", "Pedro Costa"),
        ExpenseRequest(50000.00, "Servidor para datacenter", "Ana Oliveira"),
        ExpenseRequest(150000.00, "Aquisição de empresa", "Carlos Lima"),
    ]

    for request in requests:
        result = approval_chain.handle(request)
        print(result)
        print("-" * 80)


if __name__ == "__main__":
    main()
