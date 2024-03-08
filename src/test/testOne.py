import jwt
from src.backend.settings import setting

username = "asd"
p_bytes = str(b'username').replace("b'", "").replace("'", "")
print(type(str.encode(p_bytes, encoding="utf-8")), str.encode(p_bytes, encoding="utf-8"))

token = "eyJzdWIiOiIxIiwidXNlciI6eyJ1c2VybmFtZSI6InN0cmluZyIsImVtYWlsIjoic3RyaW5nIiwiaWQiOjEsInJvbGUiOiJVc2VyIn0sImV4cCI6MTcwOTg4MDgxNiwiaWF0IjoxNzA5ODc5OTE2fQ.UOTJhPzFbWRwXQNcuVNswqlVfl40ua6ZriSqOZ88YjtW4TQ0FvpWfipgbC2s4E2S0B6vN5vmhiu0n-a8yS-ZFUv7IHEaKT6djtHL9dCtYnTx59QmI-JqQi_2EFPd-gpQVVzfKpKDR-yKnesWnEUV4d-SsDhh0iPRIGEUicGi7SH8eRE6Sipmpp7BlJ1_LayTW69DNv2Zi_I1drN-X3K4VGqN95iCDyoxW_vqS-9hIJu3miUJH5zjhafNwd0FI-7Q6d4sePvOJr53JsbSnuODp1rSW7I7ew5YAn3WdftDy4M5Dg-gS2AcdRiPXh8TUUVuVQwLyf6jOVExAVgmHBYljA"

print(jwt.decode(jwt=token, key=setting.auth.public_key_path.read_text(), algorithms='RS256'))