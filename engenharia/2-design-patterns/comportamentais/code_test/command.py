from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class TextDocument:
    def __init__(self):
        self._content = ""

    def insert_text(self, position: int, text: str) -> None:
        if 0 <= position <= len(self._content):
            self._content = self._content[:position] + text + self._content[position:]
        else:
            raise ValueError(
                f"Posição {position} inválida para documento de tamanho {len(self._content)}"
            )

    def delete_text(self, position: int, length: int) -> str:
        if position < 0 or position + length > len(self._content):
            raise ValueError(
                f"Tentativa de deletar texto fora dos limites do documento"
            )

        deleted_text = self._content[position : position + length]
        self._content = self._content[:position] + self._content[position + length :]
        return deleted_text

    def get_content(self) -> str:
        return self._content

    def get_length(self) -> int:
        return len(self._content)


class InsertCommand(Command):
    def __init__(self, document: TextDocument, position: int, text: str):
        self._document = document
        self._position = position
        self._text = text
        self._executed = False

    def execute(self) -> None:
        if self._executed:
            raise RuntimeError("Comando já foi executado")

        self._document.insert_text(self._position, self._text)
        self._executed = True

    def undo(self) -> None:
        if not self._executed:
            raise RuntimeError("Comando não foi executado ainda")

        self._document.delete_text(self._position, len(self._text))
        self._executed = False

    def __str__(self) -> str:
        return f"InsertCommand(pos={self._position}, text='{self._text}')"


class DeleteCommand(Command):
    def __init__(self, document: TextDocument, position: int, length: int):
        self._document = document
        self._position = position
        self._length = length
        self._deleted_text = ""
        self._executed = False

    def execute(self) -> None:
        if self._executed:
            raise RuntimeError("Comando já foi executado")

        self._deleted_text = self._document.delete_text(self._position, self._length)
        self._executed = True

    def undo(self) -> None:
        if not self._executed:
            raise RuntimeError("Comando não foi executado ainda")

        self._document.insert_text(self._position, self._deleted_text)
        self._executed = False

    def __str__(self) -> str:
        return f"DeleteCommand(pos={self._position}, length={self._length})"


class MacroCommand(Command):
    def __init__(self, commands: List[Command]):
        self._commands = commands.copy()
        self._executed = False

    def execute(self) -> None:
        if self._executed:
            raise RuntimeError("Macro já foi executado")

        for command in self._commands:
            command.execute()
        self._executed = True

    def undo(self) -> None:
        if not self._executed:
            raise RuntimeError("Macro não foi executado ainda")

        # Desfaz na ordem inversa
        for command in reversed(self._commands):
            command.undo()
        self._executed = False

    def __str__(self) -> str:
        return f"MacroCommand({len(self._commands)} comandos)"


class TextEditor:
    def __init__(self):
        self._document = TextDocument()
        self._command_history: List[Command] = []
        self._current_position = -1  # Posição do último comando executado

    def execute_command(self, command: Command) -> None:
        # Remove comandos após a posição atual (para casos de undo seguido de nova operação)
        self._command_history = self._command_history[: self._current_position + 1]

        # Executa o comando
        command.execute()

        # Adiciona à história
        self._command_history.append(command)
        self._current_position += 1

        print(f"Executado: {command}")
        print(f"Documento: '{self._document.get_content()}'")

    def undo(self) -> bool:
        if self._current_position < 0:
            print("Nada para desfazer")
            return False

        command = self._command_history[self._current_position]
        command.undo()
        self._current_position -= 1

        print(f"Desfeito: {command}")
        print(f"Documento: '{self._document.get_content()}'")
        return True

    def redo(self) -> bool:
        if self._current_position >= len(self._command_history) - 1:
            print("Nada para refazer")
            return False

        self._current_position += 1
        command = self._command_history[self._current_position]
        command.execute()

        print(f"Refeito: {command}")
        print(f"Documento: '{self._document.get_content()}'")
        return True

    def get_content(self) -> str:
        return self._document.get_content()

    def create_macro(self, commands: List[Command]) -> MacroCommand:
        return MacroCommand(commands)


# Exemplo de uso
def main():
    editor = TextEditor()

    print("=== Demonstração do Editor de Texto ===\n")

    # Operações básicas
    print("1. Inserindo texto...")
    editor.execute_command(InsertCommand(editor._document, 0, "Olá"))
    editor.execute_command(InsertCommand(editor._document, 3, " Mundo"))
    editor.execute_command(InsertCommand(editor._document, 9, "!"))

    print("\n2. Deletando texto...")
    editor.execute_command(DeleteCommand(editor._document, 4, 5))  # Remove "Mundo"

    print("\n3. Testando Undo...")
    editor.undo()  # Desfaz delete
    editor.undo()  # Desfaz insert "!"

    print("\n4. Testando Redo...")
    editor.redo()  # Refaz insert "!"

    print("\n5. Nova operação após undo...")
    editor.execute_command(InsertCommand(editor._document, 9, " Python"))

    print("\n6. Testando Macro...")
    macro_commands = [
        InsertCommand(editor._document, 16, " é"),
        InsertCommand(editor._document, 18, " incrível"),
    ]
    macro = editor.create_macro(macro_commands)
    editor.execute_command(macro)

    print("\n7. Desfazendo macro...")
    editor.undo()

    print("\n8. Estado final do editor...")
    print(f"Conteúdo: '{editor.get_content()}'")
    print(f"Comandos na história: {len(editor._command_history)}")


if __name__ == "__main__":
    main()
