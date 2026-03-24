async def handle_labs(args: str = "") -> str:
    """Handle /labs command - list available labs."""
    return (
        "📚 Available Labs:\n\n"
        "• lab-01\n"
        "• lab-02\n"
        "• lab-03\n"
        "• lab-04\n"
        "• lab-05\n"
        "• lab-06\n"
        "• lab-07\n\n"
        "Use /scores <lab-name> to see scores\n"
        "Example: /scores lab-04\n\n"
        "(Full implementation coming in Task 2)"
    )
