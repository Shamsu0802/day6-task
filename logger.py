import logging
import time
from fastapi import Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("app")


async def log_requests(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"{request.method} {request.url.path} "
            f"Status={response.status_code} "
            f"Latency={process_time:.3f}s"
        )

        return response

    except Exception as e:

        process_time = time.time() - start_time

        logger.error(
            f"{request.method} {request.url.path} "
            f"FAILED after {process_time:.3f}s "
            f"Error={str(e)}"
        )

        raise