import click
import webbrowser
import pyperclip


@click.command()
@click.option('--text', '-t', help='Enter text to search for')
@click.option('--engine', '-e', help='Prefered Search Engine (can only be google, duckduckgo, yandex or yandex bing)')
@click.version_option(version='0.01', prog_name='Web Search CLI')
def main(text, engine):

    """A command line program that takes a string as an argument, opens the browser and searches for string in prefered search engine (google, duckduckgo, yandex, bing).
    
    Usage:

    search --engine bing --text "how to learn coding"
    
    or
    
    search -e bing -t "how to learn coding"

    If no engine or text is specified, program opens google search engine and searches for last text copied to clipboard" """

    engine = engine or 'google'
    engine = engine.lower()

    if not text:
        text = pyperclip.paste()

    if engine == 'bing':
        url = f'https://www.bing.com/search?q={text}'
    elif engine == 'duckduckgo':
        url = f'https://duckduckgo.com/?q={text}'
    elif engine == 'yandex':
        url = f'https://yandex.com/search/?text={text}'
    elif engine == 'google':
        url = f'https://www.google.com/search?q={text}'

    webbrowser.open(url, new=1)


if __name__ == '__main__':
    main()