from typing import Tuple, List

from telegram_envelope.simple_text_bot import InputMessage
from telegram_envelope.utils import parse_command

KG_LIST: List[float] = [25, 20, 15, 10, 5, 2.5, 1.25]
KG_BARBELL = 20

COMMAND_KG = "kg"
COMMAND_ECHO = "eco"
COMMAND_HELP = "ayuda"
COMMAND_START = "start"


def kg_calc(kg: float) -> List[float]:
    def recursive_list(load_left: float, plates_left: List[float], plates_loaded: List[float]) -> List[float]:
        if len(plates_left) > 0 and load_left >= plates_left[0]:
            return recursive_list(load_left - plates_left[0], plates_left, plates_loaded + [plates_left[0]])
        elif len(plates_left) > 0 and load_left < plates_left[0]:
            return recursive_list(load_left, plates_left[1:], plates_loaded)
        else:
            return plates_loaded

    if kg > KG_BARBELL:
        return recursive_list((kg - KG_BARBELL) / 2.0, KG_LIST, [])
    else:
        return []


def barbell_logic(input_message: InputMessage) -> Tuple[str, bool]:
    cmd, rest = parse_command(input_message.text)
    is_reply = True

    if cmd == COMMAND_KG:
        try:
            load = float(rest)
            plates = kg_calc(load)
            total = sum(plates)
            if total > 0:
                extra_text = f" Discos a cargar: {', '.join([str(p) for p in plates])}"
            else:
                extra_text = ""
            result = f"Debes cargar {total}kg a cada lado de la barra.{extra_text}"
        except ValueError:
            result = "El comando /kg debe estar seguido de un número (decimales separados por \".\")\n" \
                     "Por ejemplo: /kg 102.5"

    elif cmd == COMMAND_START:
        result = "¡Hola! Bienvenido/a a Barbell Bot. Escribe /ayuda para mostrar la lista de comandos."
    elif cmd == COMMAND_HELP:
        result = "Este Bot es una calculadora de carga de discos para barras olímpicas (20kg)\n" \
                 "Para calcular la carga escribe /kg seguido de un número (decimales separados por \".\")\n" \
                 "Por ejemplo: /kg 102.5"
    elif cmd == COMMAND_ECHO:
        result = rest
    else:
        result = "Comando no reconocido o incompleto. Escribe /ayuda para mostrar la lista de comandos."

    return result, is_reply
