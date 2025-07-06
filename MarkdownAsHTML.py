import markdown
import webbrowser
import os

def save_markdown_report(markdown_content, output_name="research_report"):
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=["fenced_code", "tables"])

    # Basic HTML wrapper
    full_html = f"""
    <html>
    <head>
        <title>{output_name.replace('_', ' ').title()}</title>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; padding: 2em; max-width: 800px; margin: auto; }}
            h1, h2, h3 {{ color: #333; }}
            code {{ background-color: #f5f5f5; padding: 2px 4px; border-radius: 4px; }}
            pre {{ background: #f0f0f0; padding: 1em; overflow-x: auto; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Save as HTML file
    file_path = f"{output_name}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    # Open in default browser
    webbrowser.open('file://' + os.path.realpath(file_path))

