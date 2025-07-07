import subprocess

#Clase para la invocacion al binario externo
class ExAnalyzer:
    def __init__(self, ruta_binario_ext: str = "/usr/bin/external-analyzer"):
        self.ruta_binario_ext = ruta_binario_ext
    #Data a analizar invocando al binario externo
    def analizar(self, input_data):
        result = subprocess.run([self.ruta_binario_ext, input_data], capture_output=True, text=True, check=True)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode
        }
