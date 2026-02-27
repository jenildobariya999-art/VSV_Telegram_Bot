import requests
from config import VSV_TOKEN

def vsv_transfer(paytm_number, amount, comment):
    url = f"https://vsv-gateway-solutions.co.in/Api/api.php?token={VSV_TOKEN}&paytm={paytm_number}&amount={amount}&comment={comment}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}
