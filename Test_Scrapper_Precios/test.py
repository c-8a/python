import requests
from bs4 import BeautifulSoup
import json

def obtener_precio_alcampo(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        script_json = soup.select_one('script[type="application/ld+json"]')
        if script_json:
            data = json.loads(script_json.string)
            if "offers" in data and "price" in data["offers"]:
                return data["offers"]["price"]
            else:
                print(f"No se encontró la clave 'price' dentro de 'offers' en el JSON.")
                return None
        else:
            print("No se encontró el script JSON con la información del producto.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

if __name__ == "__main__":
    url_producto = "https://www.compraonline.alcampo.es/products/producto-alcampo-papel-higi%C3%A9nico-compacto-de-doble-capa-con-certificado-ecolabel-12-uds/439123"  # Reemplaza con la URL real
    precio = obtener_precio_alcampo(url_producto)
    if precio:
        print(f"El precio del producto es: {precio}")