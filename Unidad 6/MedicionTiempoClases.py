import time

class TimerError(Exception):
    """Mensaje de Error"""
    pass

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Comienza un nuevo temporizador"""
        if self._start_time is not None:
            raise TimerError("El tiempo está corriendo. Usa .stop() para parar esto")

        self._start_time = time.perf_counter()

    def stop(self):
        """Detiene el tiempo y lo reporta"""
        if self._start_time is None:
            raise TimerError("El tiempo no está corriendo. Usa .start() para comenzarlo")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Tiempo: {elapsed_time:0.4f} segundos")