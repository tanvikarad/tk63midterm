from datetime import datetime
from decimal import Decimal

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


def test_memento_round_trip_restores_history():
    timestamp = datetime.now()
    calculation = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3"),
    )
    memento = CalculatorMemento(history=[calculation], timestamp=timestamp)

    restored = CalculatorMemento.from_dict(memento.to_dict())

    assert restored.history == [calculation]
    assert restored.timestamp == timestamp


def test_memento_round_trip_with_empty_history():
    memento = CalculatorMemento(history=[])

    restored = CalculatorMemento.from_dict(memento.to_dict())

    assert restored.history == []
