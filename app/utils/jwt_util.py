from contextvars import ContextVar

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

jwt_payload_context: ContextVar[dict | None] = ContextVar("jwt_payload", default=None)
jwt_token_context: ContextVar[str | None] = ContextVar("jwt_token", default=None)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> dict:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if not credentials or credentials.scheme.lower() != "bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme")

        token = credentials.credentials
        payload = self.decode_token(token)
        jwt_token_context.set(token)
        jwt_payload_context.set(payload)
        return payload

    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            return payload
        except Exception:
            raise HTTPException(status_code=403, detail="Invalid token")


jwt_bearer = JWTBearer()


def get_jwt_token() -> str:
    return jwt_token_context.get()


def get_claim(key: str):
    payload = jwt_payload_context.get()
    return payload.get(key)


def get_all_claims():
    return jwt_payload_context.get()


def get_authenticated_user_id():
    user_id = get_claim("sub")
    if not user_id:
        raise RuntimeError("JWT claim 'sub' not set in context")
    return user_id
