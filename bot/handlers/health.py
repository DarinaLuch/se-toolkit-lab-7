import httpx
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import load_config

async def handle_health(args: str = "") -> str:
    """Handle /health command - check backend status."""
    config = load_config()
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.lms_api_base_url}/docs",
                timeout=5.0
            )
            if response.status_code == 200:
                return "✅ Backend is healthy and responding!"
            else:
                return f"⚠️ Backend returned status code: {response.status_code}"
    except httpx.TimeoutException:
        return "❌ Backend timeout - service might be down"
    except httpx.ConnectError:
        return "❌ Cannot connect to backend - is it running?"
    except Exception as e:
        return f"❌ Error checking backend: {str(e)}"
