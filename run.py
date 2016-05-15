from argparse import ArgumentParser
from application import app


def options():
    parser = ArgumentParser()
    parser.add_argument('port', type=int, default=5000, nargs='?')

    return parser.parse_args()


if __name__ == '__main__':
    port = options().port
    app.run(port=port)
