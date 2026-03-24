def handle_start(args: str = "") -> str:
    """Handle /start command."""
    return (
        "👋 Welcome to LMS Analytics Bot!\n\n"
        "Available commands:\n"
        "/start - Show this message\n"
        "/help - Show all commands\n"
        "/health - Check backend status\n"
        "/labs - List available labs\n"
        "/scores <lab> - Get scores for a lab\n\n"
        "You can also ask questions like:\n"
        "• What's my score for lab-04?\n"
        "• Show me the hardest tasks\n"
        "• How am I doing overall?\n\n"
        "Type /help for more details."
    )
