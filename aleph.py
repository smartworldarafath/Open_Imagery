"""Compatibility entrypoint redirecting to open_imagery."""

from open_imagery import *
from open_imagery import main

if __name__ == "__main__":
    raise SystemExit(main())
