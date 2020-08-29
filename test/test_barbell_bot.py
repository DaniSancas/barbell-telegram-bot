from telegram_envelope.simple_text_bot import InputMessage

from barbell_bot import kg_calc, barbell_logic


def test_kg_calc():
    assert [] == kg_calc(10.0)
    assert [] == kg_calc(20.0)
    assert [1.25] == kg_calc(22.5)
    assert [10] == kg_calc(40.0)
    assert [10, 2.5] == kg_calc(45.0)
    assert [10, 2.5, 1.25] == kg_calc(47.5)
    assert [25, 25, 25] == kg_calc(170)
    assert [10] == kg_calc(41)  # Less than 42.5, so rounded to 40


def test_barbell_logic():
    assert barbell_logic(InputMessage(123, "/kg 20", 456)) == \
           (f"Debes cargar 0kg a cada lado de la barra.", True)
    assert barbell_logic(InputMessage(123, "/kg 100", 456)) == \
           (f"Debes cargar 40kg a cada lado de la barra. Discos a cargar: 25, 15", True)
    assert barbell_logic(InputMessage(123, "/kg not a number", 456)) == \
           ("El comando /kg debe estar seguido de un número (decimales separados por \".\")\n"
            "Por ejemplo: /kg 102.5", True)
    assert barbell_logic(InputMessage(123, "/start not a number", 456)) == \
           ("¡Hola! Bienvenido/a a Barbell Bot. Escribe /ayuda para mostrar la lista de comandos.", True)
    assert barbell_logic(InputMessage(123, "/ayuda", 456)) == \
           ("Este Bot es una calculadora de carga de discos para barras olímpicas (20kg)\n"
            "Para calcular la carga escribe /kg seguido de un número (decimales separados por \".\")\n"
            "Por ejemplo: /kg 102.5", True)
    assert barbell_logic(InputMessage(123, "/eco something", 456)) == \
           ("something", True)
    assert barbell_logic(InputMessage(123, "/unknown", 456)) == \
           ("Comando no reconocido o incompleto. Escribe /ayuda para mostrar la lista de comandos.", True)
