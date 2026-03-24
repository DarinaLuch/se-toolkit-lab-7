async def handle_scores(args: str = "") -> str:
    """Handle /scores command - get scores for a lab."""
    if not args:
        return "Please specify a lab name. Example: /scores lab-04"
    
    return (
        f"📊 Scores for {args}:\n\n"
        f"This is a placeholder. Real implementation will:\n"
        f"• Fetch scores from LMS API\n"
        f"• Show student performance\n"
        f"• Display task completion stats\n\n"
        f"Check back after Task 2 implementation!"
    )
